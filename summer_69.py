def summer_69(my_list):
    skip = False
    sum = 0
    for num in my_list:
        if num == 6:
            skip = True
        elif skip and num == 9:
            skip = False
        elif not skip:
            sum = sum + num

    return sum


print(summer_69([1, 3, 6, 7, 9]))
