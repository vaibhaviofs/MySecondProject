d = {}
d["name"] = "Michel"
d["age"] = 29
print(d)
print(d["name"])
print(d.get("location","key not present"))
a = "age"
d1 = d.copy()
print(d1)
d2 = dict.fromkeys(d)
print(d2)
d2.setdefault("location","kolkata")
print(d2)
print(d2.setdefault("location","chennai"))
d2.pop("age")
print(d2)
print(d2.pop(a,"key not present"+ a))
print(d.values())
print(d.keys())
print(d.items())
d5 = dict([("name","vaibhav"),("occupation", "defense")])
print(d5)
d5.update(d1)
print(d5)
for val in d.items():
    print(val)
