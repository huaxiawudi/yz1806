class Dog:
    def eat(self):
        print("喜欢大骨头")
        return self

    def bark(self):
        print("旺旺")
        return self

    def beat(self):
        print("要不死你")

dog = Dog()
# 链式调用
dog.eat().eat().bark().beat()