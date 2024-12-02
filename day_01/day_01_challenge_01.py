content = open("./input.txt").readlines()
left, right = sorted([int(i.split(" ")[0]) for i in content]), sorted([int((i.split(" ")[-1]).replace("\n",'')) for i in content])
print(sum([abs(right[i]-left[i]) for i in range(len(right))]))



