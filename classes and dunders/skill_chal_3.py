class Contact():
    def __init__(self,name,lastname,phone=None,email=None,display_mode='masked'):
        self.name=name
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.display_mode=display_mode

    def __eq__(self,other):
        if not isinstance(other,Contact):
            return False
        if (self.phone is not None and self.phone == other.phone) or (self.email is not None and self.email == other.email):
            return True
        return (self.name==other.name and self.lastname==other.lastname) 
    def __hash__(self):
        return hash((self.name,self.lastname,self.phone,self.email))
    
    def __repr__(self):
        if self.display_mode == 'masked':
            return f"Contanct('{self._obfuscated(self.name)}', '{self._obfuscated(self.lastname)}')"
        return f"Contanct('{self.name}', '{self.lastname}', '{self.phone}', '{self.email}')"
    def __str__(self):
        return f'{self.lastname[0]}{self.name[0]}'
    def __format__(self, format_spec):
        if format_spec != 'masked':
            return f"Contanct('{self.name}', '{self.lastname}', '{self.phone}', '{self.email}')"
        return repr(self)
        
    @staticmethod
    def _obfuscated(text):
        half=len(text)//2
        return text[:half] + '*' * (half+1)