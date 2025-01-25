# "string qanday aniqlanadi"
from functools import total_ordering

name = "Sherzod"
last_name = 'Yoqubov'
bio = """
    Salom! Men python backend yo'nalishida 
    faoliyat olib boruvchi dasturchiman.
    Maqsadim, Toshkentdagi nufuzli IT kompaniyaga
    ishga kiraman. 
"""

# ""
# print(name)
# print(last_name)
# print(bio)

# 1.	Berilgan stringni kichik harflarga o‘zgartiring (lower()).
def word_lower(word):
    """berilgan so'zni barcha harflarini kichik harfga aylantiradigan funksiya"""

    # faqat string turlari uchun ishlaydi
    if not isinstance(word, str):
        return "Invalid argument"

    # Bo'sh string yoki faqat raqamli stringlarni tekshiradi
    if not word.strip() or word.isdigit():
        return "Invalid arguments"

    return word.lower()

# print(word_lower("Python"))         # python
# print(word_lower("123"))            # Invalid argument
# print(word_lower("   "))            # Invalid argument
# print(word_lower(["not a string"])) # Invalid argument
# print(word_lower("HELLO world!"))


# 2.	Berilgan stringni katta harflarga o‘zgartiring (upper()).
def word_upper(word):
    """ berilgan stringni barcha harflarini katta harflarga o'giradigan funksiya"""

    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip() or word.isdigit():
        return "Invalid argument"

    return word.upper()

# print(word_upper(""))
# print(word_upper("python backend"))
# print(word_upper("js2025"))
# print(word_upper("2025"))


# 3.	Stringdagi birinchi so‘zning faqat birinchi harfini katta qiling (capitalize()).
def word_capitalize(word):
    """ Berilgan stringni faqat birinchi harfini katta qiladigan funksiya"""

    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip() or word.isdigit():
        return "Invalid argument"

    return word.capitalize()

# print(word_capitalize(""))
# print(word_capitalize("2025"))
# print(word_capitalize("python"))
# print(word_capitalize("js2025"))

# 4.	Stringdagi har bir so‘zning birinchi harfini katta qiling (title()).

def word_title(word):
    """Berilgan stringni har bir birinchi harfini katta qiluvchi funksiya """

    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip() or word.isdigit():
        return "Invalid argument"

    return word.title()

# print(word_title(""))
# print(word_title("python backen developer"))
# print(word_title("2025"))
# print(word_title("javascript 2025"))


def word_swapcase(word):
    """ Berilgan stringni katta harflarini kichikka va aksincha o'zgartiruvchi funksiya """

    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip() or word.isdigit():
        return "Invalid argument"

    return word.swapcase()

# print(word_swapcase(""))
# print(word_swapcase("2025"))
# print(word_swapcase("pTHon LanGuagE"))
# print(word_swapcase("python 2025"))
# print(word_swapcase("PYTHON"))




# 6.	String boshida va oxirida bo‘sh joylar mavjud bo‘lsa, ularni olib tashlang (strip()).

def word_strip(word):
    """Berilgan stringni boshida va oxirida bo'shliq bo'lsa olib tashlaydi"""

    if not isinstance(word, str):
        return "Invalid argument"
    if not word.strip():
        return "Invalid argument"

    return word.strip()

# print(word_strip(""))
# print(word_strip("   Python"))
# print(word_strip("Python  "))
# print(word_strip(" 2025 "))
# print(word_strip("2027"))


# 7.	String boshida mavjud bo‘lgan belgilarning ro‘yxatini olib tashlang (lstrip()).

def word_lstrip(word):
    """Berilgan stringni boshida bo'shliq bo'lsa olib tashlaydi"""
    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip():
        return "Invalid argument"

    return word.lstrip()

# print(word_lstrip(""))
# print(word_lstrip("  Python"))
# print(word_lstrip("Python***  "))
# print(word_lstrip("2025"))
# print(word_lstrip(" 2027-py * "))


# 8.	String oxirida mavjud bo‘lgan belgilarning ro‘yxatini olib tashlang (rstrip()).

