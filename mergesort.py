import time


def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data)-1, drawData, timeTick)


def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):

    drawData(data, colorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    n1 = middle - left+1
    n2 = right-middle

    L = [0]*(n1)
    R = [0]*(n2)

    for i in range(0, n1):
        L[i] = data[left+i]

    for j in range(0, n2):
        R[j] = data[middle+1+j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1

    drawData(data, ["green" if x >= left and x <=
             right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def colorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")

    return colorArray
