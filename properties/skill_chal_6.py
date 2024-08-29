class Tablet:
    levels={'lite':{'base_storage':32,'memory':2},'pro':{'base_storage':64,'memory':3},'max':{'base_storage':128,'memory':4}}
    def __init__(self,model):
        model=model.lower().strip()
        if model not in self.levels.keys():
            raise ValueError("Invalid Model")
        specs=self.levels[model]
        self.model=model
        self._base_storage=specs['base_storage']
        self._memory=specs=specs['memory']
        self._added_storage=0

    def add_storage(self,additional):
        if self._base_storage+additional > 1024:
            raise ValueError("Storage limit exceeded")
        self._added_storage+=additional
    @property
    def storage(self):
        return self._added_storage + self._base_storage
    @storage.setter
    def storage(self,memory):
        additional=memory-self._base_storage
        if additional <0:
            raise ValueError("Storage limit exceeded")
        if memory > 1024:
            raise ValueError('Storage limit exceeded')
        self._added_storage=additional
    @property
    def memory(self):
        return self._memory
    @property
    def base_storage(self):
        return self._base_storage

    def __repr__(self):
        return f"Tablet(model='{self.model}', base_storage='{self.base_storage}', added_storage='{self._added_storage}', memory='{self.memory}')"
c=Tablet('lite')
print(c)
c.add_storage(128)
print(c)
c.storage=400
print(c)