def word_rstrip(word):
    """Berilgan stringni oxirida bo'shliq bo'lsa olib tashlaydi"""

    if not isinstance(word, str):
        return "Invalid argument"

    if not word.strip():
        return "Invalid argument"

    return word.rstrip()

# print(word_rstrip(""))
# print(word_rstrip("Python   "))
# print(word_rstrip("  Js2025   "))


# 9.	Berilgan stringni boshqa string bilan almashtiring (replace()).

# def word_replace(txt, word, repl_word):
#     """Berilgan stringda berilgan so'zni almastirish"""
#     if not isinstance(txt, str):
#         return "Invalid argument"
#
#     if not txt.strip() or not word.strip() or not repl_word.strip():
#         return "Invalid arguments"
#
#     if word in txt:
#         return txt.replace(word, repl_word)
#     else:
#         return "The word is not found in the given text."
# text = "Python is a dynamic programming language"

# print(word_replace("", "", ""))
# print(word_replace(text, "", "js"))
# print(word_replace("", "Python", "js"))
# print(word_replace(text, "Python", "js"))


# 10.	Berilgan stringni so‘zlar ro‘yxatiga ajratib oling (split()).

def word_split(text):
    """Berilgan stringni so'zlar ro'yxatiga aylantirish"""
    if not isinstance(text, str):
        return "Invalid argument"

    if not text.strip():
        return "Invalid argument"

    return text.split()

# print(word_split(""))
# print(word_split("py js django react"))


# 11.	String ichida substring borligini tekshiring (in operatori).
# substring bu izlanayotgan satr

def word_substring(txt, word):
    """Berilgan text ichida word bor yoki yo'qligini aniqlang"""

    if not isinstance(txt, str):
        return "Invalid argument"

    if not txt.strip():
        return "Invalid argument"

    return True if word in txt.strip() else False

text0 = "Python is best programming language"
# print(word_substring(text0, "best"))
# print(word_substring(text0, " "))
# print(word_substring(text0, "js"))


# 12.	Substringning string ichidagi birinchi paydo bo‘lish indeksini toping (find()).

def word_find(txt, word):
    """
        Berilgan txt matni ichida word substringning birinchi paydo bo'lish indeksini topish funksiyasi

        :param txt: Qidiruv amalga oshiriladigan matn
        :param word: qidirilayotgan substring
        :return Substringni birinchi paydo bo'lish joyi yoki -1 (topilmasa)
        :raises ValueError: agar argumentlar noto'g'ri bo'lsa
    """
    # 1. Tekshiruv: 'txt' va 'word' string turlari ekanligini tekshirish
    if not isinstance(txt, str):
        raise ValueError("The 'txt' parametr must be a string.")

    if not isinstance(word, str):
        word = str(word) # stringga konvertatsiya qilish

    # 2. Tekshiruv: 'txt' va 'word' bo'sh emasligini ta'minlash
    if not txt.strip():
        raise ValueError("The 'txt' parametr cannot be empty or only whitespace")

    if not word.strip():
        raise ValueError("The 'word' parametr cannot be empty or only whitespace")

    # 3. find() metodidan foydalanib natijani qaytarish
    return txt.find(word)

# if __name__ in "__main__":
#     text1 = "Python backend dev"
#     try:
#      print(word_find("", ""))
#     except ValueError as e:
#         print(e)

    # print(word_find(text1, "Python"))
    # print(word_find(text1, 'b'))
    # print(word_find(text1, 2025))


# 13.	Substringning string ichidagi indeksini aniqlang (index())
# (agar substring topilmasa xato chiqaradi).

def word_index(txt, word):
    """
    Berilgan txt matni ichidan word substringni aniqlaydigan funksiya
    :param txt: Qidiruv amalga oshiriladigan matn
    :param word: izlanayotgan substring
    :return: substringni birinchi index joyi
    :raises ValueError: agar parametrlar noto'g'ri bo'lsa yoki substring topilmasa
    """
    # 1. txt va word parametrlari kerakli turda ekanligini tekshirish
    if not isinstance(txt, str):
        raise ValueError("The 'txt' parametr must be a string.")

    if not isinstance(word, str):
        word = str(word) # Stringga o'zgartiriladi

    # 2. bo'sh qiymatlarni tekshiradi
    if not txt.strip():
        raise ValueError("The 'txt' parametr cannot be  empty or only whitespace")

    if not word.strip():
        raise ValueError("The 'word' parametr cannot be empty or only whitespace")

    if word in txt:
        return txt.index(word)

    raise ValueError(f"The word {word} was not found in the given text.")

