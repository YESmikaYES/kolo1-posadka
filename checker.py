mine = open('./output.txt')
mine = mine.read()
mine = mine.split("\n")
mine.pop()


diffs = []
with open('./posadka_vystup.txt') as correct:
    i = 1
    for line in mine:
        cline = correct.readline()
        if line == cline.strip():
            # print(f"{i} correct")
            pass
        else:
            diffs.append(i-1)
            # print(f"{i} incorrect: mine:\"{line}\" vs correct:\"{cline.strip()}\"")
        i += 1

print(diffs)


# in_data = open('./posadka_vstup.txt')
# open('./posadka_vstup(only_the_bad_ones).txt', "w").close()



# t = int(in_data.readline())
# if type(t) != int or t < 1 or t > 1000:
#     open("./posadka_vstup(only_the_bad_ones).txt", "x")
#     exit()


# data_list : list[list] = []
# for i in range(t):
#     data_list.append([])

# in_data = in_data.read()
# in_data = in_data.split("\n")
# in_data.pop()

# data_list_index = -1
# line_counter = 0
# for i in range(len(in_data)):
#     if line_counter == 3:
#         line_counter = 0
#     cur_line = in_data[i].split(" ")
#     if line_counter == 0:
#         data_list_index += 1
#         for j in range(len(cur_line)):
#             if type(int(cur_line[j])) != int or int(cur_line[j]) < -1 or int(cur_line[j]) > 10**18:
#                 open("./output.txt", "x")
#                 exit()
#             cur_line[j] = int(cur_line[j])
#         data_list[data_list_index].append(cur_line)
#     else:
#         for j in range(len(cur_line)):
#             if type(int(cur_line[j])) != int or int(cur_line[j]) < -1 or int(cur_line[j]) > 10**18:
#                 open("./output.txt", "x")
#                 exit()
#             cur_line[j] = int(cur_line[j])
#         data_list[data_list_index].append(cur_line)
#     line_counter += 1

# for i in range(len(data_list)):
#     if i not in diffs:
#         data_list.pop(i)

# print(data_list)