

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    return len(arr1) == len(arr2) and arr2 in arr1 + arr1
