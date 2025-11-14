def has_33(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] == 3 and my_list[i+1] == 3:
            return True
    else:
        return False


print(has_33([3, 1, 2, 4, 3]))
