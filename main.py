# Find an object in a List of objects in Python

class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return self.name


alice = Employee('Alice', 100)
bob = Employee('Bobbyhadz', 75)
carl = Employee('Carl', 75)

list_of_objects = [alice, bob, carl]

# ✅ Get the first object in a list that meets a condition
result = next(
    (obj for obj in list_of_objects if obj.name == 'Bobbyhadz'),
    None
)
print(result)  # 👉️ Bobbyhadz

print(result.name)  # 👉️ Bobbyhadz
print(result.salary)  # 👉️ 75