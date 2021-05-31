import random


class Animal:
    def __init__(self, name):
        self.health = 50
        self.happiness = int(random.random()*100)
        self.sexvalue = random.random()
        if self.sexvalue <= 0.5 :
            self.sex = 'Macho'
        else:
            self.sex = 'Hembra'
        self.age = int(random.random()*10)
        while self.age == 0:
            self.age = int(random.random()*10)
        self.name = name
        self.species = "placeholderspecies"

    def rename(self, name):
        self.name = name

    def death(self):
        if self.health < 0:
            print("¡"+ self.name + " ha muerto!")
        if self.happiness < 0:
            print("¡"+ self.name + " se escapó!")

    def display_info(self):
        print('Nombre: ' + self.name)
        print('Especie:' + self.species)
        print('Edad: ' + str(self.age))
        print('Sexo: ' + self.sex)
        print('Felicidad:' + str(self.happiness) + '/100')
        print('Salud:' + str(self.health) + '/100')
        print("\n")


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = 'Lion'
        self.name = name
    
    def eat(food):
        if food == "Carne":
            self.health += 30
        if food == "Verduras":
            self.health -= 30

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = 'Tiger'
        self.name = name

    def eat(self, food):
        if food == "Carne":
            self.health += 30
        if food == "Verduras":
            self.health -= 30

class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = 'Bear'
        self.name = name

    def eat(self, food):
        if food == "Carne":
            self.health += 20
        if food == "Verduras":
            self.health += 20


class Zoo(Animal):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)	
        self.animals = []
        self.name = zoo_name


    def day_end(self):
#if time_counter = 8
        for animal in self.animals:
            animal.health -= 10
            animal.happiness -= random.random()*40  
#time_counter = 0


    def add_lion(self, name):
        self.animals.append( Lion(name) )

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )

    def add_bear(self, name):
        self.animals.append( Bear(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for item in self.animals:
            item.display_info()

zoo1 = Zoo("Zoo")

zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

zoo1.animals[3].eat("Carne")
zoo1.print_all_info()


#FALTA AGREGAR MODIFICADORES DE FELICIDAD
#FALTA AGREGAR MODIFICADORES ADICIONALES DE SALUD
#FALTA CREAR MENU INTERACTIVO
#FALTA CREAR SISTEMA DE PASO DE TIEMPO
#FALTA CREAR SISTEMA DE MUERTE/HUIDA DE ANIMALES
#FALTA IMPLEMENTAR BIBLIOTECA DE IMAGENES ASCII PARA ANIMALES
#FALTA AGREGAR MAS ANIMALES
#FALTA AGREGAR INCIDENCIAS POR PROBABILIDADES DURANTE PASO DE TIEMPO
#FALTA AGREGAR INSTANCIA DE FIN DE DIA