







import webbrowser  # مكتبة لفتح المتصفح
# قاموس لتخزين الروابط
urls = {}
print("مرحباً بك في مخزن الروابط")
while True:
    option = input("1 لفتح رابط، 2 لإضافة رابط جديد: ")

    if option == "1":
        # عرض الروابط المتوفرة
        keys = list(urls.keys())
        if keys == []:
            print("لا توجد عناصر مضافة!")
        else:
            print("الروابط المتوفرة:", keys)
            
            name = input("اكتب اسم الموقع لفتحه: ")
            
            # حماية البرنامج: ماذا لو أدخل المستخدم اسماً غير موجود؟
            try:
                # محاولة جلب الرابط باستخدام الاسم (المفتاح)
                link = urls[name]
            except KeyError:
                # KeyError هو الخطأ الذي يحدث عند طلب مفتاح غير موجود في القاموس
                print("عذراً، هذا الموقع غير موجود!")
                continue  # عد للبداية
            
            # إذا وجدنا الرابط، نفتحه
            webbrowser.open(link)

    elif option == "2":
        key = input("اسم الموقع: ")
        link = input("الرابط: ")
        # إضافة الرابط للقاموس
        urls[key] = link
