import os

a = os.listdir("fake_for_code") #List files and directories available in that folder.
print(a)

current_directory = os.getcwd() #Get the current working directory
print(current_directory)

b = os.path.exists("fake_for_code") #Check if a file or directory exists
print(b)

os.remove("") #used tp remove the existing file
os.rmdir("") #used to remove the existing empty directory

# path = os.path.join("folder", "subfolder", "file.txt")
# print("Joined path:", path) ###??? want to search about this 