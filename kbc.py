question_list = [
"How many continents are there?",# pehla question
"What is the capital of India?",# doosra question
"NG mei kaun se course padhaya jaata hai?"# teesra question
]

options_list =[["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#pehle question ke liye options
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#second question ke liye options
["1.Software Engineering", "2.Counseling", "3.Tourism", "4Agriculture"]]
#third question ke liye options
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
option=[["1.four","2.seven"],["chandigarh","Delhi"],["Software Ingineering","tourism"]]
solution=[2,2,1]
i=0
count=0
while i<len(question_list):
    print(question_list[i])
    print(options_list[i])
    lifeline=input("enter you want lifline: yes or no=")
    if lifeline=="yes":
        if count==0:
            print(option[i])
            ans=int(input("enter the answer="))
            count+=1
            if ans==solution[i]:
                print("correct answer=")
            else:
                print("wrong answer=") 
                break
        else:
            print("no lifeline left")    
            ans2=int(input("enter the answer="))
            if ans2==solution_list[i]:
                print("correct answer=")
            else:
                print("wrong answer")    
    else:
        print("no")
        a=int(input("enter the answer="))
        if a==solution_list[i]:
            print("correct ans")
        else:
            print("wrong")
            break
    i=i+1


                    
    


