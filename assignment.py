'''D = 5
print(D)
print(type(D))
E = 8.5
print(E)
print(type(E))
F = 2+7j
print(F)
print(type(F))
X =float(D)
print(X)
print(type(X))
Y =int(E)
print(Y)
print(type(Y))
Z =complex(D)
print(Z)
print(type(Z))
W =complex(E)
print(W)
print(type(W))

#string
a="  Trust the process"
print(a)
print(len(a))
print(type(a))
print(a[0])
print(a[5:17])
print(a[6:])
print(a[:12])
print(a[-1])
print(a[-7:-1])
print(a[-5:])
print(a[:-1])
for i in a:
    print(i)
print("the" in a)
print("this" not in a)
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("the","this"))
print(a.split(" "))
print(a.count("t"))
w="anytime"
x=a+w
print(x)
#list
x=["red","rose","blue","orange","black","green"]
print(x)
print(type(x))
print(len(x))
print(x[2])
print(x[4:6])
print(x[:5])
print(x[3:])
print(x[-1])
print(x[-6:])
print(x[:-4])
print("orange" in x)
print("apple" not in x )
for i in x:
    print(i)
x.append("yellow")
print(x)
x.insert(2,"brown")
print(x)
y=["lavender","peech","violet"]
x.extend(y)
print(x)
x.sort()
print(x)
y=x.copy()
print(y)
z=list(x)
print(z)
z=x+y
print(z)
y.remove("orange")
print(y)
y.pop(1)
print(y)
y.pop(0)
print(y)
del y[3]
print(y)
y.clear()
print(y)

#tuple
a=("devanand","ashvin","abhinav","adhil","abishek")
print(a)
print(type(a))
print(len(a))
print(a[2])
print(a[1:6])
print(a[3:])
print(a[:6])
print(a[-3])
print(a[-6:-3])
print(a[-5:])
print(a[:-2])
print("dev" in a)
print("abhinav" in a)
print("akshay" not in a)
for i in a:
    print(i)
b=list(a)
print(b)
print(type(b))
b.insert(0,"aadhith")
print(b)
b.sort()
print(b)
b[2]="akshay"
print(b)
b.append("leepaul")
print(b)
a=tuple(b)
print(a)
print(type(a))
c=("arun","syriac","yadhu","alan")
d=a+c
print(d)
d=("sidharth")
e=d*5
print(e)
print(a.count("ashvin"))

#set
a={"aadhith","abhinav","afitha","aadhil","devanand","fayiza","leepaul","ashvin"}
print(a)
print(type(a))
print(len(a))
for i in a:
    print(i)
print("afitha" in a)
print("abishek" in a)
print("afitha" not in a)
print("abhishek" not in a)
a.add("noufiya")
print(a)
b={"syriac","punnya","abhishek","sithara"}
a.update(b)
print(a)
d={"aadhil","ashvin","arshak","devanand","abhinav","ann","arun","aman","abhishek"}
e={"abhishek","punnya","afitha","aadhil","abhinav","sidharth","anoop","arshak","leepaul"}
w=d.union(e)
print(w)
x=d.intersection(e)
print(x)
y=d.difference(e)
print(y)
z=d.symmetric_difference(e)
print(z)
b.remove("sithara")
print(b)
b.discard("ann")
d.pop()
print(d)
d.clear()
print(d)
del d
print(d)

#tuple
a=("ekm","pma","kze","klm","ktm","alpa","iki")
print(a)
print(type(a))
print(len(a))
print(a[2])
print(a[1:6])
print(a[3:])
print(a[:7])
print(a[-2])
print(a[-6:-4])
print(a[-7:])
print(a[:-1])
print("alpa" in a)
print("knr" not in a)
for i in a:
    print(i)
b=list(a)
print(a)
print(type(b))
b.append("knr")
print(b)
b.insert(4,"kskd")
print(b)
c=["tvm","mpr","wnd"]
b.extend(c)
print(b)
b.sort()
print(b)
b.remove("klm")
print(b)
b.remove("ktm")
b.remove("knr")
print(b)
a=tuple(b)
print(a)


#set
s={"kerala","karnata","goa","banglore","mumbai","delhi","maharashtra"}
print(s)
print(type(s))
print(len(s))
print("kerala" in s)
print("goa" not in s)
for i in s:
    print(i)
s.add("telungana")
print(s)
t={"sikkim","punjab","chennai"}
s.update(t)
print(s)
a={"india","australia","england","southafrica","westindies","pakisthan","bangladesh","afganisthan","srilanka"}
b={"namibia","india","america","london","england","srilanka","newyork","ireland","bangladesh","tokyo","australia"}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
s.remove("karnata")
print(s)
s.discard("karnata")
s.pop()
print(s)
s.clear()
print(s)
del s
print(s)

#Dictionary
a={"name":"Abhinav","id":123,"place":"perumbavoor","age":25}
print(a)
print(type(a))
print(len(a))
print("name" in a)
print("age" not in a)
print(a["name"])
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
a["college"]="jbcmet" 
print(a)
a.update({"id":125})
print(a)
b=a.copy()
print(b)
c=dict(b)
print(c)
a.pop("id")
print(a)
a.popitem()
print(a)
del a["age"]
print(a)
a.clear()
print(a)
del a
family={"cousin1":{"name":"jishnu","age":25},
        "cousin2":{"name":"jithin","age":24},
        "cousin3":{"name":"arun","age":23}}
print(family)
print(type(family))
print(family["cousin2"].get("age"))

#condition
a=int(input("enter the year"))
if a%4==0:
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")
a=int(input("enter the number"))
if a%3==0 and a%5==0:
    print("the number is devisible by both 3 and 5")
else:
    print("The number is not devisible by 3 and 5")

#loop
i=0
count=0
a=input("Enter the number")
for i in a:
    count+=1
print(count)
# i=0
# temp=1
# a=input("enter the string")
# n=len(a)
# while i<=n:
#     v=a%10 
#     temp=temp*v 
#     a=a//10 
#     i+=1 
# print(temp)
# x="devanand"
# print(x[::-1])

temp=0
a=int(input("enter the number"))
var=a
while a>0:
    dig=a%10#dig=1,dig=2,dig=1
    temp=temp*10+dig#temp=1,temp=12,temp=121
    a=a//10#a=12,a=1,a=0
if temp==var:
    print("the number is palindrome")
else:
    print("not palindrome")'''

