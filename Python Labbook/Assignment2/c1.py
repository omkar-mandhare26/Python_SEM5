def binarySearch(list,n):
    LB = 0
    UB = len(list) - 1

    for i in range(len(list)):
        mid = int((LB + UB) / 2)
        
        if list[mid] == n:
            return mid
        elif list[mid] > n: LB = mid + 1
        elif list[mid] > n: UB = mid - 1

    return None

list = [4,8,14,17,20,94]
n = 1
index = binarySearch(list,n)

if index:
    print(f"Index: {index}")
else:
    print("Number not found")