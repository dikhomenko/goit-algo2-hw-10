import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [
        x for i, x in enumerate(arr) if x < pivot or (x == pivot and i != pivot_index)
    ]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # mid
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr.copy())
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    random_times = []
    deterministic_times = []

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        rand_total = 0
        det_total = 0
        for _ in range(5):
            rand_total += measure_time(randomized_quick_sort, arr)
            det_total += measure_time(deterministic_quick_sort, arr)
        rand_avg = rand_total / 5
        det_avg = det_total / 5
        random_times.append(rand_avg)
        deterministic_times.append(det_avg)
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_avg:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_avg:.4f} секунд\n")

    plt.figure(figsize=(8, 6))
    plt.plot(sizes, random_times, label="Рандомізований QuickSort")
    plt.plot(sizes, deterministic_times, label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.tight_layout()
    plt.show()

    print("Висновок:")
    print(
        "Рандомізований QuickSort зазвичай працює швидше на великих масивах, оскільки випадковий вибір опорного елемента зменшує ймовірність найгіршого випадку (O(n^2))."
    )
    print(
        "Детермінований QuickSort може працювати повільніше на вже відсортованих або майже відсортованих даних через неефективний вибір опорного елемента."
    )
