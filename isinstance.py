# isinstance() - metodi moslikni tekshiradi
import sys
import gc
# isinstance(object, classinfo)

x = 17
# print(isinstance(x, int))
# print(isinstance(x, str))

y = "python"
# print(isinstance(y, str))
# print(isinstance(y, (int, str, list, set, tuple)))

z = [1,2,3]
# print(isinstance(z, (list, set, dict, tuple)))
# print(isinstance(z, str))

class Programmer:
    def __init__(self, name, job):
        self.name = name
        self.job = job


# developer = Programmer("Sherzod", "Web_developer")
# print(isinstance(developer, Programmer))

# Murakkab obyektlarning xotira hajmini aniqlash
def deep_getsizeof(obj):
    size = sys.getsizeof(obj)
    if isinstance(obj, (list, tuple, set, dict)):
        size += sum(deep_getsizeof(i) for i in obj)
    elif isinstance(obj, dict):
        size += sum(deep_getsizeof(k) + deep_getsizeof(v) for k,v in obj.items())
    return size

data = [1, [2,3], {'a':5}]
print(deep_getsizeof((data)))

gc.collect()
print(gc.isenabled())




































