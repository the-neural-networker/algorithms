def binary_search(lst, item):
    low = 0 
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess < item:
            low = mid + 1 
        elif guess > item: 
            high = mid - 1
        else:
            return mid 

    return None 

if __name__ == "__main__":
    array = list(input("Enter your array of elements: "))
    item = int(input("Enter the item you wanna find from the list: ")) 
    print(binary_search(sorted(array), item))
