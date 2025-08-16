a={"name":"devanand","age":23,"pin":683517,"place":"Kalady","job":"student"}
print(a)
print(type(a))
print(len(a))
print("name" in a)
print("pin" not in a)
print(a["place"])
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
a["place"]="angamaly"
print(a)
a.update({"job":"Datascientist"})
print(a)
a["qualification"]="btech"
print(a)
a.update({"gender":"male"})
print(a)
b=a.copy()
print(b)
c=dict(b)
print(c)
a.pop("job")
print(a)
a.popitem()
print(a)
del a["place"]
print(a)
a.clear()
print(a)
del a
family={"child1":{"name":"devan","age":23},
        "child2":{"name":"ashvin","age":22},
        "child3":{"name":"abhinav","age":25}}
print(family)
print(family["child2"].get("age"))
print(family["child2"]["name"])