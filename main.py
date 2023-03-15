import os

with open('1.txt', 'r', encoding='utf-8') as file1:
    name1 = '1.txt'
    i1 = 0
    line1_list = []
    for line1 in file1:
        line1_list.append(line1)
        i1 += 1
with open('2.txt', 'r', encoding='utf-8') as file2:
    name2 = os.path.basename('2.txt')
    i2 = 0
    line2_list = []
    for line2 in file2:
        line2_list.append(line2)
        i2 += 1
with open('3.txt', 'r', encoding='utf-8') as file3:
    name3 = os.path.basename('3.txt')
    i3 = 0
    line3_list = []
    for line3 in file3:
        line3_list.append(line3)
        i3 += 1
new_file = open('new_file.txt', 'w')
if i2 < i1 > i3 and i2 > i3:
    new_file.write(name3 + '\n')
    new_file.write(str(i3) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
elif i2 < i1 > i3 and i2 < i3:
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
    new_file.write(name3 + '\n')
    new_file.write(str(i3) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
elif i2 > i1 > i3:
    new_file.write(name3 + '\n')
    new_file.write(str(i3) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
elif i2 > i1 < i3 and i2 > i3:
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
    new_file.write(name3 + '\n')
    new_file.write(str(i3) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
elif i2 > i1 < i3 and i2 < i3:
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')
elif i2 < i1 < i3:
    new_file.write(name2 + '\n')
    new_file.write(str(i2) + '\n')
    new_file.writelines(line2_list)
    new_file.write('\n')
    new_file.write(name1 + '\n')
    new_file.write(str(i1) + '\n')
    new_file.writelines(line1_list)
    new_file.write('\n')
    new_file.write(name3 + '\n')
    new_file.write(str(i3) + '\n')
    new_file.writelines(line3_list)
    new_file.write('\n')



