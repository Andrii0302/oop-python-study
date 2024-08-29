from collections import UserDict
class BiderectionalDict(UserDict):
    def __setitem__(self,key,value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        super().__setitem__(key,value)
        super().__setitem__(value,key)
    def __delitem__(self,key):
        super().__delitem__(self[key])
        super().__delitem__(key)
    def __len__(self):
        return super().__len__() //2
    
bd=BiderectionalDict({'a':'b',"c":'f'})
# print(bd)
# print(len(bd))
# print(bd['a'])
# print(bd['b'])
# del bd['a']
# print(bd)
# del bd['f']
# print(bd)
# bd['i']='g'
# print(bd)
# print(bd.pop('g'))
# bd['f']='t'
# bd['h']='r'
# bd.update([('h','better')])
# print(bd)