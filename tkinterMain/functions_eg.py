def python_food():
    print("Spam and eggs")


# def centre_text(text, integer):
#     left_margin = (80 - len(text))//integer
#     print(" " * left_margin, text)

#Passing multiple arguments in the function


def centre_text(*args):
    text = " "
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text))//2
    #print(" " * left_margin, text)
    #return " " * left_margin + text
    return "Success"

#python_food()


print(centre_text("first", "second", 3, 4, "spam"))


