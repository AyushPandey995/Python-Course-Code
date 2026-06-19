import os

# for n in range(1, 6):
#     with open (f"{n}.tmp", "w") as f:
#         content = "This is a temp file"
#         f.write(content)



def delete_tmp_files():
    current_dir = os.getcwd()

    for files in os.listdir(current_dir):
        if files.endswith(".tmp") :
            os.remove(files)
            print(f"Delated: {files}")
            
if __name__ == "__main__":
    delete_tmp_files()
