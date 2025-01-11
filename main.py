# Hakker-Rank Masalalar yechimi: for Python(core) and Python(medium)

# 1. Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2  to  5, print Not Weird
# If n is even and in the inclusive range of 6  to 20 , print Weird
# If n is even and greater than 20 , print Not Weird
# Input Format
# A single line containing a positive integer, n.
# Constraints : 1<= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Explanation 0 : n = 3
#  n is odd and odd numbers are weird, so print Weird.
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation 1: n = 24,
# n> 20
#  and n is even, so it is not weird.

def weird_or_not(n):
    if n % 2 != 0:  # Agar son toq bo'lsa
        return "Weird"
    else:  # Agar son juft bo'lsa
        if 2 <= n <= 5:  # 2 dan 5 gacha bo'lgan juft sonlar
            return "Not Weird"
        elif 6 <= n <= 20:  # 6 dan 20 gacha bo'lgan juft sonlar
            return "Weird"
        else:  # 20 dan katta bo'lgan juft sonlar
            return "Not Weird"

# Test uchun inputni o'qish
if __name__ == "__main__":
    n = int(input().strip())
    print(weird_or_not(n))




# 2-masala
import re

def is_valid_roman(s):
    # Valid Rim raqami uchun regex
    roman_regex = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(roman_regex, s))

# Input olish
roman = input().strip()
print(is_valid_roman(roman))

"""
Regex qoidalari:

M{0,3}: 
𝑀
M harfi 0 dan 3 martagacha paydo bo'lishi mumkin (
1000
1000 qiymatlari uchun).
(CM|CD|D?C{0,3}): 
𝐶
C harfi kombinatsiyasi 
100
,
200
,
.
.
.
,
900
100,200,...,900 qiymatlarini qamrab oladi.
(XC|XL|L?X{0,3}): 
𝑋
X harfi kombinatsiyasi 
10
,
20
,
.
.
.
,
90
10,20,...,90 qiymatlari uchun.
(IX|IV|V?I{0,3}): 
𝐼
I harfi kombinatsiyasi 
1
,
2
,
.
.
.
,
9
1,2,...,9 qiymatlari uchun.
re.match:

Regex bilan mos keladigan qiymatni tekshiradi.
bool() yordamida mos kelishini True/False sifatida qaytaramiz.
"""
"""
Ushbu masalada 3D koordinatalar ro‘yxatini generatsiya qilish kerak, bunda har bir koordinata uchun 
𝑖
+
𝑗
+
𝑘
≠
𝑛
i+j+k

=n bo‘lishi kerak. Quyida ushbu masala uchun list comprehension asosida yechimni ko‘rib chiqamiz:

Yechim Kodi:
python
Copy code
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# List comprehension orqali 3D koordinatalarni generatsiya qilish
result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if i + j + k != n]

print(result)
Izohlar:
range(x + 1):
𝑖
,
𝑗
,
𝑘
i,j,k qiymatlari 
0
0 dan 
𝑥
,
𝑦
,
𝑧
x,y,z gacha bo'lishi kerakligi uchun range funksiyasida 
𝑥
+
1
x+1, 
𝑦
+
1
y+1, 
𝑧
+
1
z+1 ko'rsatiladi.
List comprehension:
Uch darajali for operatorlari orqali barcha kombinatsiyalar yaratiladi.
Filter sharti:
if i + j + k != n: Faqat 
𝑖
+
𝑗
+
𝑘
≠
𝑛
i+j+k

=n bo'lgan koordinatalar ro'yxatga qo'shiladi.
Misollar:
Kirish:
makefile
Copy code
x = 1
y = 1
z = 1
n = 2
Chiqish:
css
Copy code
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Kirish:
makefile
Copy code
x = 2
y = 2
z = 2
n = 2
Chiqish:
css
Copy code
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], 
 [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], 
 [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
Qisqacha Qoida:
List comprehension orqali biz uch darajali for tsiklini ixchamlashtiramiz.
Filter shartlari orqali biz kerakli qiymatlarni ajratib olamiz.
"""
# 3-masala
n = int(input())
scores = list(map(int, input().split()))

