import re
f = open('bookshelf.txt')
string=f.read()
f.close()
result_1=re.findall(r".+?;(.{1,25});.+?",string) # to find all the books with the name from 1 to 25 characters
#print(result_1)
result_2=re.findall(r"(.+?);.+?;20[0-9][0-9]",string) # to find all the books with the year of publishing 2000-2099
#print(result_2)
result_3=re.findall(r".+?;(.+p);.+?",string,re.I)
#print(result_3)
result_4=re.findall(r".+? (B.+?);.+;.+",string)
#print(result_4)
result_5=re.findall(r'.+?;(.+?);19[8-9][0-9]',string)
print(result_5)
