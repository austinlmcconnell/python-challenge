import os
import csv

csv_path = os.path.abspath(os.path.join("Resources", "election_data.csv"))

print("Election Results")
print("----------------------")

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    
    total_votes = 0
    candidates_list = []
    small_candidates_list = []
    for row in csv_reader:
        total_votes += 1
        candidates_list.append(str(row[2]))

    print("Total Votes: ", total_votes)
    print("-------------------")

    for candidate in candidates_list:
        if candidate not in small_candidates_list:
            small_candidates_list.append(candidate)
    
    candidate_1 = small_candidates_list[0]
    candidate_2 = small_candidates_list[1]
    candidate_3 = small_candidates_list[2]
    candidate_1_count = candidates_list.count(small_candidates_list[0])
    candidate_2_count = candidates_list.count(small_candidates_list[1])
    candidate_3_count = candidates_list.count(small_candidates_list[2])
    candidate_1_percent = (candidate_1_count / len(candidates_list)) * 100
    candidate_2_percent = (candidate_2_count / len(candidates_list)) * 100
    candidate_3_percent = (candidate_3_count / len(candidates_list)) * 100

    print(str(candidate_1) + ": " + str(round(candidate_1_percent, 3)) + "%" + " (" + str(candidate_1_count) + ")")
    print(str(candidate_2) + ": " + str(round(candidate_2_percent, 3)) + "%" + " (" + str(candidate_2_count) + ")")
    print(str(candidate_3) + ": " + str(round(candidate_3_percent, 3)) + "%" + " (" + str(candidate_3_count) + ")")
    print("---------------------")

    winning_list = [candidate_1_count, candidate_2_count, candidate_3_count]
    winning_total = max(winning_list)
    if winning_total == candidate_1_count:
        print("Winner: " + str(candidate_1))
    elif winning_total == candidate_2_count:
        print("Winner: " + str(candidate_2))
    elif winning_total == candidate_3_count:
        print("Winner: " + str(candidate_3))
    
    print("--------------------")

    with open('PyPollAnalysis.txt', 'w') as f:
        f.write("Election Results\n")
        f.write("----------------------\n")
        f.write("Total Votes: " + str(total_votes) + "\n")
        f.write("-------------------\n")
        f.write(str(candidate_1) + ": " + str(round(candidate_1_percent, 3)) + "%" + " (" + str(candidate_1_count) + ")\n")
        f.write(str(candidate_2) + ": " + str(round(candidate_2_percent, 3)) + "%" + " (" + str(candidate_2_count) + ")\n")
        f.write(str(candidate_3) + ": " + str(round(candidate_3_percent, 3)) + "%" + " (" + str(candidate_3_count) + ")\n")
        f.write("---------------------\n")
        if winning_total == candidate_1_count:
            f.write("Winner: " + str(candidate_1) + "\n")
        elif winning_total == candidate_2_count:
            f.write("Winner: " + str(candidate_2) + "\n")
        elif winning_total == candidate_3_count:
            f.write("Winner: " + str(candidate_3) + "\n")
        f.write("--------------------\n")
