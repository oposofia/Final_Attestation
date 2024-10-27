##### Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. 
Содержание первоначальной таблицы Camels:

![](https://github.com/oposofia/Final_Attestation/blob/main/Pictures/Table_camels_first.png)
Удаляем из таблицы верблюдов:
```
DELETE FROM camels;
```
При возникновении ошибки «Error Code: 1175», можно поправить запрос следующим образом:
```
DELETE FROM camels
WHERE id_camel > 0;
```
Результат:

![](https://github.com/oposofia/Final_Attestation/blob/main/Pictures/Table_camels_delete.png)
##### Объединить таблицы лошади, и ослы в одну таблицу.
```
DROP TABLE IF EXISTS horses_and_donkeys;
CREATE TABLE horses_and_donkeys SELECT * FROM horses
UNION SELECT * FROM donkeys;
```
Результат:

![](https://github.com/oposofia/Final_Attestation/blob/main/Pictures/Table_horses_and_donkeys.png)
