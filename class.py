# ========== protect ========
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)

# get properties and methods
print(dir('ABC'))

# ==========  getattr(), setattr(), hasattr() ==============
class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x

obj = Myobject()

print(hasattr(obj,'x'))  # 有属性'x'吗？
print(hasattr(obj,'y'))  # 有属性‘Y’吗？
setattr(obj,'y',19)  # 设置属性y
print(hasattr(obj,'y'))  # 有属性‘Y’吗？
print(getattr(obj,'y'))  # 有属性‘Y’吗？

#====================== advanced features =========================
#====================== __slots__ =================================
class Students(object):
    __slots__ = {'name','age'}

s = Students()
s.name = 'michael'
s.age = 25
try:
    s.score = 99  # AttributeError
except Exception as e:
    print(e)

class GraduateStudents(Students):
    pass
g = GraduateStudents()
g.score = 9999


# ========== @property =============================
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 复杂
s = Student()
s.set_score(60)
s.get_score()
try:
    s.set_score(9999)
except Exception as e:
    print(e)

# 采用decorator
class Student2(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth

s = Student2()
s.score = 60
print(s.score)
try:
    s.score = 9999
except Exception as e:
    print(e)

# =============== MixIn ==================
class Animal(object):
    pass

class Mamml(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    pass

class HerbivoresMixIn(object):
    pass

class Dog(Mamml,RunnableMixIn,CarnivorousMixIn):
    pass

