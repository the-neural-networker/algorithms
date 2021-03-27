def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        low = 0
        high = len(arr) - 1
        mid = (low + high) // 2
        pivot = arr[mid]
        left = [el for el in arr[:mid] + arr[mid + 1:] if el <= pivot] 
        right = [el for el in arr[:mid] + arr[mid + 1:] if el > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    arr = [55, 23, 5, 46, 33, 55, 65]
    print(quick_sort(arr))