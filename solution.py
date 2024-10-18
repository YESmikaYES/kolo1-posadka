in_data = open("./posadka_vstup(only_the_bad_ones).txt")
open('./output.txt', "w").close()



t = int(in_data.readline())
if type(t) != int or t < 1 or t > 1000:
    open("output.txt", "x")
    exit()


data_list : list[list] = []
for i in range(t):
    data_list.append([])

in_data = in_data.read()
in_data = in_data.split("\n")
in_data.pop()

data_list_index = -1
line_counter = 0
for i in range(len(in_data)):
    if line_counter == 3:
        line_counter = 0
    cur_line = in_data[i].split(" ")
    if line_counter == 0:
        data_list_index += 1
        for j in range(len(cur_line)):
            if type(int(cur_line[j])) != int or int(cur_line[j]) < -1 or int(cur_line[j]) > 10**18:
                open("./output.txt", "x")
                exit()
            cur_line[j] = int(cur_line[j])
        data_list[data_list_index].append(cur_line)
    else:
        for j in range(len(cur_line)):
            if type(int(cur_line[j])) != int or int(cur_line[j]) < -1 or int(cur_line[j]) > 10**18:
                open("./output.txt", "x")
                exit()
            cur_line[j] = int(cur_line[j])
        data_list[data_list_index].append(cur_line)
    line_counter += 1

output_text = ""

for crew in data_list:
    n = crew[0][0]
    if type(n) != int or n < 1 or n > 2*(10**14):
        break
    k = crew[0][1]
    if type(k) != int or k < 0 or k > 10**18:
        break
    crew.pop(0)
    # current_crew = {}
    # for i in range(len(crew[0])):
    #     cur_member = f"member-{i+1}"
    #     if crew[1][i] == -1:
    #         current_crew[cur_member] = ["captain", crew[0][i]]
    #     else:    
    #         current_crew[cur_member] = [f"member-{crew[1][i]}", crew[0][i]]
    current_member = 0
    ajajaj = False
    while k > 0:
        if current_member >= len(crew[0]):
            # for i in range(len(crew[0])):
            #     competence = crew[0][i]
            #     if competence <= lowest_competence:
            #         lowest_competence = competence
            #         lowest_competence_index = i
            
        
            lowest_competence_index = crew[0].index(min(crew[0]))

            if k <= 0:
                f = open("./output.txt", "a")
                f.write(f"ajajaj\n")
                f.close() 
                ajajaj = True
                print(crew[0])
                print(crew[1])
                print("ajajaj")
                break
            
            malleable_competences = []
            for competence in crew[0]:
                malleable_competences.append(competence)

            while True:
                if crew[1][lowest_competence_index] == -1:
                    break                
                elif crew[0][lowest_competence_index] + 1 < crew[0][crew[1][lowest_competence_index]-1]:
                    print(crew[0])
                    mins = [[],[],[]]
                    current_min = min(malleable_competences)
                    print("starting loop of multi-eligible-minimums")
                    for competence in malleable_competences:
                        if competence == current_min and competence + 1 < crew[0][crew[1][malleable_competences.index(min(malleable_competences))]-1]:
                            print(current_min)
                            mins[0].append(malleable_competences.index(current_min))
                            mins[1].append(crew[1][malleable_competences.index(min(malleable_competences))])
                            malleable_competences[lowest_competence_index] = 1*1000 + 1
                    
                    if len(mins[0]) == 1:
                        break
                    else:
                        for i in range(len(mins[0])):
                            current_superior = mins[1][i]
                            number_of_steps = 0
                            while current_superior != -1:
                                current_superior = crew[1][current_superior-1]
                                number_of_steps += 1
                            mins[2].append(number_of_steps)
                        index_in_mins = mins[2].index(max(mins[2]))
                        for i in range(len(malleable_competences)):
                            if malleable_competences[i] == malleable_competences[mins[0][index_in_mins]] and crew[1][i] == mins[1][index_in_mins]:
                                lowest_competence_index = i
                                break
                        break
                malleable_competences[lowest_competence_index] = 10**1000
                lowest_competence_index = malleable_competences.index(min(malleable_competences))
                if len(malleable_competences) <= 1:
                    break
            
            if crew[1][lowest_competence_index] == -1:
                print(f"lowest competence member: captain; their competence: {crew[0][lowest_competence_index]}")
            else:
                print(f"lowest competence member number: {lowest_competence_index + 1}; their competence: {crew[0][lowest_competence_index]}; member's superior: {crew[1][lowest_competence_index]}; superior's competence: {crew[0][crew[1][lowest_competence_index]-1]}")
            
            crew[0][lowest_competence_index] += 1
            k -= 1
            current_member = 0
            
        
        elif crew[1][current_member] == -1:
            current_member += 1


        elif crew[0][current_member] >= crew[0][crew[1][current_member]-1]:
            while crew[0][current_member] >= crew[0][crew[1][current_member]-1]:
                
                if k <= 0:
                    f = open("./output.txt", "a")
                    f.write(f"ajajaj\n")
                    f.close()        
                    ajajaj = True
                    print(crew[0])
                    print(crew[1])
                    print("ajajaj")
                    break
                
                print(f"member number: {current_member + 1}; their competence: {crew[0][current_member]}; member's superior: {crew[1][current_member]}; superior's competence: {crew[0][crew[1][current_member]-1]}")            
                crew[0][crew[1][current_member]-1] += 1
                k -= 1
            current_member += 1


        else:
            current_member += 1

    for member in range(len(crew[1])):
        if crew[1][member] == -1:
            pass
        else:
            if crew[0][member] >= crew[0][crew[1][member]-1]:
                f = open("./output.txt", "a")
                f.write(f"ajajaj\n")
                f.close()        
                ajajaj = True
                print(crew[0])
                print(crew[1])
                print("ajajaj")
                break
                    
    if not ajajaj:
        print(crew[0])
        print(crew[1])
        highest_total_competence = min(crew[0])
        print(k)
        f = open("./output.txt", "a")
        f.write(f"{str(highest_total_competence)}\n")
        f.close()
        # output_text += f"{str(highest_total_competence)}\n"
    
        
# f = open("./posadka_vystup.txt", "a")
# f.write(output_text)
# f.close()
