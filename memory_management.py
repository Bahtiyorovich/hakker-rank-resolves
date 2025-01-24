import sys
# Referenc countni tekshirish

a = [1,2,3]
print(sys.getrefcount(a))
number_lst = [1,2,3,4,5]

print(sys.getrefcount(number_lst))

number_lst_copy = number_lst
print(sys.getrefcount(number_lst))

del number_lst_copy
print(sys.getrefcount(number_lst))

# Garbage collection
import gc

# garbage collectionni o'chirish
# gc.disable()

# garbage collectionni yoqish
# gc.enable()

# garbage collectionni yoqilganligini tekshirish
# print(gc.isenabled())


# garbage collectionni majburiy chaqirish
# gc.collect()
# print(gc.isenabled())


class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

node1 = Node('Node1')
node2 = Node('Node2')

node1.ref = node2
node2.ref = node1

del node1
del node2

gc.collect()


# is va == ning farqi

# ikki obyektning xotira manzili bir xilligini tekshiradi
# id() metodi bu jarayonni tekshiradi

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b) # True
print(a is c) # False

# == operatori obyektlarning qiymatlarini taqqoslaydi

print(a == c) # True
print(a is c) # False






























































