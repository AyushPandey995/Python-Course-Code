import re
text = "The quick brown fox jumps over the lazy dog."
match = re.search("brown", text)
if match:
    print("Match Found!!")
    print("Start Index- ", match.start()) #gives starting index 
    print("End Index- ", match.end()) #gives ending index

print(re.findall("the", text, re.IGNORECASE)) 

print(f"Text- {text}")
new_text = re.sub("fox", "cat", text) #Changes all the occurances of fox
print(f"New text- {new_text}")

"""website = https://regexr.com/    ...... to learn more about regular expression"""