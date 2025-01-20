# Answer the question

# 1. 1.	Pythonda o'zgaruvchilar qanday aniqlanadi?

# x = 47
# if isinstance(x, int):
#     print(f"{x} => butun son")

width = 25
height = 35

area = height * width
# print("Maydon: ", area)

# Global o'zgaruvchi
counter = 0

def increment():
    global counter # agar global so'zini ishlatmasak bu local o'zgaruvchi
    counter += 1
    print("counter", counter)

# increment()
# increment()

# Ko'p o'zgaruvchini bir qatorda belgilash
x, y, z = 1, 5, "Hello"
# print(x, y, z)
# print(z, x, y)

# bir xil qiymatga ega o'zgaruvchilarni belgilash
a = b = c = 100
# print(a, b, c)

# 2.Python o'zgaruvchilari uchun ma'lumot turini belgilash zarurmi?

n = 42
# n = "python"
# n = ["js", "py"]

def add_numbers(a: int, b: int) -> int:
    return a + b
res = add_numbers(7, 3)
# res_2 = add_numbers("5", 5) # type_error
# print(res)
# print(res_2) # result: type_error

# user_input = input("Ixtiyoriy son kiriting: ")
# if user_input.isdigit():
#     number = int(user_input)
#     print("Kvadrat: ", number ** 2)
# else:
#     print("Iltimos, faqat raqam kiriting!")

# import keyword
# print(keyword.kwlist)

# snake_case nom berish usuli:
total_score = 100
# CamelCase nom berish usuli
FullName = "Yoqubov Sherzod"

PI = 3.14159
USER_PASSWORD='123456'

# O'zgaruvchilarning maqsadini belgilash uchun prefikslar ishlatilishi mumkin:
is_valid = True  # Boolean qiymat
num_students = 25  # Raqam
str_message = "Salom"  # String
"""
    Xulosa:
    O'zgaruvchilar nomi:
    
    1. Ma'noli va o'qilishi oson bo'lishi kerak.
    2. Python qoidalariga mos bo'lishi zarur.
    3. Snake_case uslubida yozish Python dasturlash hamjamiyatida eng yaxshi amaliyot hisoblanadi.
"""
# 5.	global kalit so'zining vazifasi nima?
settings = {"DEBUG": True, "VERSION": "1.0.0"}

def update_settings():
    global settings
    settings["DEBUG"] = False

update_settings()
# print(settings)  # {'DEBUG': False, 'VERSION': '1.0.0'}

# 6.	Python'da konstantalar (o'zgarmas qiymatlar) qanday belgilanishi kerak?

# Konstanta - qiymati dastur tomonidan o'zgarmasligi kerak bo'lgan o'zgaruvchi
# exp: konfiguratsion ma'lumotlar: ( PORT, USER_PASSWORD )

# 7.	del operatori o'zgaruvchini qanday ishlaydi?

# xotirani optimallashtirishda del operatori garbage collector bilan birgalikda ishlaydi,
# biror ma'lumot bir marta foydalanib keyin kerak bo'lmasa del operatori ishlatilsa
# garbage collector xotirani boshatadi, agar biror o'zgaruvchini del bilan o'chirdingiz,
# lekin shu o'zgaruvchiga boshqa bir o'zgaruvchi tomonidan
# havola qolgan bo'lsa Garbage Collector ma'lumotni xotiradan o'chirmaydi.

l = 10.0
del l

list = [1, 2, 3, 4]
del list[1:3]
# print(list)

dict = {'a':1, 'b': 2}
del dict['a']
# print(dict)

# 8.	Python'da o'zgaruvchining qiymatini boshqa o'zgaruvchiga qanday ko'chirish mumkin?

ab = 11
bc = ab
# print(ab)
# print(bc)

# Immutable turlar: int, float, str, tuple
# Immutable turlarda qiymatlar nusxa ko'chiriladi
ab = 11
bc = ab
# print(ab)
# print(bc)

f = 17
p = f
f = 98
# print(f)
# print(p)

# Mutable turlar: list, dict, set
# Mutable turlarda havola nusxa ko'chiriladi

list1 = [1, 2, 3]
list2 = list1

list1.append(4)
# print(list1)
# print(list2)

import copy
list3 = [1,2,3]
list4 = copy.copy(list1) # (shallow copy)
list3.append(4)
#
# print(list3)
# print(list4)

list5 = list3[:] # slicing orqali nusxa olish

dict3 = {"a": 1, "b": 2}
dict4 = dict3.copy()
dict3['c'] = 3

# print(dict3)
# print(dict4)

nested_list = [[5,6], ['.py', '.js']]
nested_copy = copy.deepcopy(nested_list)
nested_list[0].append(7)
# print(nested_list)
# print(nested_copy)
"""
Xulosa
Immutable qiymatlar: Ko'chirilgan nusxa mustaqil ishlaydi.
Mutable qiymatlar: Havola ko'chiriladi, bu esa o'zgarishlar boshqa o'zgaruvchilarga ta'sir qiladi.
Mustaqil nusxa olish:
Oddiy usul: copy() yoki slicing ([:]).
Ko'p sathli tuzilmalar uchun: deepcopy().
"""

def kvadrat(son: int) -> int:
    return son ** 2

print(kvadrat(5))

"""
Senior Dasturchi Darajasidagi Amaliy Maslahatlar:
Memoization: Rekursiyani tezlashtirish uchun natijalarni keshda saqlang.
Stack Depth Error: Chuqur rekursiyani oldini olish uchun tail recursion 
optimization yoki iteratsiyaga o'ting.
Profilerlar bilan test qiling: Funksiyaning ishlash samaradorligini 
o'lchash uchun profiling vositalaridan foydalaning.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

































