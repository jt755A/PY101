def add_element(my_list):
    # my_list.append([4])
    my_list = my_list + [4]
    # my_list += [4]
    print(f'local my_list = {my_list}')


my_list = [1, 2, 3]
add_element(my_list)
print(my_list)