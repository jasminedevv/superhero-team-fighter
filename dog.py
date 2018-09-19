class Dog:
    greeting = "Woof!"
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.greeting)

if __name__ == "__main__":
    my_dog = Dog("Spot")
    my_dog.bark()
    print(my_dog.name)