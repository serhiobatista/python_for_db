first_class = [num for num in range(160, 173, 2)]
second_class = [num for num in range(162, 181, 3)]
first_class.extend(second_class)
class_united = sorted(first_class)
print(first_class)