name = "Ayush pandey"
print(len(name))
print(name.upper()) #All character will be in upper case
print(name.lower())#All character will be in lower case
print(name.capitalize())#First character of first word will be in upper case
print(name.title())#First character of all words will be in upper case

text = "   twinkle, twinkle, little star, how I wonder what you are.    "
print(text.strip())  # remove the unnecessary white space from starting and ending of the text
print(text.lstrip())
print(text.rstrip())

print(text.find("how"))
 
print(text.replace("twinkle", "khushi"))

new = "Apple, Oranges, Banana, Guava"
print(new.split())
