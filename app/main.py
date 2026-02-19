import sys


def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break

        s = command.split()
        if s[0] == "echo":
            text = " ".join(s[1:])
            print(f"{text}")

        pass

if __name__ == "__main__":
    main()
