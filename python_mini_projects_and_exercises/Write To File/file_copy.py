import sys

def copy(from_filename, to_filename):
    with open(from_filename, 'r') as file1:
        with open(to_filename, 'w') as file2:
            for line in file1:
                l = line.strip()
                if l == "done":
                    break
                file2.write(l + '\n')

if __name__ == "__main__":
    copy(sys.argv[1], sys.argv[2])