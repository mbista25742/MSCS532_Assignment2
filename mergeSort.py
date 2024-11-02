import time
import random
import tracemalloc

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

def main():
    #random
    # dataset = [
    #     34, 67, 23, 89, 12, 45, 78, 90, 56, 11,
    #     24, 85, 36, 62, 44, 53, 77, 2, 19, 47,
    #     81, 88, 3, 69, 14, 27, 59, 70, 39, 22,
    #     92, 48, 31, 74, 60, 8, 50, 35, 76, 18,
    #     33, 65, 94, 5, 17, 71, 10, 4, 73, 30,
    #     16, 25, 84, 64, 87, 29, 1, 40, 54, 91,
    #     15, 66, 83, 72, 26, 41, 32, 58, 57, 75,
    #     37, 49, 79, 13, 86, 99, 20, 100, 9, 38,
    #     52, 61, 80, 63, 46, 42, 93, 68, 95, 14,
    #     96, 97, 98, 43, 72, 55, 88, 6, 7, 82
    # ]

    #sorted
    # dataset  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    #reverse sorted
    dataset =  [
    100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 88, 87, 86, 85, 84,
    83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 72, 71, 70, 69, 68, 67,
    66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 50, 49, 48,
    47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30,
    29, 27, 26, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15, 14, 14, 13, 12, 11,
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1
]

    # Measure execution time and memory usage
    tracemalloc.start()
    start_time = time.perf_counter()
    sorted_array = merge_sort(dataset.copy())  # Store the sorted array
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Output the performance metrics
    execution_time = end_time - start_time
    memory_usage = peak / 1024  # Convert to KB
    print(f"Merge Sort - Execution Time: {execution_time:.5f}s, Memory Usage: {memory_usage:.2f}KB")
    print(f"Sorted Array - {sorted_array}")  # Print the sorted array

if __name__ == "__main__":
    main()
