

# new  list 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# print(type(members ))

# معرفة طول القائمة 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# print(len(members ))

# الوصول الى index الثالث
# members = ["ahmed", "ali", "khalid", "mohammed"]
# print(members [3])

# الوصول الى االعنصر الأخير
# members = ["ahmed", "ali", "khalid", "mohammed"]
# print(members [-1])

# انشاء قائمة تبدأ من العنصر الأول 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members2 = members[1:]
# print(members2 )


# عكس القائمة 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# print(members [::-1])

# اضافة عنصر الى آخر القائمة 
# عن طريق الدالة  append()
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members .append("masood")
# print(members )


# اضافة index معين عن طريق الدالة insert
# هذه الدالة تقوم بتحديد الموقع الذي نريد اضافته 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members.insert(0, "sulaiman")
# print(members )

# اضافة index معين عن طريق الدالة insert
# هنا اضفنا sulaiman مرتين الدالة تقبل 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# print(members )


# اضافة index معين عن طريق الدالة insert
# هنا طبعنا طول القائمة المحدث 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# print(len(members))
# print(members )


# حذف عنصر من القائمة عن طريق القيمة 
# عن طريق الدالة remove()
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# members.remove("sulaiman")
# print(members )




# حذف عنصر من القائمة عن طريق الترتيب 
# عن طريق الدالة pop()
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# members .append("masood")
# members.pop(2)
# print(members )


# تعديل index الأول في القائمة 
# عن طريقة هذه الأقواس []
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members .append("masood")
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# members[0] = "mostafa"
# print(members )


# معرفة عدد خالد وأحمد 
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members .append("ahmed")
# members .append("masood")
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# print(members.count("khalid"))
# print(members.count("ahmed"))


# ترتيب القائمة عن طريق الدالة sort()
# members = ["ahmed", "ali", "khalid", "mohammed"]
# members .append("ahmed")
# members .append("masood")
# members.insert(0, "sulaiman")
# members.insert(2, "sulaiman")
# members.sort()
# print(members)



# انشاء قائمة تحتوي على أرقام 
# grades = [90, 87, 81, 98, 96, 99]
# s = sum(grades)
# print(s)


# معرفة المتوصط الحسابي 
# grades = [90, 87, 81, 98, 96, 99]
# s = sum(grades)
# av = s/len(grades)
# print(av )


# تعديل على القائمة من خلال متغير ثاني 
# grades = [90, 87, 81, 98, 96, 99]
# grades1 = grades
# print(grades1 )

# تعديل على القائمة من خلال متغير ثاني 
# هنا حذفنا آخر عنصر من grades1
# ملاحظة في القوائم اذا حذفنا في المتغير الأول
# يتم الحذف والتعديل أيضا في المتغير الثاني 
# grades = [90, 87, 81, 98, 96, 99]
# grades1 = grades
# grades1.pop(-1)
# print(grades1 )
# print(grades )



# الحلقات التكرارية loop
# using for 
# x = [1, 2, 3, 4, 5]
# for i in x:
#     print(i* i)


# الحلقات التكرارية loop
# هنا وضعنا شرطا في الحلقة for لكي نتأكد اذا كان 
# هذا الرقم زوجي أو فردي 
# x = [1, 2, 3, 4, 5]
# for i in x:
#     if i % 2 == 0:
#         print(f"الرقم {i} هو عدد زوجي")
#     else:
#         print(f"الرقم {i} هو عدد فردي")





# الحلقات التكرارية loop
#هنا لدينا قائمة مكونة من عدد من الأسماء 
# هنا نريد ان نرقم الأسماء الموجودة في القائمة 
# بأستخدام الحلقة التكرارية for 
# members = ['ahmed', 'ahmed', 'ali', 'khalid', 'masood', 'mohammed', 'mostafa']
# for i in range(len(members)):
#     print(f"{i+1}. {members[i]}")


# انشاء برنامج يحسب المتوصط الحسابي 
# بحيث يأخذ رقمين من المستخدم
# numbers = []
# for i in range(5):
#     number = input("اكتب رقمًا: \n")
#     number = int(number)
#     numbers.append(number)

# av = sum(numbers)/len(numbers)
# print(av)
