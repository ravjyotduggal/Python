text = str(input("Please enter some text: "))

volwels = {"a","e","i","o","u"}

test_set = set(text)

answer = test_set.difference(volwels)
print(sorted(answer))


