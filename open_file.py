score_list = []

score_list_file = open("score.txt")

for score in score_list_file:

    # score = score.rstrip()  # Delete \n  #For Example rstrip("0"), print(001111000) to output(1111)
    score = score.rstrip().split(",")

    # score_list.append(score)
    score_list.append([score[0], int(score[1])])

score_list_file.close()

print score_list
