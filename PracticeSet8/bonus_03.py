"""copied from gpt.. need to analyse the code!!!"""

import os
import sys

def folder_size(folder_path):
    total_size = 0

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)

    return total_size


if __name__ == "__main__":
    folder = sys.argv[1]
    size = folder_size(folder)
    print(f"Total size of files in '{folder}' is {size} bytes")
