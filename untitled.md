# Bash Scripting & Shell Programming

## Section 2: Shell Scripting in a Nutshell

### 4. Shell Scripting, Part I

Scripts
* Contain a series of commands.
* An interpreter executes commands in the script.
* Anything you can type at the command line, you can put in a script.
* Great for automating tasks.

`script.sh`

```bash
#!/bin/bash
echo "Scripting is fun!"
```

```console
foo@bar:~$ chmod 755 script.sh
foo@bar:~$ ./script.sh
Scripting is fun!
```

`#!` --> Shebang, `bash` --> Interpreter

`sleepy.sh`

```bash
#!/bin/bash
sleep 90
```

```console
foo@bar:~$ ./sleepy.sh &
[1] 16796
foo@bar:~$ ps -fp 16796
UID    PID    PPID   C  STIME  TTY    TIME      CMD
jason  16804  16725  0  22:51  pts/0  00:00:00  /bin/bash  /tmp/sleepy.sh
foo@bar:~$ ps
```
