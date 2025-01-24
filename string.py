# "string qanday aniqlanadi"

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

def word_replace(txt, word, repl_word):
    """Berilgan stringda berilgan so'zni almastirish"""
    if not isinstance(txt, str):
        return "Invalid argument"

    if not txt.strip() or not word.strip() or not repl_word.strip():
        return "Invalid arguments"

    if word in txt:
        return txt.replace(word, repl_word)
    else:
        return "The word is not found in the given text."
text = "Python is a dynamic programming language"

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

if __name__ in "__main__":
    text1 = "Python backend dev"
    try:
     print(word_find("", ""))
    except ValueError as e:
        print(e)

    # print(word_find(text1, "Python"))
    # print(word_find(text1, 'b'))
    # print(word_find(text1, 2025))











