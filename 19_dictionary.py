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