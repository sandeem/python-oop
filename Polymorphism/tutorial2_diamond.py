# class A is at level 1, 
# class B and C is at level 2 which takes single inheritance from class A,
# class D is at level 3 which take multiple inheritance from both 
# class B and class C thus forming multi-level inheritance on class D
# which can access all the attributes and methods on class A, B and C

# method 1 - not overriding done in class B or c 
class A:
    def method(self):
        print("# method 1 - This method belongs to class A")
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.method()

# method 2 - overriding done only in class B 
class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
        print("# method 2 - This method belongs to class B")
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.method()

# method 3 - overriding done only in class C 
class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    pass

class C(A):
    def method(self):
        print("# method 3 - This method belongs to class C")
    pass

class D(B,C):
    pass

d=D()
d.method()

# method 4 - overriding done in both class B & C 
# due to method resolution order (MRO), it will print class B first 
# instead of class C, which is class B is before class C in D(B,C)
class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
        print("# method 4 - This method belongs to class B")
    pass

class C(A):
    def method(self):
        print("# method 4 - This method belongs to class C")
    pass

class D(B,C):
    pass

d=D()
d.method()