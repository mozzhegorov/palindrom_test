# palindrom_test

Для запуска проекта в докер контейнере

docker build -t palindrom ./
docker run --name palindrom_test -v ${PWD}:/home -p 8001:8001 palindrom

остановка:
docker stop palindrom_test

удаление контейнера:
docker rm palindrom_test
