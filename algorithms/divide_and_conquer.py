def sum_array(arr):
    """Find the sum of elements of an array using the divide and conquer technique."""
    if arr == []:
        return 0

    return arr[0] + sum_array(arr[1:])

def count_array(arr):
    """Count the number of elements in an array using the divide and conquer technique."""
    if arr == []:
        return 0

    return 1 + count_array(arr[1:])

def max_array(arr):
    """Returns the maximum value in an array using the divide and conquer technique."""
    if len(arr) == 1:
        return arr[0]

    if arr[0] > max_array(arr[1:]):
        return arr[0]
    else:
        return max_array(arr[1:])

def binary_search(arr, item):
    """Searches and return index for item in the array using the divide and conquer technique."""
    low = 0 
    high = len(arr) - 1
    mid = (low + high) // 2

    if len(arr) == 1 and arr[0] == item:
        return 0
    elif len(arr) == 1 and arr[0] != item:
        return None

    if arr[mid] == item:
        return mid 
    elif arr[mid] > item:
        return binary_search(arr[:mid], item)
    elif arr[mid] < item:
        if binary_search(arr[mid + 1:], item) is None:
            return binary_search(arr[mid + 1:], item)
        return mid + 1 + binary_search(arr[mid + 1:], item)

if __name__ == "__main__":
    arr = [25, 1, 3, 35, 5, 6, 8]
    print(sum_array(arr))
    print(count_array(arr))
    print(max_array(arr))
    print(sorted(arr))
    print(binary_search(sorted(arr), 25))