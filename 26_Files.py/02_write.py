## Create a file for a person Jhon Doe and write what you know about him.
"""If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created."""

f = open("JohnDoeInfo.txt", "w")
info = """Heyy everyone, John Doe is a very nice guy. I met him on High Street in New York. He generally uses Python for programming.

"""
f.write(info)
f.close()

