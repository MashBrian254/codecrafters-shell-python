[![progress-banner](https://backend.codecrafters.io/progress/shell/f7dae795-7461-49c0-8334-a5b75238dd7e)](https://app.codecrafters.io/users/Mash1990?r=2qF)

["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview).

In this challenge, I build a POSIX compliant shell that's capable of
interpreting shell commands, running external programs and builtin commands like
cd, pwd, echo and more. Lessons learn include shell command parsing,
REPLs, builtin commands, and more.

## 🚀 Implemented Features

### 1. Builtin Commands

The shell handles several "Builtin" commands internally for speed and process control:

- `echo`: Prints arguments to standard output.
- `type`: Identifies if a command is a shell builtin or an external executable (and provides the path).
- `pwd`: Prints the current absolute working directory.
- `cd`: Changes the current directory (supports absolute paths, relative paths, and the `~` home shortcut).
- `exit`: Gracefully terminates the shell process.

### 2. External Program Execution

For any command not defined as a builtin, the shell:

1. Searches the system's `PATH` environment variable for a matching executable.
2. Uses the **"Easier to Ask for Forgiveness than Permission" (EAFP)** pattern to attempt execution.
3. Spawns a child process using the `subprocess` module to run the command with provided arguments.

### 3. Robust Error Handling

- **Command Not Found:** Gracefully catches `FileNotFoundError` when an external program doesn't exist.
- **Invalid Directories:** Provides specific error messaging for `cd` attempts on non-existent paths.
- **Empty Input:** Handles "Enter" key presses without crashing or echoing errors.