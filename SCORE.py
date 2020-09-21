
score_list = {}
for j in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else :
        score_list[score]=[name]
new_list = []
print(score_list[score])
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")





