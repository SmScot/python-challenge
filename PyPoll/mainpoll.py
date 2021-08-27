import os
import csv
from typing import TYPE_CHECKING, Set

from numpy import unique

polldata_csv = os.path.join("Resources", "election_data.csv")

votes_cast = []
candidate_total = []

with open(polldata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    for line in csv_reader:
        
        votes_cast.append(line[0])
        candidate_total.append(line[2])

total_votes_cast = len(votes_cast)
print(total_votes_cast)

unique_values = unique(candidate_total)
print(unique_values)

Correy_total = 0
Khan_total = 0
Li_total = 0
OTooley_total = 0

for line in candidate_total:
    if line == "Correy":
        Correy_total = Correy_total +1
    elif line == "Khan":
        Khan_total = Khan_total +1
    elif line == "Li":
        Li_total = Li_total +1
    else:
        OTooley_total = OTooley_total +1

Correy_percent = round(Correy_total/total_votes_cast*100, 2)
Khan_percent = round(Khan_total/total_votes_cast*100, 2)
Li_percent = round(Li_total/total_votes_cast*100, 2)
OTooley_percent = round(OTooley_total/total_votes_cast*100, 2)

Results = (f"Election Results\n----------------\nTotal Votes: {total_votes_cast}\n----------------\nKhan: {Khan_percent}% ({Khan_total})\nCorrey: {Correy_percent}% ({Correy_total})\nLi: {Li_percent}% ({Li_total})\nO'Tooley: {OTooley_percent}% ({OTooley_total})\n----------------\nWinner: Khan\n----------------")
print(Results)

text_path = os.path.join("Analysis", "Results.txt")
file = open(text_path, "w")
file.write(Results)
file.close()
