r=("apple","orange","banana","strawberry","blueberry")
print(r)
print(type(r))
print(len(r))
print(r[4])
print(r[1:3])
print(r[-1])
print(r[-3:-1])
print(r[2:])
print(r[:4])
print(r[:-1])
print(r[-5:])
for i in r:
    print(i)
print("banana" in r)
print("rambuttan" not in r)
x=list(r)
print(x)
print(type(x))
x.pop(1)
print(x)
x.insert(1,"mango")
print(x)
x[1]="jackfruit"
print(x)
r=tuple(x)
print(r)
print(type(r))

v=("benz",)
print(v)
print(type(v))
h=r+v
print(h)
t=v*3
print(t)
print(t.count("benz"))


