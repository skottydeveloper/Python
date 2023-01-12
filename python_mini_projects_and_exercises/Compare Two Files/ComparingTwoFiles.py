import sys

def same_content(file1, file2) -> bool:
    with open(file1, 'r') as f:
        file1 = f.readlines()
    
    with open(file2, 'r') as f:
        file2 = f.readlines()
    
    for line in file1:
        if file1 == file2:
            return True
    return False

if __name__ == "__main__":
    if same_content(sys.argv[1], sys.argv[2]):
        print("The two files have the same content.")
    else:
        print("The two files do not have the same content.")