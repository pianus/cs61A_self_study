def multiply1(m,n):
    if m == 0:
        return 0
    elif m > 0:
        return n + multiply1(m-1,n)

def count_down(n):
    if n >= 1:
        count_down(n-1)
        print(n)

# 2.4
def sum_digits(n):
    if n < 10:
        return n
    elif n >= 10:

        all_but_last, last = n // 10, n % 10
        return last + sum_digits(all_but_last)

# 3.1
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n > 0:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n,k):
    if n == 0:
        return 1
    elif n <0:
        return 0
    elif n > 0:
        total = 0
        current = k
        while current > 0:
            total += count_k(n-current,k)
            current -= 1
        return total
