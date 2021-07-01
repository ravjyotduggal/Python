result = True
another_result = result

print(id(result))
print(id(another_result))

another_result = "Hello"
print(id(another_result))