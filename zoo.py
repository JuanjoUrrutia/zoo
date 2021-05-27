import random


class Animal:
    def __init__(self):
        self.health = 100
        self.happiness = random.random()*100
        self.sexvalue = random.random()

    def sex_animal(self, sexvalue):
        if sexvalue <= 0.5 :
            sex = 'Macho'
        else:
            sex = 'Hembra'

    def display_info(self,name, health, happiness, species, age, sex):
        print('Nombre: ' + name)
        print('Especie:' + species)
        print('Edad: ' + age)
        print('Sexo: ' + sex)
        print('Felicidad:' + happiness + '/100')
        print('Salud:' + health + '/100')


class Lion(Animal):
    def __init__(self, name):
        self.species = 'Lion'
        self.name = name

class Tiger(Animal):
    def __init__(self, name):
        self.species = 'Tiger'
        self.name = name

class Bear(Animal):
    def __init__(self, name):
        self.species = 'Bear'
        self.name = name


class Zoo:
    def __init__(self, zoo_name):   
        self.animals = []
        self.name = zoo_name

    def day_end(self, health, happiness):
        for animal in self.animals:
            health -= 10
            happiness -= random.random()*40

    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Zoo")
zoo1.add_lion("Nala")
#zoo1.add_lion("Simba")
#zoo1.add_tiger("Rajah")
#zoo1.add_tiger("Shere Khan")
#zoo1.print_all_info()

print(zoo1.name)

zoo1.print_all_info()
