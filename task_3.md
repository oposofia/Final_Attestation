##### Для подключения дополнительного репозитория MySQL можно выполнить следующие шаги:

1. Переходим в режим суперпользователя:
```
sudo su
```
2. Добавляем ключ репозитория:

```
wget -O- https://repo.mysql.com/RPM-GPG-KEY-mysql-2022 | sudo apt-key add -
```

3. Добавляем репозиторий MySQL в систему:

```
echo "deb http://repo.mysql.com/apt/ubuntu/ $(lsb_release -sc) mysql-8.0" | sudo tee /etc/apt/sources.list.d/mysql.list
```

4. Обновляем список пакетов:

```
sudo apt update
```

5. Устанавливаем любой пакет из репозитория MySQL, например, пакет `mysql-shell`:

```
sudo apt install mysql-shell
```
