mine = open('./output.txt')
mine = mine.read()
mine = mine.split("\n")
mine.pop()

# open("./posadka_vystup(correct_solution_to_bad_ones).txt","w").close()

diffs = []
with open('./posadka_vystup(correct_solution_to_bad_ones).txt') as correct:
    i = 1
    for line in mine:
        cline = correct.readline()
        if line == cline.strip():
            # print(f"{i} correct")
            pass
        else:
            # diffs.append(i-1)
            # open("./posadka_vystup(correct_solution_to_bad_ones).txt","a").write(cline)
            # print(f"{i} incorrect: mine:\"{line}\" vs correct:\"{cline.strip()}\"")
            pass
        i += 1

exit()
print(diffs)


in_data = open('./posadka_vstup.txt')
open('./posadka_vstup(only_the_bad_ones).txt', "w").close()



t = int(in_data.readline())
if type(t) != int or t < 1 or t > 1000:
    open("./posadka_vstup(only_the_bad_ones).txt", "x")
    exit()


data_list : list[list] = []
for i in range(t):
    data_list.append([])

in_data = in_data.read()
in_data = in_data.split("\n")
in_data.pop()

data_list_index = -1
line_counter = 0
out_data = f"{len(diffs)}\n"
for i in range(len(in_data)):
    if line_counter == 3:
        line_counter = 0
        
    if line_counter == 0:
        data_list_index += 1
        if data_list_index in diffs:
            out_data = out_data + f"{in_data[i]}\n"
    else:
        if data_list_index in diffs:
            out_data = out_data + f"{in_data[i]}\n"

    line_counter += 1

# print(out_data)
open('./posadka_vstup(only_the_bad_ones).txt', "a").write(out_data)