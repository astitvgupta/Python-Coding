import pyjokes
# This prints a random joke.
joke = pyjokes.get_joke()
print(joke, "\N{grinning face}");


import pyttsx3
# This converts a text into voice message.
engine = pyttsx3.init()
# engine.say("""Hello, I'm Jarvis!""")
engine.say(joke)
engine.runAndWait()

# Schrodinger's attitude to web development: If I don't look at it in Internet Explorer then there's a chance it looks fine.
# A good programmer is someone who always looks both ways before crossing a one-way street.
# Programmer: The ship I boarded crashed and I am dying! Project Manager: Then let's do a quick knowledge transfer session before you go.