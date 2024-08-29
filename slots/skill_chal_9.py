class Point3D:
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        additional=''
        class_name = self.__class__.__name__
        if class_name != 'Point3D':
            attr= self.__class__.__dict__['__slots__'][0]
            attr_val=getattr(self,attr)
            additional=f", {attr}='{attr_val}'"
            
        return f"{class_name}(x={self.x}, y={self.y}, z={self.z}{additional})"

class ColoredPoint(Point3D):
    __slots__ = ('color',)
    
    def __init__(self, *args, color='black',**kwargs):
        super().__init__(*args,**kwargs)
        self.color = color

class ShapedPoint(Point3D):
    __slots__ = ('shape',)
    
    def __init__(self, *args, shape='sphere',**kwargs):
        super().__init__(*args,**kwargs)
        self.shape = shape

c1 = ColoredPoint(1, 2, 3, color='red')
print(c1)  
s1 = ShapedPoint(4, 5, 6, shape='cube')
print(s1)  
