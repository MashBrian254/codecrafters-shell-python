import sys
import shutil
import subprocess

BUILTINS =['type','exit','echo']

def cmd_exit(args):
    sys.exit(0)

def cmd_echo(args):
        print(" ".join(args))

def cmd_type(args):
    for arg in args:
        if arg in BUILTINS:
            print(f"{arg} is a shell builtin")
        elif path := shutil.which(arg):
            print(f"{arg} is {path}")
        else:
            print(f"{arg}: not found")

COMMAND_MAP = {
    "exit": cmd_exit,
    "echo": cmd_echo,
    "type": cmd_type,
}

def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        parts = command.split()
        
        if not parts:
            continue

        cmd, args = parts[0], parts[1:]
        if cmd in COMMAND_MAP:
            COMMAND_MAP[cmd](args)
        elif path := shutil.which(cmd):
            subprocess.run([path] + args)
        else:
            print(f"{cmd}: command not found")
        

if __name__ == "__main__":
    main()
