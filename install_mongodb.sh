#! /bin/sh

#скачиваем и добавляем репозиторий
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-
org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

#обновляем индексы
sudo apt-get update

#Устанавливаем пакеты
sudo apt-get install -y mongodb-org

#Запускаем приложение
sudo systemctl start mongod

#Добавляем в автозапуск
sudo systemctl enable mongod
