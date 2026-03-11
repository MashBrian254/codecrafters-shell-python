import sys
import shutil
import subprocess
import os
import shlex

BUILTINS = ['type','exit','echo', 'pwd', 'cd']

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

def cmd_pwd(args):
    print(os.getcwd())

def cmd_cd(args):
    if not args:
        print("cd: missing argument")

    elif len(args) > 1:
        print("too many arguments")
    else: 
        try:  
            target_path = os.path.expanduser(args[0])         
            os.chdir(target_path)
        except FileNotFoundError:
            print(f"cd: {args[0]}: No such file or directory")

def parse_arguments(user_input):
    args = shlex.split(user_input)
    return args
    


COMMAND_MAP = {
    "exit": cmd_exit,
    "echo": cmd_echo,
    "type": cmd_type,
    "pwd": cmd_pwd,
    "cd" : cmd_cd,
}

def main():

    while True:
        sys.stdout.write("$ ")
        user_input = input()
        parts = parse_arguments(user_input)
        
        if not parts:
            continue

        cmd, args = parts[0], parts[1:]
        if cmd in COMMAND_MAP:
            COMMAND_MAP[cmd](args)
        else:
            try:
                subprocess.run([cmd] + args)
            except FileNotFoundError:
                print(f"{cmd}: command not found") 
        

if __name__ == "__main__":
    main()
