my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
# This is a shallow copy, mutations in str 2 will affect str 1
my_list2[0]['first'] = 42
print(my_list1)

# What will the following code output?

# It will print: [{"first": 42}, {"second": "value2"}, 3, 4, 5]

print(my_list1[0] is my_list2[0])