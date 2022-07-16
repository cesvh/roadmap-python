class Person:
    objects_createds = 9
    def __init__(self, username):
        self.username = username


person1 = Person("Cesar")
person2 = Person("Angel")
print(f"person1: {person1.objects_createds}")
print(f"person2: {person2.objects_createds}")
print("------------------------------------")
# person1.objects_createds = 5
print(f"person1: {person1.objects_createds}")
print(f"person2: {person2.objects_createds}")
print("------------------------------------")
# person2.objects_createds = 3
print(f"person1: {person1.objects_createds}")
print(f"person2: {person2.objects_createds}")
print("------------------------------------")
Person.objects_createds = 0
print(f"Person: {Person.objects_createds}")
print(f"person1: {person1.objects_createds}")
print(f"person2: {person2.objects_createds}")
print("------------------------------------")
person1.objects_createds = 5
person2.objects_createds = 3
print(f"Person: {Person.objects_createds}")
print(f"person1: {person1.objects_createds}")
print(f"person2: {person2.objects_createds}")
