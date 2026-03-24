


# برنامج المتوصط الحسابي 
numbers = []
for i in range(5):
    number = input("اكتب رقمًا: \n")
    number = int(number)
    numbers.append(number)

av = sum(numbers)/len(numbers)
print(av)

