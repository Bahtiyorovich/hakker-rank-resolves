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
























