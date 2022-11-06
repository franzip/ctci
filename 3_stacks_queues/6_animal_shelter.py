from lib import Queue


class Animal():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class LinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return str(self)

    def __init__(self):
        self.head = None

    def append(self, value):
        item = self.Node(value)

        if not self.head:
            self.head = item
            return

        ptr = self.head

        while ptr.next:
            ptr = ptr.next

        ptr.next = item

    def delete(self, type):
        ptr = self.head

        if isinstance(ptr.data, type):
            self.head = ptr.next
            return

        while ptr.next:
            if isinstance(ptr.next.data, type):
                ptr.next = ptr.next.next
                return
            ptr = ptr.next

    def __str__(self):
        result, ptr = [], self.head
        while ptr:
            result.append(ptr)
            ptr = ptr.next

        return str(result)


class AnimalShelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.animals = LinkedList()

    def enqueue(self, animal):
        self.animals.append(animal)
        if isinstance(animal, Dog):
            self.dogs.add(animal)
        else:
            self.cats.add(animal)

    def dequeueAny(self):
        animal = self.animals.head
        if isinstance(animal.data, Dog):
            self.animals.delete(Dog)
            return self.dogs.remove()
        else:
            self.animals.delete(Cat)
            return self.cats.remove()

    def dequeueDog(self):
        dog = self.dogs.remove()
        self.animals.delete(Dog)
        return dog

    def dequeueCat(self):
        cat = self.cats.remove()
        self.animals.delete(Cat)
        return cat

    def __str__(self):
        return f"\nDogs: {self.dogs} \nCats: {self.cats}\nAnimals: {self.animals}"


animal_shelter = AnimalShelter()
animal_shelter.enqueue(Dog('Rocky'))
animal_shelter.enqueue(Cat('Beau'))
animal_shelter.enqueue(Dog('Zeus'))
animal_shelter.enqueue(Dog('Fido'))
animal_shelter.enqueue(Cat('Kitty'))
animal_shelter.enqueue(Cat('Luna'))

assert animal_shelter.dequeueAny().name == "Rocky"
assert animal_shelter.dequeueDog().name == "Zeus"
assert animal_shelter.dequeueCat().name == 'Beau'
assert animal_shelter.dequeueAny().name == "Fido"
