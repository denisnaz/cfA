#with open("input.txt") as f:
#nums = f.read().splitlines()
count = input()
nums = input()
objects, classes, parts = map(int, count.split(' '))
data = list(map(int, nums.split(' ')))
parts_list = [[] for part in range (parts)]
parts_num = 0
for i_classes in range (classes):
    for i_objects in range(objects):
        if data[i_objects] == i_classes + 1:
            parts_list[parts_num].append(i_objects+1)
            parts_num = (parts_num + 1) % parts

for part in parts_list:
    print(len(part), *part)
