from Questions import QUESTIONS
print('Welcome to the Game! This is not gonna be like your usual out of fun games. The stakes are high,and the rewards mesmerizing.')
print('Starting the ultimate Marvel Cinematic version of KBC- Kaun Banega Crorepati!!! ')
def isAnswerCorrect(ques,ans):
    for n in QUESTIONS:
        if n['name']==ques:
            a=n['answer']
            if a==int(ans):
                return True
            else:
                return False
def lifeLine(ques):
    for n in QUESTIONS:
        if n['name']==ques:
            a=n['answer']
            c=0
            for i in range(1,5):
                if i!=a and c<2:
                    del n['option'+str(i)]
                    c+=1
            for i in n:
                if i=='answer':
                    break
                print(n.get(i))
def kbc():
    print('Rules: * You will have 15 rounds')
    print('*For each question, there are 4 choices out of which ONLY one is correct.')
    print('* Each correct answer will get you money corresponding to the question and displays the next question.\n*If you are:')
    print('  1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)\n  2. As you correctly answer question number 5, the minimum reward becomes Rs. 10,000 (First level)')
    print('  3. As you correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)\n* If the answer is wrong, then you will return with the minimum reward.')
    print('* If you type "lifeline" (case insensitive) as input, then two incorrect options will be hidden and prompt again for the input of answer.')
    print('* NOTE: 50-50 lifeline can be used ONLY ONCE.\nThere is no option of lifeline for the last question( ques no. 15 ), even if you have not used it before.')
    print('* If you type "quit" (case insensitive) as input, then you will return with the amount you have won until now, instead of the minimum amount.')
    money=0
    lifeline=False
    for j in range(15):
        for i in QUESTIONS[j]:
            if i=='answer':
                break
            print(QUESTIONS[j].get(i))
        print('Type the option number or type lifeline or type quit')
        ans=input()
        if ans.lower()=='lifeline':
            if lifeline==True or j==14:
                print('Sorry, You have already used your lifeline. You cannot use lifeline anymore')
            if lifeline == False and j!=14:
                lifeline=True
                lifeLine(QUESTIONS[j].get('name'))
            again=input()
            if isAnswerCorrect(QUESTIONS[j].get('name'), again):
                print('Correct!!')
                money = QUESTIONS[j].get('money')
                print('Congrats! You have won Rs. ' + str(money))
            elif ans.lower() == 'quit':
                print('Congrats! You have won Rs. ' + str(money))
                break
            elif isAnswerCorrect(QUESTIONS[j].get('name'), again) == False:
                print('Incorrect')
                print('The correct answer is ' + str(QUESTIONS[j].get('answer')))
                if j < 5:
                    print(
                        'Sorry, You could not win any prize money. Do take our hampers and participation gifts though.')

                elif j >= 5 and j < 11:
                    print('Congrats! Your winning prize is Rs.10000')
                elif j >= 11:
                    print('Congrats! Your winning prize money is Rs.3,20,000')
                break
        elif ans.lower()=='quit':
            print('Congrats! You have won Rs. ' + str(money))
            break
        elif isAnswerCorrect(QUESTIONS[j].get('name'), ans):
            print('Correct!!')
            money=QUESTIONS[j].get('money')
            print('Congrats! You have won Rs. '+str(money))
        elif isAnswerCorrect(QUESTIONS[j].get('name'), ans)==False:
            print('Incorrect')
            print('The correct answer is '+str(QUESTIONS[j].get('answer')))
            if j<5:
                print('Sorry, You could not win any prize money. Do take our hampers and participation gifts though.')
            elif j>=5 and j<11:
                print('Congrats! Your winning prize is Rs.10000')
            elif j>=11:
                print('Congrats! Your winning prize money is Rs.3,20,000')
            break

    print('Thank You for playing KBC!')

kbc()





