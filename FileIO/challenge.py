with open("C:\\Users\\evsairn\\PythonProgramming\\Resources\\sample.txt",'a') as jabber:
    for i in range(2,13):
        for j in range(1,13):
            print("{0} times {1} is {2}".format(j,i,j*i),file=jabber)
        print("-" * 20,file=jabber)



