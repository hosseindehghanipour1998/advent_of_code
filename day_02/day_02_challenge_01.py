
#########################################
#                                       #
#           Simplified Code             #
#                                       #
#########################################

# def is_sorted(lst):
#     asc = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
#     desc = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
#     return asc or desc

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# print(is_sorted(my_list))  # True


# l = [
#     [7, 6, 4, 2, 1], 
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
#     ]
# safe = 0
# count = True
# for j in range(len(l)):
#     row = l[j]
#     if is_sorted(row):
#         for i in range(len(row)-1):
#             diff = abs(row[i]-row[i+1])
#             if diff < 1 or diff>3:
#                 count = False
#                 break
#         if count:
#             safe +=1
#         count = True
        
            

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