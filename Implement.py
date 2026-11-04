def insertion_sort(arr):

    a = list(arr)
    comparisons = 0
    shifts = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1


        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons, shifts


if __name__ == "__main__":
    print(insertion_sort([4, 3, 2, 1]))
    print(insertion_sort([1, 2, 3, 4]))