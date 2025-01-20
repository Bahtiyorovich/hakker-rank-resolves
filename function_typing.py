# Type

from typing import Union, List
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grades: List[int]

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

student = Student(name="Ali", grades=[85, 90, 86])
print(f"{student.name}ning o'rtacha baxosi: {student.average_grade()}")

def calculate_total(price: Union[int, float], quantity: int) -> float:
    """
        :param price: type int va float bo'lgan argumentlarni qabul qiladi
        :param quantity: type int bo'lgan argumentlarni qabul qiladi
        :return: natija float tipida qaytariladi
    """
    return price * quantity

# print(calculate_total(7.5, 5))
# print(calculate_total(2, 3))




