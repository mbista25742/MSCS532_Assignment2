import time
import random
import tracemalloc

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
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

# Function to create datasets
def create_datasets():
    sorted_array = list(range(1, 1001))  # Sorted array
    reverse_sorted_array = list(range(1000, 0, -1))  # Reverse sorted array
    random_array = random.sample(range(1, 1001), 1000)  # Random array
    return sorted_array, reverse_sorted_array, random_array

# Function to measure execution time and memory usage
def measure_sorting(sorting_function, dataset):
    tracemalloc.start()
    start_time = time.perf_counter()
    sorting_function(dataset.copy())
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024  # Convert to KB

def main():
    sorted_array, reverse_sorted_array, random_array = create_datasets()

    datasets = {
        "Sorted Array": sorted_array,
        "Reverse Sorted Array": reverse_sorted_array,
        "Random Array": random_array
    }

    for name, dataset in datasets.items():
        print(f"Dataset: {name}")
        
        # Measure Quick Sort performance
        quick_sort_time, quick_sort_memory = measure_sorting(quick_sort, dataset)
        print(f"Quick Sort - Time: {quick_sort_time:.5f}s, Memory: {quick_sort_memory:.2f}KB")
        
        # Measure Merge Sort performance
        merge_sort_time, merge_sort_memory = measure_sorting(merge_sort, dataset)
        print(f"Merge Sort - Time: {merge_sort_time:.5f}s, Memory: {merge_sort_memory:.2f}KB")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
