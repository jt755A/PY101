def add_element(my_list):
    my_list = my_list + [4]
    print(my_list); print(id(my_list))
    

my_list = [1, 2, 3]
add_element(my_list)
print(my_list); print(id(my_list))