
# انشاء متغيرين s and s1
# ومعرفة نوع هاذين المتغيرين 
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# print(type(s))

# الدالة replace
# وظيفة هذا الدالة الأستبدال 
# الكلمات 
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# s = s.replace("الجافا","البايثون")
# print( s )

# 3 الدوالي upper-lower - title-capitalize
# upper() سيحول كل أحرف المتغير s1 الى أحرف كبيرة
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# s1 = s1.upper()
# print(s1)

# lower
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# s1 = s1.lower()
# print(s1)

# title
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# s1 = s1.title()
# print(s1)

# capitalize
# s = "مرحبا بكم في دورة الجافا"
# s1 = "welcome to this course"
# s1 = s1.capitalize()
# print(s1)

# الدالة isdigit
# ml = input("أدخل المسافة المراد تحويلها(بالميل) >:\n")
# if ml.isdigit():
#     ml = int(ml)
#     km = 1.62 * ml
#     print("المسافة بالكيلومتر تساوي", km)
    
# else:
#     print("لقد أدخلت قيمة غير صحيحة")

#  تحديد كلمات معينة داخل النص 
# هنا سوف يطبع عبارة بكم 
# s = "مرحبا بكم في دورة الجافا"
# print(s[6:9])


#  تحديد كلمات معينة داخل النص 
# هنا سوف يطبع cours
# s1 = "welcome to this course"
# print(s1[-6:-1])

# طباعة آخر كلمة في النص 
# هنا طبع course
# s1 = "welcome to this course"
# print(s1[-6:])

# طباعة أول كلمة في النص وهي 
# كلمة welcome
# s1 = "welcome to this course"
# print(s1[:7])


# طباعة قطعة من النص مع القفز بحرف
# هنا قفز حرفين وكانت النتيجة 
# wloe
# s1 = "welcome to this course"
# print(s1[:7:2])


# قلب النص بالعكس 
# هنا طبع esruoc siht ot
# s1 = "welcome to this course"
# print(s1[:7:-1])


#  الدالةlen()
# طول النص 24
# ترجع لنا طول الكائن الذي نضعه بين قوسيها 
# يمكن ان يكون هذا الكائن سلسلة نصية أو غيرها 
# s = "مرحبا بكم في دورة الجافا"
# print(len(s))


#  الدوالي find- rfind
# بحث عن كلمة البايثون
# وجدها في  index 18
# s = "مرحبا بكم في دورة البايثون"
# search = "البايثون"
# start = s.find(search)
# print(start)

#
#  الدوالي find- rfind
# عبارتنا البايثون موجودة في النص
# تبدء في الموقع 18
# وتنتهي في الموقع 26
# هنا ايضا طبعنا عبارة البحث البايثون
# s = "مرحبا بكم في دورة البايثون"
# search = "البايثون"
# start = s.find(search)
# stop = start+len(search)
# print(start)
# print(stop)
# print(s[start:stop])


# البحث عن الحرف "ب" في النص 
# هنا سوف نبحث  عنه عن طريق الدالة find
# s = "مرحبا بكم في دورة البايثون"
# search1 = "ب"
# start1 = s.find(search1)
# print("ترتيب أول حرف- ب- في الجملة =" , start1)


# البحث عن الحرف "ب" في النص 
# نقوم بالبحث عنه عن طريق الدالة rfind
s = "مرحبا بكم في دورة البايثون"
# search1 = "ب"
# start2 = s.rfind(search1)
# print("ترتيب آخر حرف -ب - في الجملة =" , start2)


# مثال تطبيقي للبحث في النصوص 
# text = "السلام عليكم و رحمة الله و بركاته ، مرحبا بكم في دورة البايثون"
# search2 = input("أدخل عبارة البحث :")
# start3 = text.find(search2)
# if start3 == -1:
#     print("للأسف لم نجد ما تبحث عنه")
# else:
#     stop3 = start3 + len(search2)
#     print(f"تمّالعثور على عبارة البحث بين الموقعين {start3} و{stop3} و يبلغ طول العبارة التي بحثت عنها {len(search2)}")


# أستخدام الفورمات في برنامج المسافة بالميل 
# ml = input("أدخل المسافة المراد تحويلها(بالميل) >:\n")
# if ml.isdigit():
#     ml = int(ml)
#     km = 1.62 * ml
#     print(f"{ml} ميلا = {km:.3f} كلم")
# else:
#     print("لقد أدخلت قيمة غير صحيحة")
