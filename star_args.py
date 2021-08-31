# def average(*args):
#     print(type(args))
#     print("args is {}".format(args))
#     print("*args is:", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# print(average(1,2,3,4))

#Challenge


# def build_tuple(*args):
#     return args
#
#
# number_tuple = build_tuple("hello","planet","earth","take","me","to","your","leader")
# print(number_tuple)

#**kwargs

#def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, **kwargs):
#     end_character = kwargs.pop('end','\n')
#     sep_character = kwargs.pop('sep',' ')
#     print("sep character is {} and kwargs is {}".format(sep_character, kwargs))
#     for word in args[::-1]:
#         print(word[::-1], end=sep_character, **kwargs)
#     print(end=end_character)

def print_backwards(*args, **kwargs):
    seperator = kwargs['sep']
    for word in args[::-1]:
        print(word[::-1], end=seperator)


with open('backwards.txt', 'w') as backward:
    #print_backwards("hello","planet","earth","take","me","to","your","leader", file=backward)
    print_backwards("hello","planet","earth","take","me","to","your","leader", sep='|')
