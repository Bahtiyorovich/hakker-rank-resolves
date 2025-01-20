# 1. Berilgan sonning faktorialini rekursiv funksiya yordamida hisoblang.
# Kiruvchi ma'lumot: n (butun son,  𝑛 ≥ 1)
"""Muhim Eslatmalar
@lru_cache faqat immutable (o'zgarmas) argumentlar bilan ishlaydi (masalan, int, str, tuple).
Agar funksiya argumenti mutable (masalan, list, dict) bo'lsa,
bu dekorator ishlamaydi yoki xatolik yuzaga keladi.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    if n <= 1:
        return 1

    return n * factorial(n - 1)
# print(factorial(-1))
# print(factorial(5))

# Berilgan indeksdagi Fibonacci sonini rekursiv funksiya yordamida toping.
# Kiruvchi ma'lumot: n (butun son, n≥0)

lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))
# print(fibonacci(0))
# print(fibonacci(-1))
# print(fibonacci(1))



# Berilgan sonlar ro'yxatidagi barcha elementlarning yig'indisini rekursiv funksiya yordamida toping.
# Kiruvchi ma'lumot: list (butun sonlardan iborat ro'yxat)

def recursive_sum(lst):
    if not lst:
        return 0

    return lst[0] + recursive_sum(lst[1:])

# print(recursive_sum([1,2,3,4,5]))

def iter_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

# print(iter_sum([1,2,3,4,5]))

from functools import reduce
def reduce_sum(lst):
    return reduce(lambda x, y: x + y, lst)

# print(reduce_sum([1,2,3,4,5]))


# Palindrom
def is_palindrome(text):
    # Matnni tozalash
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Teskari ko‘rinishini tekshirish
    return cleaned_text == cleaned_text[::-1]

# Test qilish
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("hello"))  # False
# print(is_palindrome("madam"))  # True

def recursive_palindrome(text):
    # Matnni tozalash (rekursiyadan oldin)
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Rekursiv funksiya
    def check_recursive(s, start, end):
        # Tugatish shartlari
        if start >= end:
            return True

        if s[start] != s[end]:
             return False

        return check_recursive(s, start + 1, end - 1)
    return check_recursive(cleaned_text, 0, len(cleaned_text) - 1)
#
# print(recursive_palindrome("A man a plan a canal Panama"))  # True
# print(recursive_palindrome("hello"))  # False
# print(recursive_palindrome("madam"))  # True

# 5 Berilgan ro'yxatni rekursiv funksiya yordamida teskari tartibda qaytaring.
# Kiruvchi ma'lumot: list

def reverse_rekursive(lst):
    if len(lst) <= 1:
        return lst

    return [lst[-1]] + reverse_rekursive(lst[:-1])
#
# print(reverse_rekursive([1,2,3,4]))
# print(reverse_rekursive(['olma', 'banan', 'olcha', 'lemon']))

# 6 Berilgan butun sondan boshlab nolgacha orqaga hisoblovchi funksiyani rekursiv tarzda yarating.
# Kiruvchi ma'lumot: n (butun son, n≥0)

def print_recursive(n):
    if n < 0:
        return []

    return [n] + print_recursive(n - 1)

# print(print_recursive(5))


# 7 Berilgan ikkita sonning EKUBini rekursiv funksiya yordamida toping.
# Kiruvchi ma'lumot: a, b (butun sonlar)

def gcd_recursive(a, b):

    if b == 0:
        return a

    return gcd_recursive(b, a % b)

# print(gcd_recursive(48, 18))

# Berilgan butun sonning barcha raqamlari yig'indisini rekursiv funksiya yordamida hisoblang.
# Kiruvchi ma'lumot: n (butun son, n≥0)

def sum_of_digits_recursive(n):
    """ Tugatish sharti """
    if n < 10:
        return n
    # So'nggi raqamni ajratib olish va qolgan qismini qayta ishlash
    return (n % 10) + sum_of_digits_recursive(n // 10)

# print(sum_of_digits_recursive(12345))


def binary_search_recursive(arr, value, left, right):
    """ Tugatish sharti: agar chap ko'rsatkich o'ngdan oshib ketsa"""
    if left > right:
        return -1

    #O'rta indeksni hisoblash
    mid = (left + right) // 2

    # Agar qiymat o'rta elementga teng bo'lsa
    if arr[mid] == value:
        return mid

    # agar qiymat o'rta elementdan kichik bo'lsa chap qismini qidiring
    elif value < arr[mid]:
        return binary_search_recursive(arr, value, left, mid - 1)

    # aks holda o'ng qismini qidiring
    else:
        return binary_search_recursive(arr, value, mid + 1, right)


sorted_list = [1,2,3,4,5,6,7,8,9]
value_to_find = 7

# result = binary_search_recursive(sorted_list, value_to_find, 0, len(sorted_list) - 1)
# print(result)

# Map
# 1. Berilgan ro'yxatdagi barcha sonlarni kvadratga ko'paytiring.
lst0 = [1,2,3,4,5]
result0 = map(lambda x: x**2, lst0)
# print(list(result0))

# 2. Berilgan sonlar ro'yxatidagi barcha qiymatlarni 2 ga bo'ling va natijalarni qaytaring.
lst1 = [4,6,10,16,18]
result1 = map(lambda x: x / 2, lst1)
# print(list(result1))

# 3. Berilgan satrlar ro'yxatini bosh harf bilan boshlanadigan qilib qaytaring.
lst2 = ['reactjs', 'nodejs', 'javascript', 'python']
result2 = map(lambda x : x.title(), lst2)
# print(list(result2))

# 4. Berilgan raqamlar ro'yxatiga har bir qiymatga 10 qo'shing.
lst3 = [10, 15, 20, 25, 30]
result3 = map(lambda x: x + 10, lst3)
# print(list(result3))

# 5. Berilgan ikkita ro'yxatdagi bir xil indeksdagi sonlarni qo'shib, yangi ro'yxat qaytaring.
lst4 = [1,2,3]
lst5 = [9,8,7]

result4 = list(map(lambda x, y: x + y, lst4, lst5))
# print(result4)

# filter bo'yicha 5 ta masala:

# 1. Berilgan ro'yxatdan faqat juft sonlarni ajratib oling.
lst6 = list(range(1,11))
result6 = filter(lambda x: x % 2 == 0, lst6)
# print(list(result6))

# 2. Ro'yxatdagi barcha manfiy sonlarni chiqarib tashlang.
lst7 = list(range(-10, 11))
result7 = filter(lambda x: x < 0, lst7)
# print(lst7)
# print(list(result7))

# 3. Satrlar ro'yxatidan faqat uzunligi 5 dan katta bo'lganlarni tanlang.
lst8 = ['python', 'javascript', 'java', 'reactjs']
result8 = filter(lambda x: len(x) > 5, lst8)
# print(list(result8))

# 4. Berilgan ro'yxatdan faqat True qiymatlarni tanlang.
lst9 = [0, 1,10, True, False, -1]
result9 = filter(lambda x: x == True, lst9)
# print(list(result9))

# 5. Ro'yxatdan barcha "Python" bilan boshlanadigan satrlarni ajratib oling.
lst10 = ['Python_Dev', 'python@backend', 'Django', 'DRF']
result10 = filter(lambda x: x.startswith('Python'), lst10)
# print(list(result10))

# reduce bo'yicha 5 ta masala:
from functools import reduce

# 1. Berilgan sonlar ro'yxatidagi barcha qiymatlarni birlashtirib ko'paytmani qaytaring.

lst11 = [1,2,3,4,5]
result11 = reduce(lambda x, y: x * y, lst11 )
# print(result11)

# 2. Ro'yxatdagi barcha sonlarni birlashtirib qo'shish natijasini hisoblang.
lst12 = [1,2,3,4,5,6]
result12 = reduce(lambda x, y: x + y, lst12)
# print(result12)

# 3. Berilgan ro'yxatdan eng katta sonni toping.
lst13 = [1,0,3,7,10]
result13 = reduce(lambda x, y: x if x > y else y, lst13)
# print(result13)

# 4. Ro'yxatdan barcha satrlarni birlashtirib bitta to'liq matn qaytaring.
lst14 = ['I', 'am', 'web', 'developer']
result14 = reduce(lambda x, y: x + ' ' + y, lst14)
# print(result14)

# 5. Berilgan ro'yxatdagi sonlarning o'rtacha qiymatini hisoblang.
lst15 = [1,2,3]
result15 = reduce(lambda x, y: x + y, lst15)
# print(result15 / len(lst15))















