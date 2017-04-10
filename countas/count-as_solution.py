from pathlib import Path

def count_as(filename):
    my_file = Path(filename)
    if my_file.is_file() == False:
        return "0"
    elif "." in filename:
        content = open(filename, 'r')
        read_content = content.read()
        return read_content.count('a') + read_content.count('A')

    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

print(count_as("countas/afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
