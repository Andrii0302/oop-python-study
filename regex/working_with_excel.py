import openpyxl
import os
import re

workbook = openpyxl.load_workbook(f"{os.getcwd()}\Employees.xlsx")
# print(workbook.sheetnames)
sheet = workbook["EmployeeData"]
# print(sheet.dimensions)
# for row in sheet.values:
#     print(row)
data = []
for row in sheet.values:
    a, b, c, d, e, f, g = row
    data.append("{};{};{};{};{};{};{}".format(a, b, c, d, e, f, g))
employees = "\n".join(data)
# print(employees)
s1 = re.findall(r"\d{1,};.+?;(.+?);.+;2[4-9]\d{3}", employees)
# print(s1)
s2 = re.findall(r"\d{1,};.+?;(\w{1,5});(?:IT|Marketing);.+;\d{5}", employees)
# s2 = [i[0] for i in s2]
# print(s2)
s3 = re.findall(r"\d{1,};([P-Z].+?);.+?;[2468]\d+[13579];.+;\d+", employees)
# print(s3)
s4 = re.findall(r"\d{1,};(.+?);(.+?);Sales;(.+?);.+New York;\d+", employees)
result = [" ".join(i) for i in s4]
# print(result)
s5 = re.findall(r"\d{1,}.+?;(.+?);.+?;.+?;.+, (?!Miami)", employees)
# print(s5)

# Exercises:
# 1
ex1 = re.findall(r"\d{1,};.+?;(.+?);\w{2};.+;[3-5]\d{4}", employees)
# print(ex1)
ex2 = re.findall(r"\d{1,};(.+?);(.+?);.+?;\d+[13579]{2};.+", employees)
# print(ex2)
ex3 = re.findall(r"\d{1,};(.+?);D.+?;IT;.+", employees)
# print(ex3)
ex4 = re.findall(r"\d{1,};.+?;.+?;Logistics;.+?;.+(?:Chicago|LA);(.+)", employees)
print(ex4)
ex5 = re.findall(r"\d{1,};.+?;(.+?);.+?;(.+?);.+, (?!Las Vegas)", employees)
print(ex5)
