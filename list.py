# List mavzusi bo'yicha masalalar yechimi
from typing import Union, List, Optional


# 1.	Berilgan ro'yxatdagi barcha elementlarni ekranga chiqaring.
def view_list_item(lst: List[int]) -> list:
    """
    Berilgan lst parametri ro'yxat qabul qiladi va uni elementlarini chop etadi
    :param lst: int turidagi elementlardan iborat list
    :return: list elementi
    """
    for item in lst:
        yield item

# my_list = [1,2,3,4,5]
# for i in view_list_item(my_list):
#     print(i, end=" ")


# 2.	Ro'yxatning uzunligini topuvchi dastur yozing.
def length_list(lst: List[str]) -> int:
    """
    Berilgan listni uzunligini aniqlovchi funksiya
    :param lst: str tipidagi elementlardan iborat list qabul qiladi
    :return: list uzunligini int formatida qaytaradi
    """
    return len(lst)

# my_list2 = ['python', 'js', 'react', 'django', 'DRF']
# print(length_list(my_list2))


# 3.	Ro'yxatga yangi element qo'shish uchun kod yozing.

my_list3 = []
def append_item_to_list(item:int) -> list:
    """
    funksiya yangi elementni my_list3 listga qo'shadi
    :param item: int tipidagi argument qabul qiluvchi parametr
    :return: yangi element qo'shilgan my_list3 ni qaytaradi
    """
    my_list3.append(item)
    return my_list3

# print(append_item_to_list(1)


# 4.	Ro'yxatdan elementni o'chirish uchun dastur yozing.
def remove_all_occurrences(lst: List, value) -> List:
    """
    Ro'yxatda barcha bir xil qiymatlarni o'chiradi
    :param lst:ro'yxat
    :param value:o'chirilishi kerak bo'lgan qiymat
    :return:yangilangan ro'yxat
    """

    return [item for item in lst if item != value]

# my_list4 = [1,2,3,4,3,6]
# print(remove_all_occurrences(my_list4, 3))


# 5.	Ro'yxatdagi barcha elementlarning yig'indisini hisoblang.

