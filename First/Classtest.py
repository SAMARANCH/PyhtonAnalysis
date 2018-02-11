
class Person(object):
   general = ''
   def __init__(self,name ,age):
       self.__age = age
       self.name = name

   def getAge(self):
       self.age=__age

class Student(Person):

    def __init__(self,name,age,gender):
        Person.__init__(self,name ,age)
        self.gender = gender


xiaohong = Person("xiaohong",15)
#instance attribute value change , but class value not change
xiaohong.general = 'change'
xiaolan = Person('xiaolan',16)
print  Person.general
print dir(xiaohong)
age = 10
name = 'shen'
print "i'm age %d name %s " %(age , name )