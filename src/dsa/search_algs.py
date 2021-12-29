def binary_search(arr, target):
    """
    Returns index of target in a sorted array. 
    If target not in arr, returns -1
    """
    low, high = 0, len(arr) - 1
 
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    
    return -1