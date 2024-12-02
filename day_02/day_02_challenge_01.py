
#########################################
#                                       #
#           Do you like Spaghetti?      #
#                                       #
#########################################

# Part 0: Read the File
# [[int(number) for number in item.split(" ")] for item in [row.strip() for row in open("input_01.txt", "r").readlines()]]

# Part 1: Check if they exceed the limit of 1 & 3
# map(lambda lst: all([bool(diff >= 1 and diff <= 3) for i in range(len(lst) - 1) if(diff := abs(lst[i]-lst[i+1]))])) 

# Part 2: Check if the list either asc or desc
# list(filter(lambda lst: all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all((lst[i] >= lst[i+1]) for i in range(len(lst)-1)), list_of_levels))

# part4: Combine
print(sum(list(map(lambda lst: all([bool(diff >= 1 and diff <= 3) for i in range(len(lst) - 1) if(diff := abs(lst[i]-lst[i+1]))]),
list(filter(lambda lst: all(lst[i] < lst[i+1] for i in range(len(lst)-1)) or all((lst[i] > lst[i+1]) for i in range(len(lst)-1)), [[int(number) for number in item.split(" ")] for item in [row.strip() for row in open("input_02.txt", "r").readlines()]]))))))