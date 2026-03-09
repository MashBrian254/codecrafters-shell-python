import sys
import os

def main():

    while True:
        sys.stdout.write("$ ")
        builtins =['type','exit','echo']

        command = input()
        
        s = command.split()
        if s[0] == "exit":
            break

        if len(s) > 0:
            
            if s[0] == "echo":
                text = " ".join(s[1:])
                print(f"{text}")
        
            elif s[0] == 'type':
                if len(s) > 1:
                    if s[1] in builtins:
                        print(f"{s[1]} is a shell builtin")

                    else:
                        PATH = os.environ.get("PATH")
                        for dir in PATH.split(":"):
                            file_path = os.path.join(dir, s[1])
                            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                                print(f"{s[1]} is {file_path}")
                                break
                        else:
                            print(f"{s[1]}: not found")

                        
                else:
                    print("please enter a command")

            else:
                print(f"{s[0]}: command not found")

        pass

if __name__ == "__main__":
    main()
