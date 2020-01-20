print("Computers Knows the Following data")
print("a. I am a human being")
print("b. I am good")
print("c. Good graders study")
print("d. Humans love graders")
print("e. Every human does not study")

#concerned_Data - Every,Human,grader,study
#If every is 0, and Human is 1, this means "Not Every" Human...Or..Some Humans

print("Query : Is every human a good grader ?")

#The following data set is possible according to the Propositions -
Data=[{"study":0,"grader":0,"human":1,"every":1},{"study":1,"grader":1,"human":1,"every":0},
           {"study":0,"grader":0,"human":1,"every":1},{"study":0,"grader":0,"human":0,"every":0}]

flag=1
#Our reult would be when EVERY HUMAN is a GOOD GRADER
#Means when "Human" & "Every" implies "Good Grader" is a Tautology for all the possible Data Sets

for i in range(len(Data)):
    p = not(Data[0]["human"] and Data[0]["every"]) or Data[0]["grader"]
    q = not(Data[i]["human"] and Data[i]["every"]) or Data[i]["grader"]
    if ( p == q ):
        continue
    else:
        print("No")
        flag=0
        break;
if(flag==1):
    print("Yes")