def sum_all_occurrences(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Berilgan ro'yxatning barcha elementlarini yig'indisini qaytaradi
    :param lst: ro'yxat
    :return: yig'indi
    """
    numeric_values = [item for item in lst if isinstance(item, (int, float))]
    return sum(numeric_values)

# my_list5 = [1,2,3,4,5,6,7,8,9, 'py']
# print(sum_all_occurrences(my_list5))


# 6.	Ro'yxatdagi eng katta va eng kichik elementlarni toping.
def max_and_min(lst: List[Union[int, float]]) -> str:
    """
    Berilgan ro'yxatda max va min qiymatlarni topuvchi funksiya
    :param lst: ro'yxat
    :return: max va min qiymatlar
    """

    if not lst:
        return "Ro'yxat bo'sh, qiymatlar topilmadi!"

    maximum = max(lst)
    minimum = min(lst)
    return f"Maximum: {maximum}; Minimum: {minimum}"

# my_list6 = list(range(1,20,3))
# print(my_list6)
# print(max_and_min(my_list6))



# 7.	Ro'yxatni teskari tartibda chop eting.
def reversed_list(lst: List[Union[int,float]]) -> Union[str, List[Union[int, float]]]:
    """
    Berilgan ro'yxatni teskari tartibda qaytaruvchi fubksiya
    :param lst: ro'yxat
    :return: teskari tartiblangan ro'yxat
    """
    if not lst:
        return "Bo'sh ro'yxat bilan amaliyot bajarish mumkin emas"
    reversed_lst = lst[::-1]
    return reversed_lst

# my_list7 = []
# my_list8 = list(range(1,10))
# print(reversed_list(my_list7))
# print(reversed_list(my_list8))


# 8.	Ro'yxatni o'sish tartibida saralang.

def growth_order_list(lst: List[Union[int, float]]) -> Union[str, List[Union[int, float]]]:
    """
    Berilgan ro'yxatni o'sish tartibida saralovchi funksiya
    :param lst: ro'yxat
    :return: saralangan ro'yxat
    """
    if not lst:
        return "Ro'yxat bo'sh, amaliyot bajarilmadi"

    sorted_list = sorted(lst)
    return sorted_list

# my_list9 = []
# my_list10 = [7,11,5,98,6,47,15,23,12,9]
# print(growth_order_list(my_list10))
# print(growth_order_list(my_list9))


# 9.	Ro'yxatni kamayish tartibida saralang.

def descending_order_list(lst: List[Union[int, float]]) -> Union[str, List[Union[int, float]]]:
    """
    Berilgan ro'yxatni kamayish tartibida saralovchi funksiya
    :param lst: ro'yxat
    :return: saralangan ro'yxat
    """

    if not lst:
        return "Ro'yxat bo'sh, amaliyot bajarilmadi!"

    sorted_list = sorted(lst, reverse=True)
    return sorted_list

# my_list11 = [1,5,7,8,11,4,45,6,98,75,64,23,2,10]
# print(descending_order_list(my_list11))


# 10.	Ro'yxatda berilgan qiymat necha marta takrorlanganini toping.
from collections import Counter

def count_all_occurrences(lst: List[Union[int, float]], value:Union[int, float]) -> Union[str, int]:
    """
    berilgan ro'yxat ichida value necha marta qatnashganini aniqlovchi funksiya
    :param lst: ro'yxat
    :param value: izlanayotgan qiymat
    :return: value soni
    """
    if not lst:
        return "Ro'yxat bo'sh"

    if value not in lst:
        return f"Ro'yxat ichida {value} elementi mavjud emas!"

    # 1 - usul list.count() metodi
    # result = lst.count(value)
    # return result

    # 2-usul: tez va samarali optimal va tavsiya qilinadi: collections.Counter()
    counter = Counter(lst)
    return counter[value]

# my_list12 = [1,2,3,6,7,8,9,10]
# my_list13 = []
# print(count_all_occurrences(my_list12, 11))
# print(count_all_occurrences(my_list12, 8))
# print(count_all_occurrences(my_list13, 1))


# 11.	Ikki ro'yxatni birlashtiruvchi dastur yozing.

def extend_lists(lst1, lst2):
    """
    Berilgan ikki ro'yxatni birlashtiruvchi funksiya
    :param lst1: ro'yxat
    :param lst2: ro'yxat
    :return: birlashgan ro'yxat
    """

    return lst1 + lst2

# my_list14 = [1,2]
# my_list15 = [3,5]
# print(extend_lists(my_list14, my_list15))




# 12.	Ro'yxatda takrorlangan elementlarni o'chirib tashlang.

def remove_all_item(lst: List[Union[int, float, str]], value: Union[int, float, str]) -> Union[str, List[Union[int, float, str]]]:
    """
    Berilgan ro'yxat ichidan barcha value ni o'chirib tashlaydigan funksiya
    :param lst: ro'yxat
    :param value: izlanayotgan qiymat
    :return: yangilangan ro'yxat
    """
    if not lst:
        return "Ro'yxat bo'sh, amaliyot topilmadi"

    if value not in lst:
        return f"Ro'yxat ichida {value} elementi topilmadi!"

    result = [item for item in lst if item != value]
    return result

# my_list16 = []
# my_list17 = [1,2,5,7,5,7,8,9,10,5,6,5]
# print(remove_all_item(my_list16, 1))
# print(remove_all_item(my_list17, 5))
# print(remove_all_item(my_list17, 17))





# 13.	Ro'yxatni slicing yordamida faqat bir qismini chiqaruvchi kod yozing.
def slicing_list(lst: List[Union[str, int, float]], idx1:int, idx2:int, ) -> Union[str, List[Union[str, int, float]]]:
    """
    Berilgan indexlar bo'yicha listdan ma'lumotlarni oladi
    :param lst: berilgan ro'yxat
    :param idx1: boshlang'ich nuqta uchun index1
    :param idx2: tugash nuqtasi uchun index2
    :return: ajratib olingan ma'lumotlarni ro'yxat qilib qaytaradi
    """
    if not lst:
        return "List bo'sh"

    result = lst[idx1:idx2+1]
    return result

# lst17 = list(range(0,100,3))
# print(slicing_list(lst17, 11, 28))

# 14.	Ro'yxatning barcha elementlarini kvadratga oshirib, yangi ro'yxatga saqlang.
def square_list(lst: List[Union[int, float]]) -> Union[str, List[Union[int, float]]]:
    """
    Berilgan ro'yxat elementlarini kvadratga oshirib yangi ro'yxat yaratuvchi funksiya
    :param lst: ro'yxat
    :return: yangi ro'yxat
    """
    if not lst:
        return "List bo'sh"

    try:
        result = [i ** 2 for i in lst]
    except TypeError:
        return "Ro'yxatda faqat raqam qatnashish kerak"

    return result

# lst18 = [1, 2,3,4,5,6,7,8,9,10]
# print(square_list(lst18))



# 15.	Juft indeksdagi elementlarni ajratib oling.

def pair_index_item(lst: List[Union[str, int, float]]) -> Union[str, List[Union[str, int, float]]]:
    """
    Berilgan ro'yxat tarkibidan faqat juft indexdagi qiymatlarni qaytaruvchi funksiya
    :param lst: berilgan ro'yxat
    :return: juft indexdagi qiymatlardan iborat ro'yxat
    """

    if not lst:
        return "Ro'yxat bo'sh"
    n = len(lst)
    result = [lst[i] for i in range(1, n) if i % 2 == 0]
    return result

# lst19 = ['py', 17, 25, True, False, 'Js', 25]
# print(pair_index_item(lst19))



# 16.	Ro'yxatdagi faqat juft sonlarni qaytaring.

def pair_number(lst: List[int]) -> Union[str, List[int]]:
    """
    Berilgan ro'yxatdan faqat juft qiymatlarni qaytaruvchi funksiya
    :param lst: ro'yxat
    :return: juft qiymatlardan iborat ro'yxat
    """

    if not lst:
        return "Ro'yxat bo'sh"

    result = []
    for i in lst:
        if isinstance(i, int) and i % 2 == 0:
            result.append(i)
        elif not isinstance(i, int):
            return "ro'yxatda faqat butun sonlardan foydalaning"

    return result

# lst20 = [1,2,3,4,56,8,11,17,25,30]
# print(pair_number(lst20))


# 17.	Ro'yxatdagi har bir elementni 2 ga bo'ling va natijani saqlang.

def bisection_item(lst: List[Union[int, float]]) -> Union[str, List[Union[int, float]]]:
    """
    Berilgan ro'yxatdagi barcha qiymatlarni ikkiga bo'luvchi funksiya
    :param lst: ro'yxat
    :return: yangi ro'yxat
    """

    if not lst:
        return "Ro'yxat bo'sh"

    result = [ i/2 for i in lst if isinstance(i, Union[int, float])]
    return result

# lst21 = [10,20,30]
# lst22 = [3.6,4.2,10.2,18,20]
# print(bisection_item(lst22))
# print(bisection_item(lst21))



# 18.	Ro'yxatni aylanma siljiting (masalan, birinchi element oxiriga o'tsin).
def revers_mylist(lst):
    """
    berilgan ro'yxatni elementlarini aylanma siljitish
    :param lst: ro'yxat
    :return: qaytarilgan ro'yxat
    """
    if not lst:
        return "List bo'sh"

    return lst[::-1]

# lst23 = [1,2,3,4]
# print(lst23[-1])
# print(revers_mylist(lst23))



# 19.	Faqat sonlardan iborat ro'yxatni saralang, matn elementlarini e'tiborsiz qoldiring.

def sorted_only_number(lst: List[Union[str, int, float]]) -> Union[str, List[Union[str, int, float]]]:
    """
    ro'yxatdagi faqat raqamlarni tartiblaydigan funksiya
    :param lst: ro'yxat
    :return: raqamlardan iborat tartiblangan ro'yxat
    """

    if not lst:
        return "Empty"

    result = sorted([i for i in lst if isinstance(i, int)])
    return result

# lst24 = ['py', 25, 'js', 10]
# print(sorted_only_number(lst24))



# 20.	Ikki ro'yxatning umumiy elementlarini topuvchi kod yozing.

def twins_list_items(lst: List[Union[str, int, float, bool]], lst2:List[Union[str, int, float, bool]])-> Union[str, List[Union[str, int, float, bool]]]:
    """
    ikki ro'yxatda bir xil elementlarni ajratib oluvchi funksiya
    :param lst: birinchi ro'yxat
    :param lst2: ikkinci ro'yxat
    :return: ikki ro'yxatda ham mavjud bo'lgan elementlar ro'yxati
    """

    if not lst and not lst2:
        return "Ikkala ro'yxat ham elementlarga ega bo'lishi kerak"

    set_lst1 = set(lst)
    set_lst2 = set(lst2)

    result = list(set_lst1 & set_lst2)
    return result

# lst24 = ['py', 'js', 25, 27, True]
# lst25 = ['py', 'js', 10, 30, True]
# print(twins_list_items(lst24, lst25))


# 23.	Ro'yxatdagi faqat string elementlarni yig'ib, ularni birlashtiring.
def string_elements(lst: List[Union[str, int, float, bool]]) -> str:
    """
    Berilgan ro'yxat tarkibidagi barcha stringlarni ajratib olib birlashtirish
    :param lst: ro'yxat
    :return: birlashgan string
    """

    if not lst:
        return "Ro'yxat bo'sh"

    result = [i for i in lst if isinstance(i, str)]
    return ''.join(result)

# lst26 = ['main', True, 17, '.py']
# print(string_elements(lst26))



# 24.	Berilgan ro'yxatdan palindrom so'zlarni ajratib oling.
def is_palindrome_str(lst: List[str]) -> Union[str, List[str]]:
    """
    ro'yxatdagi barcha palindrome qiymatlarni ajratib olish
    :param lst: ro'yxat
    :return: palindrome ro'yxat
    """

    if not lst:
        return  "Ro'yxat bo'sh"

    result = [i for i in lst if i == i[::-1]]
    return result

# lst27 = ['aziza', 'kiyik', 'py', 'js']
# print(is_palindrome_str(lst27))


# 25.	Faqat bir marta uchraydigan elementlarni ro'yxatga qaytaring.

def only_item(lst: List[Union[str, int, float, bool]]) -> Union[str, List[Union[str, int, float, bool]]]:
    """
    Berilgan ro'yxat tarkibida faqat bir marta qatnashgan elementlarni ajratib oluvchi funksiya
    :param lst: ro'yxat
    :return: ro'yxat
    """

    if not lst:
        return "Ro'yxat bo'sh"

    counter = Counter(lst)
    result = [el for el, freq in counter.items() if freq == 1]
    return result


# lst28 = ['py', 'js', 1,1,5,7,5,7,11]
# print(only_item(lst28))


# 28.	Ro'yxatdagi eng uzun stringni topuvchi dastur yozing.
def maximum_length_string(lst: List[str]) -> Union[str, None]:
    """
    Ro'yxatdagi eng uzun stringni topuvchi dastur
    :param lst: ro'yxat
    :return: maximum length string
    """

    if not lst:
        return None

    return max(lst, key=len)

# lst29 = ['py', 'python', 'pythonweb']
# print(maximum_length_string(lst29))



# 29.	Elementlari tuple bo'lgan ro'yxatdagi birinchi qiymatlar bo'yicha saralang.
def tuple_element_sorted(lst: List[tuple]) -> Union[List[tuple], None]:
    """
    Elementlari tuple bo'lgan ro'yxatdagi birinchi qiymatlar bo'yicha saralaydi
    :param lst: ro'yxat
    :return: saralangan ro'yxat
    """

    if not lst:
        return None

    result = sorted(lst, key=lambda x: x[0])
    return result

# lst30 = [(1, 'apple'), (3, 'py'), (2, 'js'), (0, 'drf')]
# print(tuple_element_sorted(lst30))


# 30.	Ro'yxatdagi barcha elementlar boshqa bir ro'yxat elementlariga bo'linadimi, tekshiring.

def are_elements_divisible(lst1: List[int], lst2: List[int]) -> bool:
    """
    lst1 dagi barcha elementlar lst2 dagi hech bo'lmaganda bitta elementga bo'linishini tekshiradi.
    :param lst1: Tekshiriladigan sonlar ro'yxati
    :param lst2: Bo'luvchilar ro'yxati
    :return: True agar barcha elementlar bo'linsa, aks holda False
    """
    if not lst1 or not lst2:  # Bo'sh ro'yxat bilan ishlash
        return False

    lst2 = [x for x in lst2 if x != 0]  # 0 bo'luvchilarni olib tashlash
    if not lst2:  # Agar faqat 0 lar bo'lsa, False qaytarish
        return False

    return all(any(num % divisor == 0 for divisor in lst2) for num in lst1)

# Test
print(are_elements_divisible([10, 20, 30], [2, 5]))  # True
print(are_elements_divisible([10, 15, 25], [3, 4]))  # False
print(are_elements_divisible([10, 20, 30], [0, 5]))  # True
print(are_elements_divisible([], [2, 5]))  # False
print(are_elements_divisible([10, 20, 30], []))  # False
print(are_elements_divisible([10, 20, 30], [0, 0, 0]))  # False

























































