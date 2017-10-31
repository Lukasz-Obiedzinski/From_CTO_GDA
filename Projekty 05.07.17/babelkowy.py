__title__='sortowanie babelkowe'

import random


data=random.sample(range(10000),1000)


def sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

sort(data)
print(data)
