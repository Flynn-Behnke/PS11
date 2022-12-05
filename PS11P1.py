#1
def listlength(mylist):
  n = int(input("Enter number of items in list: "))
  for n in range(0,n,1):
    s = int(input("Enter an integer: "))
    mylist.append(s)
  return mylist

mylist = []
mylist = listlength(mylist)
print(mylist)

#2
mylist[1] = 99
print()
print(mylist)

#3
mylist[1] = 100
print()
print(mylist)

#4
mylist2 = [500, 600, 700, 800, 900]
print()
print(mylist2)
mylist.extend(mylist2)
print(mylist)

#5
mylist.remove(800)
print()
print(mylist)

#6
mylist.pop(2)
print()
print(mylist)

#7
grades = ["A", "B", "C", "A", "A", "C"]

#8
print()
print(grades.count("A"))

#9
print()
print(grades.index("B"))

#10
print()
print("There are", str(grades.count("F")), "F's in grades")

#11
print()
print(mylist2)
mylist2.clear()
print(mylist2)

#12
print()
del mylist2


#13
players1 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#14
players1.sort()
print()
print(players1)

#15
players2 = players1.copy()
print()
print(players2)

#16
players2.reverse()
print()
print(players2)
