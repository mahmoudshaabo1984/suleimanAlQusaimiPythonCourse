


# # الجمل الشرطية if
# name = "mahmoud"
# user_name = input("ادخل إسم المستخدم: \n")
# if name == user_name:
#     print("تم تسجيل الدخول")
#     print("مرحبا بك في البرنامج")




# Conditional statements if
name = "mahmoud"
user_name = input("Please Enter your name:\n")
if name == user_name:
    print("Login successful")
    print("Welcome to the program")
    print("the program has been end")

else:
    print("The username is not correct")



# البرنامج النهائي: حساب تقدير درجات الطلاب بناء على القيمة المدخلة
# طلب إدخال قيمة الدرجة من المستخدم
grade = input("ادخل قيمة الدرجة :\n")
# تحويل القيمة المدخلة إلى عدد صحيح
grade = int(grade)
# التحقق من قيمة الدرجة وطباعة النتيجة المناسبة باستخدام الشروط المتعددة والمتداخلة
if grade >= 90 and grade <= 100:
    print("التقدير A")
elif grade >= 80 and grade<= 90:
    print("التقدير  B")
elif grade >= 70 and grade <= 80:
    print("التقدير C")
else:
    # شروط متداخلة (Nested If) للتحقق من الأخطاء والرسوب
    if grade > 100:
        print("خطأ: لقد تجاوزت الحد المسموح به لقيمة الدرجة (100)")
    else:
        print("التقدير: راسب")

    
    


