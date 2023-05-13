import time
import random
import matplotlib.pyplot as plt

min_number = 1
max_number = 1000000

numbers_count = 1000000


def generate_numbers(n):
    with open("numbers.txt", "w") as f:
        for i in range(n):
            number = random.randint(min_number, max_number)
            num_digits = random.randint(1, 9)
            number_str = str(number)[:num_digits]
            f.write(number_str + '\n')


def read(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers


def pivot(numbers, l, r):
    v = numbers[r]
    i = l - 1
    j = r
    while i < j:
        while True:
            i = i + 1
            if numbers[i] >= v:
                break
        while True:
            j = j - 1
            if numbers[j] <= v:
                break
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i], numbers[r] = numbers[r], numbers[i]
    return i


def quick_sort(numbers, l, r):
    if l < r:
        q = pivot(numbers, l, r)
        quick_sort(numbers, l, q - 1)
        quick_sort(numbers, q + 1, r)
    return numbers


def merge(numbers, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = numbers[l + i]
    for j in range(0, n2):
        R[j] = numbers[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            numbers[k] = L[i]
            i += 1
        else:
            numbers[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        numbers[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        numbers[k] = R[j]
        j += 1
        k += 1


def merge_sort(numbers, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(numbers, l, m)
        merge_sort(numbers, m + 1, r)
        merge(numbers, l, m, r)


def selection_sort(numbers):
    n = len(numbers)
    for i in range(0, n - 1):
        k = i
        for j in range(i + 1, n):
            if numbers[k] > numbers[j]:
                k = j
        if k != i:
            numbers[i], numbers[k] = numbers[k], numbers[i]
    return numbers


def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        aux = numbers[i]
        j = i - 1
        while j >= 1 and aux < numbers[j]:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = aux
    return numbers


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def print_numbers(numbers):
    for number in numbers:
        print(number)


filename = "numbers.txt"

bubble_sum = 0
insertion_sum = 0
selection_sum = 0
merge_sum = 0
quick_sum = 0

avg_bubble = 0
avg_insertion = 0
avg_selection = 0
avg_merge = 0
avg_quick = 0

for i in range(0, 5):
    generate_numbers(numbers_count)
    numbers = read(filename)
    start_time = time.time()
    bubble_sort(numbers)
    end_time = time.time()
    bubble_sort_duration = (end_time - start_time) / 60
    bubble_sum += bubble_sort_duration
    print("Bubble sort time: ", bubble_sort_duration)

    numbers = read(filename)
    start_time = time.time()
    insertion_sort(numbers)
    end_time = time.time()
    insertion_sort_duration = (end_time - start_time) / 60
    insertion_sum += insertion_sort_duration
    print("Insertion sort time: ", insertion_sort_duration)

    numbers = read(filename)
    start_time = time.time()
    selection_sort(numbers)
    end_time = time.time()
    selection_sort_duration = (end_time - start_time) / 60
    selection_sum += selection_sort_duration
    print("Selection sort time: ", selection_sort_duration)

    numbers = read(filename)
    n = len(numbers)
    start_time = time.time()
    merge_sort(numbers, 0, n - 1)
    end_time = time.time()
    merge_sort_duration = (end_time - start_time) / 60
    merge_sum += merge_sort_duration
    print("Merge sort time: ", merge_sort_duration)

    numbers = read(filename)
    n = len(numbers)
    start_time = time.time()
    quick_sort(numbers, 0, n - 1)
    end_time = time.time()
    quick_sort_duration = (end_time - start_time) / 60
    quick_sum += quick_sort_duration
    print("Quick sort time: ", quick_sort_duration)
    
    print('\n')

avg_bubble = bubble_sum / 5
avg_insertion = insertion_sum / 5
avg_selection = selection_sum / 5
avg_merge = merge_sum / 5
avg_quick = quick_sum / 5

average = [avg_bubble, avg_insertion, avg_selection, avg_merge, avg_quick]
algorithms = ["Bubble sort", "Insertion sort", "Selection sort", "Merge sort", "Quick sort"]
positions = range(len(average))

plt.bar(positions, average)
plt.xticks(positions, algorithms)
plt.xlabel("Algorithms")
plt.ylabel("Time (min)")
plt.show()