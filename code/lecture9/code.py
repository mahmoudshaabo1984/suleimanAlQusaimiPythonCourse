# الدوال (Functions) لإعادة الاستخدام الأسهل
def average(l):
    s = sum(l)
    length = len(l)
    return s / length  # إرجاع الناتج المكتمل لخارج الدالة ليستقبل في متغير

numbers = [5, 4, 2, 6, 9, 10, 30, 20, 50]
print("متوسط الأرقام:", average(numbers))

def square(x):
    return x * x
print("مربع العدد 5 هو:", square(5))

# التعامل السليم مع الأخطاء وتجاوزها برمجيا (try...except)
try:
    print(5 / 0)
except ZeroDivisionError:
    print("خطأ منطقي: لا يمكن القسمة على صفر")

# القواميس (Dictionaries) - التكوين بالمفتاح والقيمة
urls = {
    "google": "www.google.com", 
    "youtube": "www.youtube.com", 
}

# طباعة قيمة مفتاح معين بشكل مباشر
print("رابط جوجل هو:", urls["google"])

# إضافة عنصر جديد للقاموس
urls["twitter"] = "www.twitter.com"

# استخراج جميع المفاتيح دون القيم وتحويلها لقائمة لتسهيل التنقل
keys = list(urls.keys())
print("المفاتيح المتوفرة:", keys)

# الحذف والاسترجاع باستخدام دالة الحذف
popped_value = urls.pop("youtube")
print("الرابط الذي تم حذفه هو:", popped_value)
