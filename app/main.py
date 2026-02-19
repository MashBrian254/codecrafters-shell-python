import sys


def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break

        s = command.split()

        if len(s) > 0:
            if s[0] == "echo":
                text = " ".join(s[1:])
                print(f"{text}")
            else:
                print(f"{s[0]}: command not found")

        pass

if __name__ == "__main__":
    main()
