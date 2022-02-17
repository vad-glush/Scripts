#! /bin/sh

# Устанавливаем git

sudo apt-get install -y git

# копируем
git clone -b monolith https://github.com/express42/reddit.git

#  Переходим, устанавливаем зависимости 
cd reddit && bundle install

#Запускаем приложение из проекта
puma -d
