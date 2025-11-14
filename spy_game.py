def spy_game(my_list):
    for i in range(len(my_list)-2):
        if my_list[i] == 0 and my_list[i + 1] == 0 and my_list[i+2] == 7:
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
