##### Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице
*Создаем вспомогательную таблицу, объединяющуюу всех жиовтных, добавим в нее столбец с возрастом жиовтных в месяцах:*
```
CREATE TABLE all_animals
SELECT * FROM dogs
UNION SELECT * FROM cats
UNION SELECT * FROM hamsters
UNION SELECT * FROM horses
UNION SELECT * FROM camels
UNION SELECT * FROM donkeys;
```
*Создаем таблицу “молодые животные”:*
```
CREATE TABLE young_animals
SELECT name_animal, birthday, commands, id_pet, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS age_in_month
FROM all_animals
WHERE birthday BETWEEN ADDDATE(CURDATE(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
```
Результат:
```
SELECT * FROM young_animals;
```
![](https://github.com/oposofia/Final_Attestation/blob/main/Pictures/Table_young_animals.png)