# if __name__ in "__main__":
#     txt = "Python web developer"
#     try:
#         print(word_index("", ""))
#     except ValueError as e:
#         print(e)
#
#     print(word_index(txt, "web"))
#     print(word_index(txt, 2025))
#     try:
#         print(word_index(txt, "js"))
#     except ValueError as e:
#         print(e)


# 14.	Substring string ichida nechta marta uchrayotganini hisoblang (count()).

def word_count(txt: str, word: str) -> int:
    """
    Berilgan txt ichida word necha marta qatnashganini count() metodi bilan aniqlaydigan funksiya
    :param txt: Berilgan matn
    :param word: izlanayotgan so'z
    :return: substringni uchrash soni
    """

    if not word:
        raise ValueError("Substring bo'sh bo'lishi mumkin emas")

    count = txt.count(word)
    return count

# text2 = "reactjs, js, nodejs, vuejs"
# substr = "js"
# result = word_count(text2, substr)
# print(result)


# 15.	Stringning berilgan substring bilan boshlanishini aniqlang (startswith()).

def word_startswith(txt:str, word:str):
    """
    Berilgan matn word parametri bilan boshlanishini startswith() metodi bilan boshlanishini aniqlash
    :param txt: berilgan matn
    :param word: berilgan substring
    :return: qaytariladigan qiymat
    """

    if not word:
        raise ValueError("substring bo'sh bo'lishi mumkin emas")

    return txt.startswith(word)

# text3 = "Python web developer"
# substr = 'P'
# print(word_startswith(text3, substr))

# 16.	Stringning berilgan substring bilan tugashini aniqlang (endswith()).

def word_endswith(txt:str, word:str):
    """
    Berilgan matn word parametri bilan tugashini endswith() metodi bilan aniqlaydigan funksiya
    :param txt: berilgan matn
    :param word: izlanayotgan substring
    :return: qiymat qaytarish
    """

    if not word:
        raise ValueError("substring bo'sh bo'lishi mumkin emas")

    return txt.endswith(word)

# text4 = "string.py"
# substr = ".py"
# print(word_endswith(text4, substr))


# 17.	Stringdagi birinchi paydo bo‘lgan substringni olib tashlang.

def remove_first_occurrence(txt:str, word:str) -> str:
    """
    Stringdan birinchi paydo bo'lgan substringni olib tashlaydi
    :param txt:Asosiy matn
    :param word: olib tashlanadigan substring
    :return:Birinchi paydo bo'lgan substring olib tashlangan matn
    :raises ValueError: agar substring bo'sh bo'lsa yoki string topilmasa
    """

    if not word:
        raise ValueError("Substring bo'sh bo'lishi mumkin emas")

    index = txt.find(word)
    if index == -1:
        raise ValueError(f"Substring '{word}' matn ichida topilmadi.")

    return txt[:index] + txt[index + len(word):]

# text5 = "abracadabra"
# substring = "abra"
# result = remove_first_occurrence(text5, substring)
# print(f"Natija: '{result}'")

# 18.	Stringdagi substringni boshqa substringga almashtiring (replace()).

def word_repl(txt:str, word:str, repl_word:str) -> str:
    """
    Stringdagi substringni boshqa substringga almashtiradi
    :param txt: Asosiy matn
    :param word: almashtiriladigan so'z
    :param repl_word: yangi so'z
    :return: almashtirilgan matn
    """

    return txt.replace(word, repl_word)

# text6 = "py js nodejs, reactjs"
# substr = "py"
# repl_word = "js"
# print(word_repl(text6, substr, repl_word))


# 19.	Berilgan string ichidagi har bir belgi yoki substringning oxirgi paydo bo‘lishini toping (rfind()).

