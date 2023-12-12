import os
import csv

csv_file_path = ".\\vbu_mod_3\\python-challenge\\PyPoll\\main.py\\Resources\\election_data.csv"  
output_file_path = ".\\vbu_mod_3\\python-challenge\\PyPoll\\main.py\\analysis\\election_poll_analysis_results.txt"

def analyze_and_export_election_votes_data(csv_file_path, output_file_path):
    total_votes = 0
    candidates = {}
    
    with open(csv_file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader) 

        for row in csvreader:
            total_votes = total_votes + 1

            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates[candidate_name] = 1
            else:
                candidates[candidate_name] = candidates[candidate_name] + 1

    percentages = {}
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        percentages[candidate] = percentage

    winner = max(candidates, key=candidates.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    with open(output_file_path, mode="w") as textfile:
        textfile.write("Election Results\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("-------------------------\n")
        for candidate, votes in candidates.items():
            textfile.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("-------------------------\n")
        
    print(f"Election poll analysis results exported to {output_file_path}")

analyze_and_export_election_votes_data(csv_file_path, output_file_path)
