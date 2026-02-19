import sys


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
                        print(f"{s[1]}: not found")
                else:
                    print("please enter a command")

            else:
                print(f"{s[0]}: command not found")

        pass

if __name__ == "__main__":
    main()
