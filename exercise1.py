def sum_of_odd_numbers(lst):
    sum = 0
    for i in lst:
        if i%2 != 0:
            sum +=i
    return sum



my_list = [2, 5, 9]
print(sum_of_odd_numbers(my_list))


