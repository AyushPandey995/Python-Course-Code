import sys

def count_lines(file_name):
    with open (file_name, "r") as f:
        l = len(f.readlines())
        return l
    
if __name__ == "__main__":
    file_name = sys.argv[1]
    no_lines = count_lines(file_name)
    print(f"The file '{file_name}' has {no_lines} no. of lines in it")