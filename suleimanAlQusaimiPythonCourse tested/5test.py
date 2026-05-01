# -----------------------------------------------
# File: string_methods_practice.py
# Purpose: تعلم دوال النصوص في بايثون بطريقة نظيفة ومرتبة
# -----------------------------------------------

def demo_replace():
    print("\n--- دالة الاستبدال replace ---")
    s = "مرحبا"
    result = s.replace("ا", "ن")
    print(f"النص الأصلي: {s}")
    print(f"بعد الاستبدال: {result}")


def demo_case_methods():
    print("\n--- دوال حالة الأحرف (للغة الإنجليزية) ---")
    s = "welcome to this course"
    print(f"تكبير الكل upper(): {s.upper()}")
    print(f"تصغير الكل lower(): {s.lower()}")
    print(f"تكبير أول حرف فقط capitalize(): {s.capitalize()}")
    print(f"تكبير أول حرف من كل كلمة title(): {s.title()}")


def demo_isdigit():
    print("\n--- التحقق من الأرقام isdigit ---")
    s1 = "12345"
    s2 = "welcome"
    print(f"هل '{s1}' يتكون من أرقام فقط؟ {s1.isdigit()}")
    print(f"هل '{s2}' يتكون من أرقام فقط؟ {s2.isdigit()}")


def demo_indexing():
    print("\n--- الفهارس والتقطيع Indexing & Slicing ---")
    s = "السلام عليكم ورحمة الله وبركاته"
    
    # استخدام f-string هنا يجعل المخرجات واضحة جداً لتفهم ماذا يفعل كل كود
    print(f"النص: '{s}'")
    print(f"s[0]      (الحرف الأول)           : {s[0]}")
    print(f"s[7]      (الحرف رقم 7)           : {s[7]}")
    print(f"s[7:12]   (من 7 إلى 11)           : {s[7:12]}")
    print(f"s[-1]     (الحرف الأخير)          : {s[-1]}")
    print(f"s[-7:]    (آخر 7 أحرف للنهاية)    : {s[-7:]}")
    print(f"s[7:]     (من 7 للنهاية)          : {s[7:]}")
    print(f"s[0:7:2]  (من 0 لـ 6 بخطوتين)     : {s[0:7:2]}")
    print(f"s[::-1]   (عكس النص بالكامل)      : {s[::-  1]}")


def demo_len():
    print("\n--- معرفة طول النص len ---")
    s = "mahmoud"
    print(f"عدد أحرف كلمة '{s}' هو: {len(s)}")


def demo_find():
    print("\n--- البحث عن نص find ---")
    txt = "السلام عليكم ورحمة الله وبركاته مرحبا بكم في دورة البايثون"
    search = "مرحبا" # بدلاً من input لتسريع التجربة
    start = txt.find(search)

    if start == -1:
        print(f"لم يتم العثور على الكلمة: '{search}'")
    else:
        stop = start + len(search)
        print(f"تم العثور على '{search}' من المؤشر {start} إلى {stop}")


# -----------------------------------------------
# قسم التشغيل (قم بإزالة علامة # لتشغيل الدالة التي تريد تجربتها)
# -----------------------------------------------

# demo_replace()
# demo_case_methods()
# demo_isdigit()
# demo_indexing()  # قمنا بتشغيل هذه الدالة فقط كمثال
# demo_len()
demo_find()