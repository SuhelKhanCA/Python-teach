
class Student:

    
    prior_student = "AMU" # class variable or static var

    def __init__(self, name, age, height, isAdult):
        
        self.name = name
        self.age = age
        self.height = height
        self.isAdult = isAdult

    def increase_age(self):

        self.age = self.age + 10
        
        return self.age
    


s1 = Student("Suhel", 23, 163.5, True)
s2 = Student("Zainab", 13, 163.5, True)

Student.prior_student = "Aligarh Muslim University"


print(s1.prior_student)
print(s2.prior_student)

ans = s1.increase_age()
ans2 = s2.increase_age()

print(ans)
print(ans2)