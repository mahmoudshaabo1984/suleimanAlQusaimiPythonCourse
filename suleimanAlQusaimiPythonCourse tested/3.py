


# التعابير المنطقية 
x = 50
y = 100
print(x == y)
print(x < y)
print(y < x)
print(y > x)
print(x + 50 == y)
print(x == y - 50)
print(x > y - 70)
print(x + 50 < y)
print(x + 50 <= y)
print(x + 50 > y)
print(x + 50 >= y)


# التعابير المنطقية  على الأسماء 

name = input("please enter your name:\n")
print(name)
print("ahmed " == "mahmoud")
print("mahmoud "== "mahmoud ")
print("Mahmoud "== "mahmoud ")


text = "السلام عليكم ورحمة الله وبركاته "
print(" " in text)
print("ورحمة الله وبركاته" in text)
print("السلام" in text)



# البرنامج النهائي لحساب المسافة بالميل
# طلب إدخال المسافة من المستخدم
mile = input("أدخل المسافة بالميل\n")
# تحويل القيمة المدخلة إلى رقم صحيح
mile = int(mile)
# حساب المسافة بالكيلومتر
km = mile * 1.62
# طباعة النتيجة النهائية
print(mile , "ميل تساوي " , km, "كيلو متر")
