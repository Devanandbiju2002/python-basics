'''#sample
print("helloworld")
print(4)
x=3
print(x)
print(type(x))
y="Devanand Biju"
print(y)
print(type(y))
a,b,c="orange","apple","mango"
print(a)
print(b)
print(c)
a=b=c="apple"
print(a)
print(b)
print(c)

#numeric
a=5
print(a)
print(type(a))
b=3.9
print(b)
print(type(b))
c=2+3j
print(c)
print(type(c))

#a->b
x=float(a)
print(x)
print(type(x))
#b->c
y=complex(b)
print(y)
print(type(y))
z=int(b)
print(z)
print(type(z))

#text.py
a="python is a progamming language"
print(a)
print(type(a))
print(len(a))
print(a[5])
print(a[0:31])
print(a[-1])
print(a[-9:-1])
print("a" in a)
print("am" not in a)


#string
g="python is the most popular programming language"
print(g)
print(type(g))
print(len(g))
print(g[31])
print(g[20:31])
print(g[27:])
print(g[:20])
print(g[-1])
print(g[-9:])
print(g[-20:-31])
for i in g:
    print(i)
print("lan" in g)
print("guage" not in g)
print(g.upper())
print(g.strip())
print(g)
print(g.replace("the","a"))
print(g)
print(g.split(" "))
print(g)
print(g.count("a"))
h="it is easy to use

a="My Name Is Devanand"
print(a)
print(type(a))
print(len(a))
print(a.upper())
print(a.strip())
print(a.split(" "))
print(a.replace("Is","is also called"))
print(a.count("N"))
b=" and i am from kerala"
c=a+b
print(c)'''


'''R=["cat","dog","horse","giraffe","elephant","snake"]
R.append("monkey")
print(R)
R.insert(3,"cheetah")
print(R)
S=["fox","buffallo","lion"]
R.extend(S)
print(R)
x=R.copy()
print(x)

#sample
s="devanand"
print(s)
print(len(s))
print(type(s))
a,b,c="apple","orange","banana"
print(a)
print(b)
print(c)

a=[2,4,6,8,10,12]
a.sort()
print(a)
print(a[0])
n=len(a)
print(a[n-1])

#Dictionary
a={""}'''

#even number in a range

# a=int(input("enter the range"))
# for i in range(0,a+1,2):
#     print(i)



#sum of first n numbers
# sum=0
# n=int(input("enter the number"))
# for i in range(0,n+1,1):
#     sum=sum+i
# print(sum)



#sum of odd number in a range
# sum=0
# a=int(input("enter the number"))
# for i in range(1,a+1,2):
#     sum=sum+i
# print(sum)



#factorial
# fact=1
# a=int(input("enter the number"))
# for i in range(1,a,1):
#     fact=fact*i
# print(fact)



# #prime
# a=int(input("enter the number"))
# for i in range(2,a):
#     if a%i==0:
#         print("Not prime")
#         break
# else:
#     print("prime")




#fibonassi seq
# n=int(input("enter the number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     temp=a
#     a=b
#     b=temp+a

# for i in range(5,0,-1):
#     print("*"*i)


# for i in range(5,0,-1):
#     print((5-i)*" +" * "*i)

#pattern
# for i in range(1,6):
#     print('*'*i)

#multiplication
# a=int(input("enter the number"))
# for i in range(1,11,1):
#     print(i*a)


#smallest
# a=[1,2,3,4,5,6]
# for i in range(a):
#     if a[i] < a[i+1]:
#         print(a[i])



# def sample():
#     print("Devanand Biju")
# sample()

# def adder():
#     print(a+b)
# a=int(input("Enter the 1st number"))
# b=int(input("Enter the 2nd number"))
# adder()

# def adds(a,b):
#     print(a+b)
# adds(1,2)


# def eve():
#     for i in range(a,b+1,1):
#         if i%2==0:
#             print(i)
# a=int(input("Enter the starting number"))
# b=int(input("Enter the last number"))
# eve()


# a="   python is a programming language    "
# print(a)
# print(type(a))
# print(len(a))
# print(a[25])
# print(a[31])
# print(a[1:5])
# print(a[-8:0])
# for i in a:
#     print(i)
# print("is" in a)
# print("and" in a) 
# print("is" not in a)
# print("and" not in a)

# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("python","Java"))
# print(a.split(" "))
# print(a.count("a"))
# b="\tand it is easy to understand"
# c=a+b
# print(c)

# a="  python is a programming language  "
# print(a)
# print(type(a))
# print(len(a))
# print(a[25])
# print(a[0])
# print(a[31])
# print(a[1:5])
# print(a[3:9])
# print(a[-7:-1])
# print(a[-10:-1])
# for i in a:
#     print(i)
# print("is" in a)
# print("ah" in a)
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.split(" "))
# print(a.replace("python","java"))
# print(a.count("a"))
# a=["mango","grape","orange","apple","banana","blueberry"]
# print(a)
# print(type(a))
# print(type(a))
# print(len(a))
# print(a[3])
# print(a[5])
# print(a[0:4])
# a.append("strawberry")
# print(a)
# a.append("kiwi")
# print(a)
# a.insert(1,"pineapple")
# print(a)
# b=["malberry","greenapple","sappotta"]
# a.extend(b)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# c=a.copy()
# print(c)
# d=list(a)
# print(d)
# e=["cat","dog","ant"]
# f=["horse","elephant","zebra"]
# g=e+f
# print(g)
# print(a)
# a.remove("strawberry")
# print(a)
# a.pop(3)
# print(a)
# del a[3]
# print(a)
# a.clear()
# print(a)
# a=("apple","orange","yellow","blue","grape")
# print(a)
# print(type(a))
# print(len(a))

# a=("apple","orange","mango","banana","kiwi","tender")
# print(a)
# print(type(a))
# print(len(a))
# print(a[3])
# print(a[1:5])
# for i in a:
#     print(i)
# print("mango" in a)
# print("sappotta" in a)
# x=list(a)
# print(x)
# x.append("strawberry")
# print(x)
# x.insert(1,"blueberry")
# print(x)
# y=["pineapple","carrot"]
# x.extend(y)
# print(x)
# x.sort()
# print(x)
# b=x.copy()
# print(b)
# c=list(x)
# print(c)
# x.remove("apple")
# print(x)
# x.pop(8)
# print(x)
# x.remove("strawberry")
# print(x)
# x.insert(0,"apple")
# print(x)
# x.insert(4,"dryfruit")
# print(x)
# x.remove("banana")
# print(x)
# del x[4]
# print(x)
# a=tuple(x)
# print(a)

r={"black","white","red","mango","carrot","vancho"}
# print(a)
# print(type(a))
# print(len(a))
# print("mango" in a)
# for i in a:
#     print(i)

# a.add("choctruf")
# print(a)
# b={"snickers","spanishdelight","irishcoffe"}
# a.update(b)
# print(a)

a={"google","microsoft","apple","deloitte","hcl","tcs","claysis","codex","talrop","unique"}
b={"deloitte","amazon","flipkart","ey","infosys","apple","talrop","spacex","tcs","pinterest","meesho"}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
d=a.symmetric_difference(b)
print(d)
r.remove("black")
print(r)
r.discard("black")
r.pop()
print(r)