def rfind_method(txt:str, word:str) -> int:
    """
    	Berilgan string ichidagi har bir belgi yoki substringning oxirgi paydo bo‘lishini topadigan o'rni
    :param txt: Asosiy matn
    :param word: izlanayotgan substring
    :return: substringni oxirgi paydo bo'lish o'rnini qaytaradi
    """

    if not word:
        raise ValueError("Substring bo'sh bo'lishi mumkin emas")

    return txt.rfind(word)

text7 = "Asosiy matn shu yerda matn berilgan"
substring = "matn"
# print(rfind_method(text7, substring))


# 20.	Berilgan substringning mavjud emasligi holatini boshqarib ko‘rsating (find() vs index()).
def find_vs_index_methods(txt:str, substr:str) -> int:
    """
        find vs index methods
    :param txt: Asosiy matn
    :param substr: substring qiymati
    :return:
    """

    if not substr:
        raise ValueError("Substring bo'sh bo'lishi mumkin emas.")

    index = txt.find(substr)
    if index == -1:
        raise ValueError(f"Asosiy matn tarkibida {substr} substring topilmadi.")

    if substr in txt:
        return txt.index(substr)

    raise ValueError(f"Substring mavjud emas")

# text8 = "Asosiy matn shu yerda joylashgan"
# substr = "js"
# print(find_vs_index_methods(text8, substr))


# 21.	Bir nechta stringlarni bitta stringga birlashtiring (join()).
def join_method(lst: list[str]) -> str:
    """berilgan ro'yxat elementlarini join yordamida birlashtirish"""
    if not lst:
        raise ValueError("The 'lst' cannot be empty")

    return ", ".join(lst)

# arr = ["py", "js", "html", "css"]
# print(join_method(arr))


# 22.	Stringni har bir belgi yoki substringdan keyin bo‘lish (split).
def split_method(txt:str, substr:str) -> list:
    """
        Stringni har bir belgi yoki substringdan keyin bo‘lish (split).
        :param txt: Asosiy string
        :param substr: substring qiymati
        :raises ValueError: Agar string bo'sh bo'lsa qaytariladi
        :return: natija string qaytariladi
    """

    if not txt.strip():
        raise ValueError("Asosiy matn bo'sh")

    return txt.split(substr)


text9 = "Asosiy matn shu yerda"
substr = " "
# print(split_method(text9, substr))



# 26.	Stringning har bir belgisiga indeks raqami qo‘shilgan format yarating.

def enumerate_method(txt:str) -> str:
    """
    Stringning har bir belgisiga indeks raqami qo‘shilgan format yaratadi
    :param txt: Asosiy matn
    :return: index raqami qo'shilgan format qaytaradi
    """

    if not txt:
        raise ValueError("Txt bo'sh ekan")

    enumerate_txt = ", ".join([f"{i}{char}" for i, char in enumerate(txt)])
    return enumerate_txt

text10 = "Python"
# print(enumerate_method(text10))


def generate_order_id(order_number, total_order):
    order_id = f"Buyurtma ID: {str(order_number).zfill(len(str(total_order)))}"
    return order_id

# order_number = 17
# total_order = 1000
# print(generate_order_id(order_number, total_order))

def generate_receipt_line(item, price, width=30):
    """Narxni belgilar bilan o'ngga suramiz"""
    formatted_line = f"{item.rjust(width - 10)} | {str(price).rjust(10)} so'm"
    return formatted_line

# item = "Telefon"
# price = 1200000
# print(generate_receipt_line(item, price))


# 31.	String palindrom ekanligini aniqlang ([::-1]).
def is_palendrome(string:str) -> bool:
    """
        Berilgan stringni palendrome ekanligini aniqlash uchun uni
        reverse qilib asli bilan solishtirish kerak
        :param: Asosiy string
        :return palendrome stringni natijasini bool qiymatda qaytaradi
    """

    cleaned_str = string.replace(" ", "").lower()

    return cleaned_str == cleaned_str[::-1]

# string = "level"
# string2 = "Hello"
# print(is_palendrome(string))
# print(is_palendrome(string2))


