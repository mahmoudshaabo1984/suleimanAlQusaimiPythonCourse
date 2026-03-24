



# لدالة count() ترجع لنا عدد المرات التي ورد فيها ما نضعه بين قوسيها :
# txt = "أهلا بكم في هذه الليلة السعيدة"
# txt = txt.count("ل")
# print(txt)


# x = 5
# y = 6 
# print("{} + {} = {}".format(x,y,x+y))




# القوائم
# test = ["ahmed","أحمد", 1,2,3.5,4.6,True,False]
# print(test)


# القوائم
# members = ["ahmed","ali","khaled","mohammed"]
# print(members)
# print(len(members))
# print(members[3])
# print(members[-1])
# members1 = members[1:]
# print(members1)
# members2 = members[::-1]
# print(members2)
# members.append("messaoud")
# members.insert(0,"soulimen")
# print(members)
# members.insert(3,"soulimen")
# print(members)
# #الطريقة 1 
# members.extend(["alaa","salem","mohsen"])
# print(members)
# members3 = ["leila","maryem","semia"]
# members.extend(members3)
# print(members)
# print(len(members))
# members.remove("soulimen")
# print(members)
# members.pop(2)
# print(members)
# members[0] = "mustapha"
# print(members)
# c = members.count("mustapha")
# print(c)
# members.sort()
# print(members)
grates = [90,87,81,98,96,99]
s = sum(grates)
print(s)
l = len(grates)
print(l)
av = s/l
print(av)
av = round(av,1)
print(av)
print(min(grates))
print(max(grates))
grates1 = grates
print(grates1)
grates1.pop(-1)
print(grates1)
print(grates)
grates2 = grates.copy()
grates3 = list(grates)
print("grates2 = ",grates2)
print("grates3 = ",grates3)
