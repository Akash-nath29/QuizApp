with open('QnA.txt','r+') as f:
    for line in f:
        line = line.rstrip('\n')
        question, answer = line.split('/')
        print(question)
        query = str(input('\t:'))
        if query.lower()==answer:
            print('Correct !!')
        else:
            print('Incorrect')