def MaxPairwiseProduct(n, a, c):
    for i in range(0, n):
        for j in range(1, n):
            if a[i] != a[j]:
                m = a[i] * a[j]
                c.append(m)

            else:
                continue

    Product1 = max(c)
    return Product1


def MaxPairwiseProductFast(n, a):
    max_index1 = -1
    for i in range(0, n):
        if a[i] > a[max_index1]:
            max_index1 = i
        else:
            continue
    # the value of the other index should be different compared to the        #first, else it will assume the same
    # indices for both the max
    max_index2 = -2
    for j in range(0, n):
        if a[j] > a[max_index2] and a[j] != a[max_index1]:
            max_index2 = j
        else:
            continue

    Product2 = a[max_index1] * a[max_index2]
    return Product2


n = int(input("Enter the number of elements in the array (2-200,000):"))
a = [int(x) for x in
     input("Enter all numbers of the sequence with only non-negative intergers not exceeding 100,000:").split()]
c = list()

print('The max value by regular algorithm:', MaxPairwiseProduct(n, a, c))
print('The max value by faster algorithm:', MaxPairwiseProductFast(n, a))
