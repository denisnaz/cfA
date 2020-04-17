#with open("input.txt") as f:
#nums = f.read().splitlines()
count = input()
nums = input()
objects, classes, parts = map(int, count.split(' '))
data = list(map(int, nums.split(' ')))
parts_list = [[] for part in range (parts)]
classes_list = [0 for class1 in range (classes)]
parts_classes_list = [0 for class2 in range (classes)]
for i in range (objects):
    classes_list[data[i]-1] += 1
for j in range (classes):
    if j == 0:
       parts_classes_list[0] = 0
    else:
        parts_classes_list[j] = (parts_classes_list[j-1] + classes_list[j-1]) % parts
for i_objects in range(objects):
    parts_list[parts_classes_list[data[i_objects]-1]].append(i_objects+1)
    parts_classes_list[data[i_objects]-1] = (parts_classes_list[data[i_objects]-1] + 1) % parts

for part in parts_list:
    print(len(part), *part)
