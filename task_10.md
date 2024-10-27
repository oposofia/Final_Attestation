##### Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. 

```
DELETE FROM camels;
```
При возникновении ошибки «Error Code: 1175», можно поправить запрос следующим образом:
```
DELETE FROM camels
WHERE id_camel > 0;
```
##### Объединить таблицы лошади, и ослы в одну таблицу.
```
DROP TABLE IF EXISTS horses_and_donkeys;
CREATE TABLE horses_and_donkeys SELECT * FROM horses
UNION SELECT * FROM donkeys;
```
