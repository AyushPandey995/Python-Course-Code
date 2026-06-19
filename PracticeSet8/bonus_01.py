def upper_case(file_name):

    with open (file_name, "r") as f:
        content = f.read().upper()
    
    with open (f"upper_{file_name}", "w") as f:
        f.write(content)
        

upper_case("notes.txt")