def reverse_txt(string: str) -> bool:
    """
    berilgan string palendromeligini aniqlash
    :param string: Asosiy matn
    :return: agar qiymat palendrome bo'lsa boolean qiymat qaytariladi
    """

    cleaned_str = "".join(char.lower() for char in string if char.isalnum())
    return cleaned_str == cleaned_str[::-1]


example1 = "A man, a plan, a canal: Panama"
example2 = "No lemon, no melon"
example3 = "Hello, World!"

# print(reverse_txt(example1))
# print(reverse_txt(example2))
# print(reverse_txt(example3))


# 34.	Faqat harflardan iborat stringni teskari qilib qaytaring.

def is_alpha(string: str) -> str:
    """
    Agar string faqat harflardan iborat bo'lsa reverse qiladi
    :param string:Asosiy matn
    :return: reverce string qaytaradi
    """

    if not string.isalpha():
        raise ValueError(f"'{string}': Berilgan string tarkibida raqam qatnashishi mumkin emas.")
    return string[::-1]

# word7 = "hello"
# word8 = "2025Py"
# if __name__ in "__main__":
#     try:
#         print(is_alpha(word8))
#     except ValueError as e:
#         print(e)
#
#     print(is_alpha(word7))


# 35.	Stringni teskari qilib, har bir so‘zni alohida qaytaring.

def reversed_string(string:str) -> str:
    """
    Berilgan stringni teskariga o'girib, har bir so'zni alohida qaytaradigan funksiya
    :param string: Asosiy matn
    :return: reverse qilingan so'z
    """
    if not string.strip():
        raise ValueError("Berilgan string bo'sh bo'lishi mumkin emas.")

    reversed_list = string[::-1].split()
    return ",".join(reversed_list)

txt10 = "PY JS HTML CSS"
# if __name__ in "__main__":
#     try:
#         print(reversed_string(""))
#     except ValueError as e:
#         print(e)
#
#     print(reversed_string(txt10))

# 36.	Stringdagi barcha bo‘sh joylarni olib tashlab, natijani qaytaring.

def remove_whitespace(string: str) -> str:
    """
    Berilgan stringdagi barcha whitespacelarni olib tashlash
    :param string: Asosiy matn
    :return: whitespace olib tashlangan string
    """

    if not string.strip():
        raise ValueError("Berilgan string bo'sh bo'lishi mumkin emas.")

    return string.replace(" ", "")

txt11 = " The Python programming language "
# if __name__ in "__main__":
#     try:
#         print(remove_whitespace(""))
#     except ValueError as e:
#         print(e)
#
#     print(remove_whitespace(txt11))

# 38.	String ichidagi eng uzun so‘zni toping.

def max_len(string: str) -> str:
    """
    Eng uzun so'zni qaytaradigan funksiya
    :param string: Asosiy matn
    :return: eng uzun so'z
    """
    if not string.strip():
        return "String cannot be empty"

    string_list = string.split()
    result = max(string_list, key=len)

    return result

text12 = "Python is very fast programming language"
# print(max_len(text12))



# 39.	String ichidagi eng ko‘p uchraydigan belgi yoki substringni aniqlang.

import re
from collections import Counter

def preprocess_string(string: str) -> str:
    """
    Berilgan stringni keraksiz bo'sh joylar, katta-kichik harflarga sezgirlikni tozalash
    :param string:Asosiy matn
    :return: tozalangan string
    """
    if not string.strip():
        return "String bo'sh ekan"

    return re.sub(r'\s+', ' ', string.strip())


# Eng ko'p uchraydigan belgi uchun
def most_frequent_character(string: str) -> (str, int):
    """
    Eng ko'p uchraydigan belgini topish
    :param string: Asosiy matn
    :return:
    """
    string = preprocess_string(string)
    counter = Counter(string)
    max_count = max(counter.values())
    most_frequent = [char for char, count in counter.items() if count == max_count]

    return most_frequent, max_count


# text = "Dasturlash dasturda dasturchi"
# result = most_frequent_character(text)
# print(f"Eng ko'p uchraydigan belgi(lar): {result[0]} ({result[1]} marta)")


