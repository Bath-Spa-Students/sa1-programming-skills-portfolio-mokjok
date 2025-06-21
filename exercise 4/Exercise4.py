#steps
#1 create an application that question the user, "what is the capital of France?"after which you will wait for their reply.
#2 The application will tell that the answer entered is correct if they write the right answer ("Paris").
#3 If the answer is wrong, it would print incorrect answer

#giving the variable question.
Answer = input("what is the capital of France?:")
if Answer =="Paris" : #selecting the answer of the question
    print("the answer is correct!") #if the answer in Paris then it is correct
else:
    print("the answer is wrong.") #answer is wrong should be written if it is anything other than Paris
