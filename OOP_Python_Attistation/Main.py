from HomeAnimals import *
from PackAnimals import *
from Menu import *
from datetime import datetime
from AnimalRegister import *

animals_registry=AnimalRegister()
animals_registry.add(('Муся','кот',datetime(2024,1,10), ['голос']))
animals_registry.add(('Вася','кот',datetime(2020,5,11), ['сидеть']))
animals_registry.add(('Жулик','кот',datetime(2015,7,10), ['лежать']))
animals_registry.add(('Бобик','собака',datetime(2023,2,18), ['голос']))
animals_registry.add(('Хома','хомяк',datetime(2024,8,18), ['бегать']))
animals_registry.add(('Луна','лошадь',datetime(2018,6,30), ['галоп']))
animals_registry.add(('Гоша','осел',datetime(2020,10,3), ['стоять']))
animals_registry.add(('Султан','верблюд',datetime(2021,10,2), ['лежать']))
while True:
    match Menu.menu():
        case 1:
            animals_registry.add(Menu.for_one_menu())        
            print("\nЖивотное добавлено в реестр\n")            
        case 2: #2. Показать реестр
            print(f"В регистре находятся:\n")
            if len(animals_registry) == 0:
                print("В реестре еще нет животных. Добавьте животных в реестр")
            else: print(*animals_registry, sep='\n')
        case 3: #3. Обучить животное
            Menu.to_teach_animal_to_commands(animals_registry)            
        case 4: #4. Удалить животное из регистра
            del animals_registry[Menu.del_animal_from_register()]
        case 5: #5. Выход из программы
            print("До свидания!")
            break
        case _: #В случае ввода неверного значения
            print ("Для продолжения, введите пункт меню от 1 до 5")