# Eng ko'p uchraydigan substring
def most_frequent_substring(string, k=2):
    """
    Eng ko'p uchraydigan substringni aniqlash
    :param string: Asosiy matn
    :param k: substringni eng minimal uzunligi
    :return: eng ko'p uchraydigan substring va uni soni
    """

    string = preprocess_string(string)
    n = len(string)

    if n < k:
        return None, 0

    counter = Counter(string[i:i + k] for i in range(n - k + 1))
    max_count = max(counter.values())
    most_frequent = [substr for substr, count in counter.items() if count == max_count]
    return most_frequent, max_count

# text = "abababab"
# result = most_frequent_substring(text, k=2)
# print(f"Eng ko'p uchraydigan substring(lar): {result[0]} ({result[1]} marta)")



# 40.	Teskari string yordamida yangi formatlangan string yarating.

def reverse_and_format_string(string: str) -> str:
    """
    Berilgan stringni teskari tartibda formatlash funksiyasi
    :param string: Asosiy string
    :return: formatlangan string
    """

    reverse_string = string[::-1]
    return reverse_string

# input_string = "hello world"
# output = reverse_and_format_string(input_string)
# print(f"Original: {input_string}")
# print(f"Teskari formatlangan: {output}")


def reverse_words_and_format_string(string: str) -> tuple:
    """
    Berilgan stringni har bir so'zini belgilarigacha teskari tartibda formatlaydigan funk
    :param string:Asosiy string
    :return: formatlangan string
    """

    words = string.split()
    reversed_string = ' '.join(words[::-1])

    reversed_each_word = ' '.join(word[::-1] for word in words)

    return reversed_string, reversed_each_word


# input_string = "hello world"
# output = reverse_words_and_format_string(input_string)
# print(f"Original: {input_string}")
# print(f"Teskari formatlangan: {output}")



# 41.	Stringni paragraflar bo‘yicha bo‘ling va ularni qayta tartiblang.

def reverse_paragraphs(string: str) -> str:
    """
    Berilgan stringni paragraph bo'yicha tartiblovchi funksiya
    :param string: Asosiy string
    :return: paragrf bo'yicha teskari tartiblangan string qiymat
    """

    paragraphs = string.split('\n')
    reverse_paragraphs = '\n'.join(paragraphs[::-1])

    return reverse_paragraphs

# input_text = """Paragraph 1: Python is an amazing programming language.
#
# Paragraph 2: It is used for web development, data analysis, AI, and more.
#
# Paragraph 3: The community support for Python is incredible."""
#
# # Funktsiyani chaqirish
# output_text = reverse_paragraphs(input_text)
# print("Original Paragraflar:")
# print(input_text)
# print("\nTeskari Paragraflar:")
# print(output_text)



# 42.	String ichidagi barcha so‘zlarning birinchi harfini katta qiling va

def title_string(string: str) -> str:
    """
    Berilgan stringni har bir so'zni bosh harfini katta qolganlarini kichik qiladi
    :param string: Asosiy matn
    :return: formatlangan qiymat
    """

    result = string.title()
    return result

# input_string = "Python web developer and web designer"
# print(title_string(input_string))


# 43.	Berilgan stringning faqat sonlardan iborat qismini ajratib oling (isdigit()).

def only_number_string(string: str) -> str:
    """
    Berilgan stringdagi faqat sonlarni ajratib olish
    :param string: Asosiy matn
    :return: ajratib olingan string typedagi raqamli qiymatlar
    """
    split_string = string.split()
    return ', '.join(num for num in split_string if num.isdigit())

# input_string = "2025 python 1997"
# print(only_number_string(input_string))


# 44.	String ichida faqat harflar bo‘lsa, ularni tartibga keltiring (isalpha()).

def is_alpha_string(string: str) -> str:
    """
    Berilgan string ichidagi faqat harflarni tartiblovchi funksiya
    :param string: Asosiy matn
    :return: formatlangan string
    """

    words = [word for word in string if word.isalpha()]

    return ','.join(sorted(words))

