import re
#findall
a="The Rain In Train in Spain"
# b=re.findall("as",a)
# print(b)

#Search
# c=re.search("\s",a)
# print(c)
# d=re.search("z",a)
# print(d)

#split
# b=re.split("\s",a,2)
# print(b)

#sub
# b=re.sub("\s","<>",a,2)
# print(b)

# x=re.search("^The.*Spain$",a)
# if x:
#     print("It is matching")
# else:
#     print("Not")

b=input("Enter password")
if len(b)>=8 and (re.search("[A-Z]",b)) and (re.search("[a-z]",b)) and (re.search("\d",b)) and (re.search("[@#$%^&*_.]",b)):
    print("strong")
else:
    print("weak")