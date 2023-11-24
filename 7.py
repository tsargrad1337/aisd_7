import itertools
import copy
from random import randint

class ArrayVariants:
    def __init__(self, n):
        self.n = n
        self.array = [0] * n

    def generate_array(self): # метод для генерации случайных величин для массива
        for i in range(self.n):
            self.array[i] = randint(-10, 10)

    def get_best_variant(self, max_sum): # метод для нахождения варианта, удовлетворяющего ограничению
        if max_sum < sum(x for x in self.array if x < 0):
            raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")
        
        variants = []
        indices = [i for i in range(1, len(self.array), 2) if self.array[i] > 0]
        
        for i in range(len(indices) + 1):
            for combination in itertools.combinations(indices, i):
                variant = copy.deepcopy(self.array)
                for index in combination:
                    variant[index] = 0
                print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")  # выводим каждый вариант перед проверкой
                if sum(variant) <= max_sum:
                    variants.append(variant)
        
        best_variant = max(variants[::-1], key=sum)
        return best_variant

n = randint(0, 10)
print(n, "- количество элементов массива")
max_sum = randint(0, 30)
print(max_sum, "- максимальная сумма")

array_variants = ArrayVariants(n)
array_variants.generate_array()

best_variant = array_variants.get_best_variant(max_sum)
print(best_variant, '- вариант с максимальной суммой')
