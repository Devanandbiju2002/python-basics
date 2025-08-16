s={"rose","jasmine","sunflower","dalia"}
print(s)
print(type(s))
print(len(s))
print("rose" in s)
print("lavender" in s)
for i in s:
    print(i)
s.add("lilly")
print(s)
t={"yello","green","orange","red"}
s.update(t)
print(s)
a={"cse","civil","aero","ece","nautical","marine"}
b={"aero","eee","marine","bsc","bcom","ece"}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
s.remove("dalia")
print(s)
s.discard("blue")
print(s)
s.pop()
print(s)
s.clear()
print(s)
del s