



# الدالة count لعد العناصر
text = "أهلا بكم في هذه الليلة السعيدة"
print(text.count("ل"))


# Using format function for arithmetic operations
x = 6
y = 5
print("{} + {} = {}".format(x, y, x + y))



# القوائم 
# new  list 
members = ["ahmed", "ali", "khalid", "mohammed"]
print(type(members ))
# معرفة طول القائمة 
print(len(members ))

# الوصول الى index الثالث
print(members[3])
# الوصول الى االعنصر الأخير
print(members[-1])

# انشاء قائمة تبدأ من العنصر الأول 
members2 = members[1:]
print(members2)


# عكس القائمة 
print(members [::-1])



# اضافة عنصر الى آخر القائمة  عن طريق الدالة  append()
members.append("masood")
print(members)


# اضافة index معين عن طريق الدالة insert
# هذه الدالة تقوم بتحديد الموقع الذي نريد اضافته 
members.insert(0, "sulaiman")
print(members)



# اضافة index معين عن طريق الدالة insert هنا اضفنا sulaiman مرتين الدالة تقبل 
members.insert(2, "sulaiman")
print(members)

# اضافة index معين عن طريق الدالة insert هنا طبعنا طول القائمة المحدث
print(len(members))
print(members)

# حذف عنصر من القائمة عن طريق القيمة  عن طريق الدالة remove()
members.remove("sulaiman")
print(members)



# حذف عنصر من القائمة عن طريق الترتيب  عن طريق الدالة pop()
members.insert(0, "sulaiman")
members.pop(2)
print(members )


# تعديل index الأول في القائمة عن طريقة هذه الأقواس []
members[0] = "mostafa"
print(members )



# معرفة عدد خالد وأحمد 
members.append("ahmed")
print(members.count("khalid"))
print(members.count("ahmed"))



# ترتيب القائمة عن طريق الدالة sort()
members.sort()
print(members)




# انشاء قائمة تحتوي على أرقام 
# هنا استخدمنا الدالة sum() لمعرفة مجموع الأرقام الموجودة في هذه القائمة 
grades = [90, 87, 81, 98, 96, 99]
s = sum(grades)
print(s)

# معرفة المتوصط الحسابي 
# بتقسيم مجموع الأرقام عىل عددها 
grades = [90, 87, 81, 98, 96, 99]
s = sum(grades)
av = s/len(grades)
print(av )





# تعديل على القائمة من خلال متغير ثاني 
grades1 = grades
print(grades1 )

# تعديل على القائمة من خلال متغير ثاني   هنا حذفنا آخر عنصر من grades1
# ملاحظة في القوائم اذا حذفنا في المتغير الأول  # يتم الحذف والتعديل أيضا في المتغير الثاني
grades1.pop(-1)
print(grades1 )
print(grades)


# الحلقات التكرارية loop  using for
x = [1 , 2 , 3 , 4, 5]
for i in x:
    print(i * i)

# الحلقات التكرارية loop# هنا وضعنا شرطا في الحلقة for لكي نتأكد اذا كان  # هذا الرقم زوجي أو فردي 
x = [1, 2, 3, 4, 5]
for i in x:
    if i % 2 == 0:
        print(f"الرقم {i} هو عدد زوجي")
    else:
        print(f"الرقم {i} هو عدد فردي")

        


# الحلقات التكرارية loop هنا لدينا قائمة مكونة من عدد من الأسماء
# هنا نريد ان نرقم الأسماء الموجودة في القائمة  # بأستخدام الحلقة التكرارية for 
members = ['ahmed', 'ahmed', 'ali', 'khalid', 'masood', 'mohammed', 'mostafa']
for i in range(len(members )):
    print(f"{i + 1} . {members [i]}")



# البرنامج النهائي انشاء برنامج يحسب المتوصط الحسابي
# بحيث يأخذ رقمين من المستخدم
numbers = []
for i in range(5):
    number = input("اكتب رقما \n")
    number = int(number)
    numbers.append(number)

av = sum(numbers) / len(numbers)
print(av)




