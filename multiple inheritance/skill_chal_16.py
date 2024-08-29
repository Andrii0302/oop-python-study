from random import choices
from abc import ABC,abstractmethod
import re
class CreditCard:
    DIGITS=list(range(10))
    def __init__(self):
        self._number=self.generate()
    def generate(self):
        return choices(self.DIGITS,k=14)
    @property
    def display(self):
        s="".join(map(str,self._number))
        return ' '.join(re.findall('.{4}',s))
class VisaMixin():
    def generate(self):
        return [4,2] + super().generate()
    
class MasterCardMixin():
    def generate(self):
        return [5,3] + super().generate()
    
class ValidMixin:
    def generate(self):
        num=super().generate()
        return num[:-1] + [self.calculate(num[:-1])]
    @staticmethod
    def calculate(num):
        cul_sum=0
        # for idx, num in enumerate(num[::-1]):
        #     if idx % 2 == 0:
        #         if num * 2 >9:
        #             #summ+=sum(map(int,str(num*2)))
        #             cul_sum+=num*2-9
        #         else:
        #             cul_sum+=num*2
        #     else:
        #         cul_sum+=num
        # return 10 - cul_sum % 10
        toggle=True
        for num in num[::-1]:
            n=num*2 if toggle else num
            toggle=not toggle
            if n>9:
                cul_sum+=n-9
            else:
                cul_sum+=n
        return 10 - cul_sum%10
class Visa(VisaMixin,CreditCard):
    pass
class ValidVisa(ValidMixin,VisaMixin,CreditCard):
    pass
class MasterCard(ValidMixin, MasterCardMixin,CreditCard):
    pass
if __name__ == "__main__":        
    random_visa=Visa()
    print(random_visa.display)
    valid_visa=ValidVisa()  
    print(valid_visa.display)
    master_card=MasterCard()
    print(master_card.display)