# Ro'yxatni tartibga keltirish va unikal qiymatlarni olish
unique_scores = sorted(set(scores), reverse=True)

# Ikkinchi eng yuqori qiymatni chop etish
print(unique_scores[1])

# Inputlarni qabul qilish
n = int(input())  # Ishtirokchilar soni
scores = list(map(int, input().split()))  # Natijalarni qabul qilish

# Birinchi eng yuqori qiymatni topish va o'chirish
max_score = max(scores)
scores = [score for score in scores if score != max_score]

# Ikkinchi eng yuqori qiymatni topish
runner_up = max(scores)
print(runner_up)

"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by
n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
Input Format:
The first line contains an integer, n , denoting the number of commands.
Each line i of the n  subsequent lines contains one of the commands described above.
Constraints:
The elements added to the list must be integers.
Output Format:
For each command of type print, print the list on a new line.

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    n = int(input())  # Buyruqlar sonini o'qish
    lst = []  # Bo'sh ro'yxatni yaratish

    for _ in range(n):
        command = input().split()  # Buyruq va argumentlarni ajratish
        cmd = command[0]  # Buyruq nomi
        args = command[1:]  # Argumentlar (agar mavjud bo'lsa)

        try:
            if cmd == "insert":
                # Indeks va qiymatni tekshirib, qo'shish
                lst.insert(int(args[0]), int(args[1]))
            elif cmd == "print":
                print(lst)  # Ro'yxatni chop etish
            elif cmd == "remove":
                # Agar qiymat mavjud bo'lsa, uni olib tashlash
                lst.remove(int(args[0]))
            elif cmd == "append":
                # Ro'yxat oxiriga element qo'shish
                lst.append(int(args[0]))
            elif cmd == "sort":
                lst.sort()  # Ro'yxatni tartiblash
            elif cmd == "pop":
                # Ro'yxat bo'sh bo'lmasa, oxirgi elementni olib tashlash
                if lst:
                    lst.pop()
            elif cmd == "reverse":
                lst.reverse()  # Ro'yxatni teskari tartibga keltirish
        except (ValueError, IndexError):
            # Noto'g'ri argument yoki indeks bo'lsa, o'tkazib yuborish
            print(f"Xato: Buyruq noto'g'ri yoki ro'yxatda mavjud emas: {command}")


"""
Sizga butun son berilgandan so'ngelektron pochta manzillari.
 Sizning vazifangiz leksikografik tartibda faqat haqiqiy elektron pochta manzillarini
o'z ichiga olgan ro'yxatni chop etishdir .


Yaroqli elektron pochta manzillari quyidagi qoidalarga amal qilishi kerak:

U username@websitename.extension format turiga ega bo'lishi kerak.
Foydalanuvchi nomi faqat harflar, raqamlar, tire va pastki chiziqdan iborat bo'lishi mumkin.
Veb-sayt nomi faqat harflar va raqamlardan iborat bo'lishi mumkin.
Kengaytma faqat harflardan iborat bo'lishi mumkin.
Kengaytmaning maksimal uzunligi.

Kontseptsiya

Filtr "True" yoki "False" ni qaytaruvchi funksiyani oladi va 
uni ketma-ketlikka qo'llaydi va faqat funksiya "True" ni qaytargan ketma-ketlik
 a'zolari ro'yxatini qaytaradi . Filtrlar bilan Lambda funksiyasidan foydalanish mumkin.Example

Complete the function fun in the editor below.

fun has the following paramters:

string s: the string to test
Returns

boolean: whether the string is a valid email or not
Input Format

The first line of input is the integer , the number of email addresses.
 lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""
import re
def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)


"""You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  """

def swap_case(s):
    if not s:
        return ""

    current_char = s[0].lower() if s[0].isupper() else s[0].upper()
    return current_char + swap_case(s[1:])


# textwrap
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)























