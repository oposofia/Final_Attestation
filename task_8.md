##### Создать таблицы с иерархией из диаграммы в БД
```
DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;
USE human_friends;

DROP TABLE IF EXISTS animals;
CREATE TABLE animals
(
	id_animals INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	animal_type VARCHAR(30)
);

INSERT INTO animals (animal_type)
VALUES ("HomeAnilals"), ("PackAnimals");

DROP TABLE IF EXISTS home_animals;
CREATE TABLE home_animals
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    animal_class VARCHAR(30),
    id_animals INT,
    FOREIGN KEY (id_animals) REFERENCES animals (id_animals)
);

INSERT INTO home_animals (animal_class, id_animals)
VALUES ('cats', 1), ('dogs', 1), ('hamsters', 1);

DROP TABLE IF EXISTS pack_animals;
CREATE TABLE pack_animals
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    animal_class VARCHAR(30),
    id_animals INT,
    FOREIGN KEY (id_animals) REFERENCES animals (id_animals)
);

INSERT INTO pack_animals (animal_class, id_animals)
VALUES ('horse', 2), ('camel', 2), ('donkey', 2);

DROP TABLE IF EXISTS cats;
CREATE TABLE cats (
    id_cat INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES home_animals(id)
);

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs (
    id_dog INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES home_animals(id)
);

 DROP TABLE IF EXISTS hamsters;
 CREATE TABLE hamsters (
    id_hamster INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES home_animals(id)
);

DROP TABLE IF EXISTS horses;
 CREATE TABLE horses (
    id_horse INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES pack_animals(id)
);

DROP TABLE IF EXISTS camels;
 CREATE TABLE camels (
    id_camel INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES pack_animals(id)
);

DROP TABLE IF EXISTS donkeys;
 CREATE TABLE donkeys (
    id_donkey INT AUTO_INCREMENT PRIMARY KEY,
    name_animal VARCHAR(255),
    birthday DATE,
    commands TEXT,
    id_pet INT,
    FOREIGN KEY (id_pet) REFERENCES pack_animals(id)
);
```
Проверяем таблицы в базе данных:
```
SHOW TABLES;
```
Результат:
```
animals
camels
cats
dogs
donkeys
hamsters
home_animals
horses
pack_animals
```
