##### Установка и удаление deb-пакета с помощью dpkg

1. Скачиваем deb-пакет, например, Midnight Commander (MC):
```
wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mc/mc_4.8.25-2ubuntu2_amd64.deb
```
2. Устанавливаем deb-пакет:
```
sudo dpkg -i mc_4.8.25-2ubuntu2_amd64.deb
```
3. Если в процессе установки возникнут ошибки, которые необходимо исправить, выполним команду:
```
sudo apt --fix-broken install
```
4. Удаляем установленный пакет:
```
sudo dpkg -r mc
```
