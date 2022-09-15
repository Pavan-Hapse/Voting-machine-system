Responces=["Thank You for using Voting Machine", "                                =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*", "                                                 Welcome In Voting Machine                "]

print("\n\n\n")

print(Responces[1])
print(Responces[2])
print(Responces[1])

print("\n")

print("\n \t \t \t \tPlease Enter the candidate Names who are belongs to Election Parties:")

candidate1=input("\n \t \t \t \t \t Enter the name for 1st candidate: ")
candidate2=input("\n \t \t \t \t \t Enter the name for 2st candidate: ")

cand1_votes=0
cand2_votes=0


""" Method1 
voter_id=[101,102,103,104,105,106,107,108,109,110]
"""

voters_id=[]
size=int(input("\n \t \t \t \tEnter the Total Number of voter.. Who are comming for voting: "))
print("\n \t \t \t \t" f"Please Enter the {size} voters id.. who have come for vote")
for i in range(size):
    v_id=int(input("\n \t \t \t \t"))
    voters_id.append(v_id)

print("\n \t \t \t \tThis are the candidate Id's for voting: ", voters_id)

no_of_voters=len(voters_id)
print("\n \t \t \t \t \t Number of voters: ", no_of_voters)

voted=[]

while True:
    if voters_id==[]:
        print("\n \t \t \t \t \t Voting is over!!")
        if cand1_votes>cand2_votes:
            print("\n \t \t \t \t \t" f"{candidate1} won the election with {cand1_votes} Votes")
        elif cand2_votes>cand1_votes:
            print("\n \t \t \t \t \t" f"{candidate2} won the election with {cand2_votes} Votes")
        elif cand1_votes==cand2_votes:
            print(" \t \t \t \t \t Result Tied")
        break
    else:
        voter=int(input("\n \t \t \t \t \t Enter your id: "))
        if voter in voted:
            print("\n \t \t \t \t \t You are already voted!!")
        else:
            if voter in voters_id:
                print("\n \t \t \t \t \t" f"1. {candidate1}\n\n \t \t \t \t \t2. {candidate2}")
                choice=int(input("\n \t \t \t \t \t Enter Your Choice: "))
                if choice==1:
                    cand1_votes+=1
                    print("\n \t \t \t \t \t" f"You Voted to {candidate1}")
                elif choice==2:
                    cand2_votes+=1
                    print("\n \t \t \t \t \t" f"You Voted to {candidate2}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("\n \t \t \t \t \t You are not allow to vote...!!")
print("\n \t \t \t \t \t",Responces[0])