# input_string = "python 2025 js2024"
# print(is_alpha_string(input_string))



# 45.	String ichidagi maxsus belgilarni olib tashlang.

def regular_marks(string: str) -> tuple:
    """
    Berilgan string ichidagi belgilarni ajratib oluvchi funksiya
    :param string: Asosiy matn
    :return: belgilar
    """

    patterns = r'[^a-zA-z0-9\s]'
    special_char = re.findall(patterns, string)
    special_char_alpha = re.sub(patterns,'', string)
    return special_char, special_char_alpha

# input_string = "py 2025 test@gmail.com !? @sherzod1797"
# print(regular_marks(input_string))


# 46.	URL ichidagi domen nomini ajratib oling (split(), find()).

def find_domain(url: str) -> str:
    """
    Berilgan string ichida url uchun domain ni ajratib oluvchi funk
    :param string: Asosiy matn
    :return: domain
    """
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    return domain if domain else "Noto'g'ri url"

urls = [
    "https://www.google.com/search?q=python",
    "http://example.org/about",
    "https://subdomain.website.uz/blog",
    "ftp://ftp.example.com/files",
    "not-a-valid-url"
]

# for url in urls:
#     print(f"URL: {url}")
#     print(f"Domain: {find_domain(url)}\n")


# 47.	Matnda ko‘rinadigan email manzillarni toping (regex ishlating).

def find_emails(string:str) -> list:
    """
    Berilgan string tarkibida email topilsa qaytaradi
    :param string: Asosiy matn
    :return: emaillar ro'yxatini qaytaradi
    """

    email_pattern = r'[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, string)

    return emails

text_email = """
    Hello, you can contact us at support@example.com for support. 
    Alternatively, reach out to admin@website.uz or info@company.co.uk.
    Fake emails like test@com or hello@.com won't be captured!
"""

# found_emails = find_emails(text_email)
# print(found_emails)

def remove_html_tag(html:str) -> str:
    """
    Berilgan html kodlarini faqat content qismlarini qaytaradi
    :param html: Asosiy html kodlari string formatida
    :return: html taglarisiz matn
    """

    html_tag_pattern = r'<.*?>'
    cleaned_text = re.sub(html_tag_pattern, '', html)

    return cleaned_text

html_text = """
<html>
    <head><title>My Website</title></head>
    <body>
        <h1>Welcome to My Website</h1>
        <p>This is a paragraph.</p>
        <a href="https://example.com">Click here</a>
    </body>
</html>
"""
# print(remove_html_tag(html_text))


import json
def validate_and_convert_to_json(data:str) -> str:
    """
    berilgan stringni json formatiga convertatsiya qiluvchi funksiya
    :param data: Asosiy matn
    :return: json data
    """
    try:
        json_data = json.loads(data)
        return json.dumps(json_data, indent=4)
    except json.JSONDecodeError as e:
        return f"Xatolik: String haqiqiy JSON formatida emas!\n{e}"

# string_data = '{"name":"Ali", "age":30, "city":"New York"}'
# result = validate_and_convert_to_json(string_data)
# print(result)


def convert_to_snake_case(text:str) -> str:
    """
    Berilgan stringni snake_case usuliga o'tkazing
    :param text: Asosiy matn
    :return: snake_case usuliga o'tkazilgan string
    """

    sub_text = re.sub(r'([a-z])([A-Z])', r'\1\2', text)
    return sub_text.lower()


def convert_to_camel_case(text:str) -> str:
    """
    Berilgan stringni camelCase usuliga convertatsiya qiluvchi funk
    :param text: Asosiy matn
    :return: camelCase usuli qo'llanilgan string
    """

    words = text.split('_')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

string_snake_case = "ThisIsCamelCase"
string_camel_case = "this_is_snake_case"

snake_case_result = convert_to_snake_case(string_snake_case)
camel_case_result = convert_to_camel_case(string_camel_case)

print("Original CamelCase string:", string_snake_case)
print("Snake_case formatiga:", snake_case_result)

print("\nOriginal Snake_case string:", string_camel_case)
print("CamelCase formatiga:", camel_case_result)
























