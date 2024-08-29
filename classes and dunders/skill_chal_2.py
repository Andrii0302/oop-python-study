from random import choices
from string import ascii_letters,punctuation
from copy import copy
class Password():
    """ A class that generates new instances of Password"""
    INPUT_UNIVERSE = {'numbers':list(range(10)),'letters':list(ascii_letters),'punctuation':list(punctuation)}
    DEFAULT_LEN = {'low':8,'mid':12,'high':16}
    @classmethod
    def show_input(cls):
        return cls.INPUT_UNIVERSE
    
    def __init__(self,strength='mid',length=None):
        self.strength=strength
        self.length=length
        self._generate()
    def _generate(self):
        pop = copy(self.INPUT_UNIVERSE['letters'])
        length=self.length or self.DEFAULT_LEN.get(self.strength)
        if self.strength == 'high':
            pop += self.INPUT_UNIVERSE['numbers'] + self.INPUT_UNIVERSE['punctuation']
        else:
            pop += self.INPUT_UNIVERSE['numbers']
        self.password = ''.join(list(map(str, choices(pop,k=length))))

if __name__ == '__main__':
    p=Password()
    print(p.password)