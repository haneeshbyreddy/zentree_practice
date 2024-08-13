import time

arr = [1,4,6,7,2,4,6,9,7,1,1,6,7,3,5,5,8]
length = len(arr)
sorted_arr = sorted(arr)
print('Input array :', arr)
print('Sorted array :', sorted_arr)

class timelapse:
    def start(this):
        this.start_time = time.time()
    def stop(this):
        this.end_time = time.time()
        return round(this.end_time - this.start_time, 6)

# selection_sort, time complexity : O(n^2)
def selection_sort(arr, length):
    selection_arr = arr.copy()
    for i in range(length):
        mini = i
        for j in range(i, length):
            mini = j if selection_arr[j] < selection_arr[mini] else mini
        selection_arr[i], selection_arr[mini] = selection_arr[mini], selection_arr[i]
    return selection_arr

# bubble sort, time complexity : O(n^2)
def bubble_sort(arr, length):
    bubble_arr = arr.copy()
    for i in range(length):
        bubble_sorted = True
        for j in range(0,length-1-i):
            if bubble_arr[j] > bubble_arr[j+1]:
                bubble_arr[j], bubble_arr[j+1] = bubble_arr[j+1], bubble_arr[j]
                bubble_sorted = False
        if bubble_sorted:
            break
    return bubble_arr

# insertion sort, time complexity : O(n^2)
def insertion_sort(arr, length):
    insertion_arr = arr.copy()
    for i in range(length):
        j = i
        curr = insertion_arr[i]
        while j>0 and insertion_arr[j-1] > curr:
            insertion_arr[j] = insertion_arr[j-1]
            j -= 1
        insertion_arr[j] = curr
    return insertion_arr

# merge sort, time complexity : 
def merge_sort(merge_arr):
    length = len(merge_arr)
    if length <= 1:
        return merge_arr
    mid = length // 2
    left = merge_sort(merge_arr[:mid])
    right = merge_sort(merge_arr[mid:])
    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# quick sort, time complexity :
def quick_sort(quick_arr):
    length = len(quick_arr)
    if length <= 1:
        return quick_arr
    left, right = [], []
    for i in range(length-1):
        if quick_arr[i] < quick_arr[-1]:
            left.append(quick_arr[i])
        else:
            right.append(quick_arr[i])
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [quick_arr[-1]] + right

# heap sort, time complexity :
def heap_sort(heap_arr):
    sorted_arr = []
    while len(heap_arr) > 0:
        # heapify
        for i in range(len(heap_arr) // 2 - 1, -1, -1):
            l = (2*i) + 1
            r = (2*i) + 2
            maxi = i
            if l<len(heap_arr) and heap_arr[l] > heap_arr[maxi]:
                maxi = l
            if r<len(heap_arr) and heap_arr[r] > heap_arr[maxi]:
                maxi = r
            heap_arr[i], heap_arr[maxi] = heap_arr[maxi], heap_arr[i]
        heap_arr[0], heap_arr[-1] = heap_arr[-1], heap_arr[0]
        sorted_arr.insert(0, heap_arr.pop())
    return sorted_arr

t1 = timelapse()
t1.start()
print("Selection sort :", selection_sort(arr, length) if not (selection_sort(arr, length) == sorted_arr) else t1.stop())
t1.start()
print("Bubble sort :", bubble_sort(arr, length) if not (bubble_sort(arr, length) == sorted_arr) else t1.stop())
t1.start()
print("Insertion sort :", insertion_sort(arr, length) if not (insertion_sort(arr, length) == sorted_arr) else t1.stop())
t1.start()
print("Merge sort :", merge_sort(arr.copy()) if not (merge_sort(arr.copy()) == sorted_arr) else t1.stop())
t1.start()
print("Quick sort :", quick_sort(arr.copy()) if not (quick_sort(arr.copy()) == sorted_arr) else t1.stop())
t1.start()
print("Heap sort :", heap_sort(arr.copy()) if not (heap_sort(arr.copy()) == sorted_arr) else t1.stop())