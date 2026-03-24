# التعامل مع العشوائية واختيار القيم
import random
from random import choice

# توليد رقم عشوائي صحيح بين 1 و10 لمعرفة الفائز
secret_number = random.randint(1, 10)

# اختيار حرف أو رمز عشوائي لبناء كلمات السر
choices = "abcdefghijklmnopqrstuvwxyz0123456789!@#$"
random_char = choice(choices)

# تشغيل الأصوات في ويندوز (يتطلب وجود ملفات صوتية في المسار المحدد)
import winsound
# winsound.PlaySound("sounds/correct.wav", 1) # تشغيل الصوت في الخلفية وعدم إيقاف الكود

# مقدمة في الدوال: تعريف دالة مجردة تحسب طول القائمة وتعمل مثل الدالة المدمجة المعتادة len()
def custom_length(o):
    count = 0        # تهيئة العداد الداخلي للدالة
    for i in o:
        count += 1   # زيادة العداد لكل عنصر يمر في الحلقة
    return count     # إرجاع طول الدالة بعد الحساب النهائي

# استدعاء الدالة المخصصة وتمرير المتغيرات لها وطباعة النتيجة
my_list = [1, 3, 5, 6]
print("طول القائمة هو:", custom_length(my_list))
