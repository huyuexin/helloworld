#dog.py
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friend='yuki'
    def sit(self):
        print(self.name.title()+" is now sitting!")
    def roll_over(self):
        print(self.name.title()+" rolled over.")
    def is_age(self):
        print(self.name.title()+ " 's age is " + str(self.age) +" .")
    def change_friend(self,new_friend):
        self.friend=new_friend

my_dog=Dog('hu',15)
my_dog.is_age()
my_dog.roll_over()
print(my_dog.name.title() + "'s age is " + str(my_dog.age) + '!')
my_dog.sit()
print(my_dog.name.title()+" 'friend is " + my_dog.friend)
#通过直接修改属性值
my_dog.friend='cici'
print(my_dog.name.title()+" 'friend is " + my_dog.friend)
#通过方法修改属性
my_dog.change_friend('hulili')
print(my_dog.name.title()+" 'friend is " + my_dog.friend)
class Guangdong_dog():
    def __init__(self,eat_what='everything'):
        self.eat_what=eat_what
    def describe_eat(self):
        print("this dog can eat"+self.eat_what)


class China_dog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
        #python2.7需要指定子类名称和self 另外class(object)
        #super(China_dog,self).__init__(name,age)
        #定义子类属性
        self.from_where='中国'
    #引用类 创建实例
        self.guangdong_dong=Guangdong_dog()
    #子类方法定义
    def describe_from_where(self):
        print(self.name.title()+" is from " + self.from_where)
    #重写父类属性，函数覆盖
    def sit(self):
        print(self.name.title() + " 能用中文坐下指挥，好聪明")


my_dog1=China_dog('hudong1',12)
my_dog1.sit()
print(my_dog1.name.title()+" 'friend is " + my_dog1.friend)
my_dog1.describe_from_where()
my_dog1.sit()
#引用独立类
my_dog1.guangdong_dong.describe_eat()



