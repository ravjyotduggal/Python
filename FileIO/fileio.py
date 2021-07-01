# jabber = open("C:\\Users\\evsairn\\PythonProgramming\\Resources\\sample.txt",'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open("C:\\Users\\evsairn\Desktop\\04LS.txt",'r') as jabber:
#     for line in jabber:
#         print(line)
#         if "JAB" in line.upper():
#             print(line, end='')

#ReadLine

# with open("C:\\Users\\evsairn\\PythonProgramming\\Resources\\sample.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

#ReadLines
#
# with open("C:\\Users\\evsairn\\PythonProgramming\\Resources\\sample.txt",'r') as jabber:
#     lines = jabber.read()
# print(lines)
#
# # for line in lines:
# #     print(line, end='')

with open("C:\\Users\\evsairn\\PythonProgramming\\Resources\\sample.txt",'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()


