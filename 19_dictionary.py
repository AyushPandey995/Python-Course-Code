marks = {"Ayush ": 84, "Khushi": 93, "Diksha": 77, "Harry": 74}
print(marks)
print(marks["Khushi"])
marks["Khushi"] = 95
print(marks)

"""Methods"""
toped_on = {"Maths": "Ayush",
            "Bio": "Khushi",
            "Chemistry": "Pratha",
            "Physics": "Praveen",
            "English": "KishorKumar"
            }
print(toped_on)
print(toped_on.keys())
print(toped_on.values())
print(toped_on.items())
toped_on.pop("English")
print(toped_on)

list1 = [toped_on.get("Maths", 0), toped_on.get("English", 0)]
print(list1) #.get('key', default_value) gives the value of key if found and if not then returns the defalut value,
toped_on.update({"Hindi" : "Stephen Hawkin"})
print(toped_on)
toped_on["English"] = "Kishor Kumar"
print(toped_on)
print(toped_on.pop("hduh", 0)) #Here if any key is not available in the dict then it will not throw an error insted retuen the default value

new_toped_on = toped_on.copy()
print(new_toped_on)

toped_on.clear()
print(toped_on)