# Print multiline lyrics of your choice
print("""If you have eagerness in your heart, it means you are alive,
If your eyes are filled with dreams, it means you are alive
Learn to be free like the wind,
Learn to flow freely like the river,
Embrace every moment with open arms,
See a new horizon every time with your eyes,
If you carry surprise in your eyes, it means you are alive,
If you have eagerness in your heart, it means you are alive…""")


import pyttsx3
engine = pyttsx3.init()
engine.say("""Hello, I'm Jarvis!""")
engine.runAndWait()


import os
# Specify the directory you want to list
directory = 'C:/Users/hp/Documents/Prog. Language/Python Coding'
# Get the list of all files and directories
contents = os.listdir(directory)
# Print the contents of the directory
print(f"Contents of '{directory}':")
for item in contents:
    print(item)

