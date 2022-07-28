class Student:
    # def __init__(self, name, groupNumber, age):
    #     self.name = name
    #     self.groupNumber = groupNumber
    #     self.age = age

    def getName(self):
        return self.name

    def getAge(self, age):
        return self.age

    def getgroupNumber(self, groupNumber):
        return self.groupNumber

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setgroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


st1 = Student("Елена", 10, 21)
print(f"Имя {st1.name}")
print(f"Группа № {st1.groupNumber}")
print(f"Возраст {st1.age}")
st1.setName("Виктория")
print(f"Изменить имя на {st1.name}")

st2 = Student("Татьяна", 12, 22)
print(f"Имя {st2.name}")
print(f"Группа № {st2.groupNumber}")
print(f"Возраст {st2.age}")
st2.setAge(23)
print(f"Изменить возраст на {st2.age}")
