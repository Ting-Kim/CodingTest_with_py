# Problem 1095
# 퀵 정렬
def partition(arr, start, end):
    pivot = arr[(start+end)//2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while pivot < arr[end]:
            end -= 1
        if start <= end:
            swap(arr,start,end)
            start += 1
            end -= 1

    return start


def quick(arr,start,end):
    part = partition(arr,start,end)     # 우측 start 인덱스
    if start < part - 1:
        quick(arr, start, part-1)

    if part < end:      # 여기! @@@@@@@
        quick(arr, part, end)

def swap(arr, start, end):
    #  구현 필요./
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


n = int(input())
arr = list(map(int,input().split()))

quick(arr,0, len(arr)-1)

print(arr[0])



'''
    if end - start < 1:
        return

    part = (end-start)//2
    pivot = arr[part]

    while start <= end:

        while arr[start] <= pivot:
            if start >= end:
                break
            start += 1
        while arr[end] >= pivot:
            if end <= start:
                break
            end -= 1

        if start <= end:
            swap(arr, start, end)
            start += 1
            end -= 1

    quick(arr, 0, start-1)
    quick(arr, start, len(arr)-1)
    return
'''
