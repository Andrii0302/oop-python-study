class DNABase:
    def __init__(self,nucleotide):
        self.base=nucleotide
    @staticmethod
    def _validate_and_standardize(base):
        allowed=[('a','adenine'),('c','cytosine'),('t','thymine'),('g','guanine')]
        for b in allowed:
            if base.lower().strip() in b:
                return b[1]
        return False
    def __repr__(self):
        return f"{type(self).__name__}({self.base})"
    def get_nucleotide(self):
        return self._base
    def set_nucleotide(self,base):
        nucleotide=self._validate_and_standardize(base)
        if nucleotide:
            self._base=nucleotide
        else:
            raise ValueError("Invalid Nucleotide")
        
    base=property(fget=get_nucleotide,fset=set_nucleotide)
c=DNABase('a')
print(c)
print(c.base)
# G=DNABase('tHEO')
