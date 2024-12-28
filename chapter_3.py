# Q: write greeting message for user using input function 
name=input("enter your name: ")
print(f"Good AfterNoon {name}")


# Q: use replace() function
letter='''Dear <|name|>,
you are selected!
<|date|>'''
print(letter.replace("<|name|>","Tirth shah").replace("<|date|>","27th December 2024"))


# Q: write a python program to che double space 
a="my name is  tirth shah"
print(a.find("  "))


# Q: write a program to replace double spaces with single spaces 
b="my name is  tirth shah"
print(a.replace("  "," "))


#Q: write a python program to showcase a use of  escape sequence charecters
greet="Dear user,\n\tThis is Artificial Intelligence.\nwelcome." 
print(greet)