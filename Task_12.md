##### Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам
```
SELECT cats.name_animal, cats.birthday, cats.commands, home_animals.animal_class, animals.animal_type
FROM cats
LEFT JOIN home_animals ON home_animals.id = cats.id_pet
LEFT JOIN animals ON animals.id_animals=home_animals.id_animals
UNION
SELECT dogs.name_animal, dogs.birthday, dogs.commands, home_animals.animal_class, animals.animal_type
FROM dogs
LEFT JOIN home_animals ON home_animals.id = dogs.id_pet
LEFT JOIN animals ON animals.id_animals=home_animals.id_animals
UNION
SELECT hamsters.name_animal, hamsters.birthday, hamsters.commands, home_animals.animal_class, animals.animal_type
FROM hamsters
LEFT JOIN home_animals ON home_animals.id = hamsters.id_pet
LEFT JOIN animals ON animals.id_animals=home_animals.id_animals
UNION
SELECT horses.name_animal, horses.birthday, horses.commands, pack_animals.animal_class, animals.animal_type
FROM horses
LEFT JOIN pack_animals ON pack_animals.id = horses.id_pet
LEFT JOIN animals ON animals.id_animals=pack_animals.id_animals
UNION
SELECT camels.name_animal, camels.birthday, camels.commands, pack_animals.animal_class, animals.animal_type
FROM camels
LEFT JOIN pack_animals ON pack_animals.id = camels.id_pet
LEFT JOIN animals ON animals.id_animals=pack_animals.id_animals
UNION
SELECT donkeys.name_animal, donkeys.birthday, donkeys.commands, pack_animals.animal_class, animals.animal_type
FROM donkeys
LEFT JOIN pack_animals ON pack_animals.id = donkeys.id_pet
LEFT JOIN animals ON animals.id_animals=pack_animals.id_animals;
```
Результат:

![](https://github.com/oposofia/Final_Attestation/blob/main/Pictures/Table_All_Animals.png)
