panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"

print(numbers.split(","))

generated_list = ['9',' ',
                  '2','2','3',' ',
                  '3','7','2',' ',
                  '0','3','6',' ',
                  '8','5','4',' ',
                  '7','7','5',' ',
                  '8','0','7'
]

print(generated_list)

print("".join(generated_list).split())

#print("".join(generated_list).split())

# values = "".join(generated_list)
# print(values)
#
# values_list = values.split()
# print(values_list)
#

#Mini Challenge
# new_list = []
# for i in values_list:
#     new_list.append(int(i))
# print(new_list)