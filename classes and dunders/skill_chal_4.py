from math import sqrt
from functools import total_ordering
@total_ordering
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    def __abs__(self):
        return sqrt(self.x**2 + self.y **2 +self.z **2)
    def __add__(self,other):
        if not isinstance(other,Vector):
            raise TypeError("Vector object required")
        new=Vector(self.x+other.x, self.y + other.y, self.z + other.z)
        return new
    def __mul__(self,other):
        if not isinstance(other,int):
            raise TypeError("Int is required")
        new=Vector(self.x*other, self.y*other,self.z*other)
        return new
    def __rmul__(self,other):
        if not isinstance(other,int):
            raise TypeError("Int is required")
        return self*other
    def __gt__(self,other):
        if not isinstance(other,Vector):
            raise TypeError("Vector object required")
        return abs(self) > abs(other)
    def __eq__(self,other):
        if not isinstance(other,Vector):
            raise TypeError("Vector object required")
        return abs(self) == abs(other)
    def __bool__(self):
        return bool(self.__abs__())
    def __hash__(self):
        return hash((self.x,self.y,self.z))
    def __getitem__(self,item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")
        else:
            NotImplemented
v1=Vector(1,2,3)
v2=Vector(2,3,6)
v3=Vector(0,0,0)
print(bool(v1),bool(v3))
print(v1+v2)
print(v2*2)
print(v1<v2)
print(v1<=v2)
print(v1==v2)
print(v1['z'])
print(v1['a '])

