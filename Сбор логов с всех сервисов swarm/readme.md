С OS Windows(Необходимо что бы был установленн  putty)
plink 10.2.12.11 -ssh -batch -l USER -pw "PASS" "cd logs && ./get_stack_logs.sh PMP --since=2m --until=2s"

Необходимо в файле skipt.py Указать свои верные данные
host = 'IPorNAME'
user = 'USER'
secret = 'PASSWORD'