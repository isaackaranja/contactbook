import pickle
c = ["isaac", "Bona", "kagema", "sammy"]
print(c)
name = input("enter name: ")
for i in c:
    if name == i:
        c.remove(i)
print(c)
