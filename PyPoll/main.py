import csv

file_to_load="Resources/election_data.csv"
file_to_output='Analysis/elections_poll.txt'

total_votes=0
candidate_options=[]
candidate_votes={}
winner=""
winner_count=0

with open(file_to_load) as election_data:
    reader=csv.DictReader(election_data)

    for row in reader:

        total_votes+=1
        candidate_name=row["Candidate"]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name]+=1
    election_result=(
        "\n\nElection Results\n".format()+
        "----------------------\n".format()+
        "Total Votes: {}\n".format(total_votes)+
        "----------------------\n".format()
    )

print (election_result)

with open (file_to_output,"w") as txt_file:
    text_file.write(election_result)

    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        # vote_percentage