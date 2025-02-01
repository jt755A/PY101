dictionary = {'first': [1]}
num_list = dictionary['first']
# num_list shares pointer with dictionary to [1]
num_list.append(2)
# mutates object at dictionary['first']

# num_list == [1], 2
# dictionary == {'first': [1], 2}


print(num_list)
# num_list = [1], 2

print(dictionary)

# What does the last line in the following code output?

#  {'first': [1], 2}


# Edit, not quite... 
# line 4 appends 2 INTO the list: so [1, 2]