import paramiko 
import subprocess

host = 'IP'
user = 'USER'
secret = 'PASS'
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)
# Выполнение команды
client.exec_command('mkdir /tmp/fromswarm/')
subprocess.run(["sshpass", "-p", (secret), "scp", "get_stack_logs.sh", f"{user}@{host}:/tmp/fromswarm/get_stack_logs.sh"])
stdin, stdout, stderr = client.exec_command('/tmp/fromswarm/get_stack_logs.sh PMP --since=2m --until=2s')
while True:
    print(stdout.read().decode(), end='')
    if stdout.channel.exit_status_ready():
        break
while True:
    print(stderr.read().decode(), end='')
    if stderr.channel.exit_status_ready():
        break
stdin, stdout, stderr = client.exec_command('cd /tmp/fromswarm && find /tmp/fromswarm -type d -mmin -5 | grep logs')
for line in stdout:
    file = (line)
print (file)
subprocess.run(["sshpass", "-p", (secret), "scp", "-r", f"{user}@{host}:{file}",  "fromswarm"])
while True:
    print(stdout.read().decode(), end='')
    if stdout.channel.exit_status_ready():
        break
while True:
    print(stderr.read().decode(), end='')
    if stderr.channel.exit_status_ready():
        break
client.exec_command('rm -rf /tmp/fromswarm')
data = stdout.read() + stderr.read()
client.close()