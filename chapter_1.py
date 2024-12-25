#Q :  print multi line input in python 
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')#This is how you print multi-line content in python



#Q:  import any module of your choice and use it 

import pyttsx3#module which convert text into speech
engine = pyttsx3.init()
engine.say("Welcome to the world of Artificial Intelligence and machine learning.")#text to convert into speech
engine.runAndWait()



# Q: write program to print content of directory using OS module 

import os

# Specify the directory path (use '.' for current directory)
directory_path = '.'  # '.' represents the current directory

# Get the list of files and directories in the specified directory
content = os.listdir(directory_path)

# Print each entry in the directory
for entry in content:
    print(entry)