# a=str(input("enter the string"))
# rev=a[::-1]
# if a==rev:
#     print("palindrome")
# else:
#     print("not palindrome")






#pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()


#pyramid
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


#right angled
# n=5
# for i in range(1,n+1):
#     print("  "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# n=5
# for i in range(1,6):
#     for j in range(5,n-i,-1):
#         print(j,end=" ")
#     print()


#Diamond
# for i in range(1,5):
#     print(" "*(5-i)+"* "*i)
# for j in range(3,0,-1):
#     print(" "*(5-j)+"* "*j)



#num pattern
# for i in range(1,4):
#     print("  "*(4-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end="  ")
#     print()
# for k in range(2,0,-1):
#     print("  "*(2-k),end="    ")
#     for b in range(1,k+1):
#         print(b,end="   ")
#     print()



#outer pattern
# for i in range(1,7):
#     print(" "*(7-i)+"* "*i)
# for j in range(7,0,-1):
#     print(" "*(7-j)+"* "*j)

# for i in range(1,3):
#     print(" "*(8-i)+(" *"*i))
# for j in range(2,5):
#     print(" "*(8-j)+("*   "*i))
# print()
# for k in range(1,3):
#     print(" "*(2-k)+("*"))


#square the list
# a=[1,2,3,4,5,6]
# b=list(map(lambda i:i*i,a))
# print(b)
#double the list
# a=[1,2,3,4,5,6]
# b=list(map(lambda i:i+i,a))
# print(b)
#find even in list
# a=[2,3,4,5,6,7,8]
# b=list(filter(lambda i:i%2==0,a))
# print(b) 
#square even in list
# a=[4,5,6,7,8,9,10]
# b=list(filter(lambda i:i%2==0,a))
# c=list(map(lambda j:j*j,b))      
# print(c)
#length of string
# a=["monday","tuesday","thursday","friday","saturday"]
# b=list(map(lambda i:len(i),a))
# print(b)
#double odd in list
# a=[1,2,3,4,5,6,7,8]
# b=list(filter(lambda i:i%2!=0,a))
# c=list(map(lambda j:j+j,b))
# print(c)
#Calculate length of string
# a="devanandbiju"
# b=str(map(lambda i:len(a),a))
# print(b)   
#list negative number
# a=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
# b=list(filter(lambda i:i<0,a))
# print(b)
#Calculate length of string
# a=["Devanandbiju","Ashvinsajan","Abhinavskumar","Adhilcs"]
# b=list(map(lambda i:len(i),a))
# print(b)




import math
#Volume of cylinder
# r=int(input("Enter the radius"))
# h=int(input("enter the height"))
# vol=(math.pi)*(pow(r,2))*h
# print(vol)

#Volume of sphere
# r=int(input("Enter the radius"))
# vol=(4/3)*(math.pi)*(r*r)
# print(vol)

#Volume of hemisphere
# r=int(input("Enter the radius"))
# vol=(2/3)*(math.pi)*(r*r*r)
# print(vol)

#Area of cylinder
# r=int(input("Enter the Radius"))
# h=int(input("Enter the Height"))
# area=(2*(math.pi)*r*h)+(2*(math.pi)*(r*r))
# print(area)

#Area of sphere
# r=int(input("Enter the radius"))
# area=4*(math.pi)*(r*r)
# print(area)

#Area of cone
# r=int(input("Enter the radius"))
# h=int(input("Enter the height"))
# area=((math.pi)*r)*(r+math.sqrt((h*h)+(r*r)))
# print(area)
