# 1 dan n gacha bo'lgan sonlarni qaytaruvchi generator yozing.
def generator_numbers(n):
    for i in range(1, n+1):
        yield i

gen = generator_numbers(10)
# for _ in range(10):
#  print(next(gen), end=", ")

# Berilgan ro'yxatdagi juft sonlarni qaytaruvchi generator yarating.

def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

lst = [1,2,3,4,5,6,7,8,9,10]
# res = filter_even(lst)
# print(list(res))

# Cheksiz natural sonlarni qaytaruvchi generator yarating.
def infinite_numbers():
    i = 1
    while True:
        yield i
        i += 1
# number = infinite_numbers()
# for _ in range(10):
#     print(next(number), end=" ")



# Berilgan matn satrlaridagi so'zlarni birma-bir qaytaruvchi generator yozing.
def word_generator(text):
    for word in text.split():
        yield word

txt = "Hello!, I'm Sherzod, Are you okey?"
# words = word_generator(txt)
# print(' '.join(list(words)))


# Fibonacci ketma-ketligini qaytaruvchi generator yarating

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# fibonacci = fibonacci_sequence(6)
# print(list(fibonacci), end=" ")


# Kattalashtirilgan harflarni qaytaruvchi generator yozing.

def word_upper(text):
    for word in text:
        yield word.upper()

txt1 = ['js', 'py', 'jsx', 'html', 'css']
result0 = word_upper(txt1)
# print(list(result0))

# Berilgan ro'yxatdagi barcha sonlarning kvadratlarini qaytaruvchi generator yarating.
def squire_number(lst):
    for i in lst:
        yield i ** 2

lst1 = [2,3,4]
res = squire_number(lst1)
# print(list(res))


# Berilgan ro'yxatdagi matnlarning uzunligini qaytaruvchi generator yozing.
def len_word_generator(arr):
    for word in arr:
        yield len(word)

words_list = ['python', 'javascript', 'nodejs', 'reactjs']
result2 = len_word_generator(words_list)
# print(list(result2))

# 1 dan n gacha bo'lgan sonlarning faqat toqlarini qaytaruvchi generator yozing.
def odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i

odd = list(odd_numbers(20))
# print(odd)

# Berilgan matnni har bir harfini teskarisiga qaytaruvchi generator yozing.
def char_reversed(text):
    for char in reversed(text):
        yield char

txt0 = 'Python'
char = list(char_reversed(txt0))
# print(', '.join(char))










