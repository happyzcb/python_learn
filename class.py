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

