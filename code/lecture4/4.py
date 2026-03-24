

# hالجمل الشرطية if
# name = "محمود"
# userName = input("أدخل اسم المستخدم:")
# if name == userName:
#     print("تم تسجيل الدخول")
#     print("مرحبا فيك في البرنامج")


# Conditional statements if
# name = "mahmoud"
# userName = input("Enter username: ")
# if name == userName:
#     print("Login successful")
#     print("Welcome to the program")
#     print(" the program has been end")


# else:
#     print("The username is not correct")


# برنامج لحساب درجات الطلاب
# grade = input("أدخل قيمة الدرجة")
# grade = int(grade)

# if grade >= 90 and grade <= 100:
#     print("a")
# elif grade >= 80 and grade < 90:
#     print("b")
# elif grade >= 70 and grade < 80:
#     print("c")
# else:
#     print("لقد أدخلت قيمة غير صحيحة")



# وضع شرط داخل else
# طلب إدخال قيمة الدرجة من المستخدم
grade = input("ادخل قيمة الدرجة: ")

# تحويل القيمة المدخلة إلى عدد صحيح
grade = int(grade)

# التحقق من قيمة الدرجة وطباعة النتيجة المناسبة
if grade >= 90 and grade <= 100:
    print("a")
elif grade >= 80 and grade < 90:
    print("b")
elif grade >= 70 and grade < 80:
    print("c")
else:
    if grade > 100:
        print("لقد تجاوزت الحد المسموح به لقيمة الدرجة")
    else:
        print("حالة الطالب راسب")        
