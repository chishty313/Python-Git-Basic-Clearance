def sum_all(*args):
    sum_manual = 0
    for i in args:
        sum_manual += i
    sum_auto = sum(args)
    return sum_manual, sum_auto
sum_manual, sum_auto = sum_all(1, 2, 3)
print('Summation manually in Python:', sum_manual)
print('Summation using built in method in Python:', sum_auto)