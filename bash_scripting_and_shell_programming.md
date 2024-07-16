# Section 2: Shell Scripting in a Nutshell

## 4. Shell Scripting, Part I

### Scripts
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

Executing `sleepy.sh`:
```console
$ ./sleepy.sh &
[1] 16796
$ ps -fp 16796
UID     PID     PPID    C   STIME   TTY     TIME        CMD
jason   16796   16725   0   22:50   pts/0   00:00:00    /bin/bash ./sleepy.sh
```
```console
$ /tmp/sleepy.sh &
[1] 16804
$ ps -fp 16804
UID     PID     PPID    C   STIME   TTY     TIME        CMD
jason   16804   16725   0   22:51   pts/0   00:00:00    /bin/bash /tmp/sleepy.sh
$ ps -ef| grep 16804 | grep -v grep
jason   16804   16725   0   22:51   pts/0   00:00:00    /bin/bash /tmp/sleepy.sh
jason   16805   16804   0   22:51   pts/0   00:00:00    sleep 90
$ pstree -p 16804
sleepy.sh(16804)----sleep(16805)
```
`hi.py`
```bash
#!/usr/bin/python
print "This is a Python script."
```
We can also use other interpreter for running our scripts, like `Python`.

Executing `hi.py`:
```console
$ chmod 755 `hi.py`
$ ./hi.py
This is a Python script.
```

### Variables
* Syntax: `VARIABLE_NAME="Value"`
* Variables are case sensitive.
* By convention variables are uppercase.

Assign `string` to a variable
```bash
#!/bin/bash
MY_SHELL="bash"
echo "I like the $MY_SHELL shell."
echo "I like the ${MY_SHELL} shell."
echo "I am ${MY_SHELL}ing on my keyboard."
echo "I am $MY_SHELLing on my keyboard."
```

Output:
```console
I like the bash shell.
I like the bash shell.
I am bashing on my keyboard.
I am  on my keyboard.
```

Assing `command output` to a variable
```bash
#!/bin/bash
SERVER_NAME=$(hostname)
echo "You are running this script on ${SERVER_NAME}."
```

Output:
```console
You are running this on linuxsvr.
```

### Tests
Syntax:

`[ condition-to-test-for ]`

* Example: `[ -e /etc/passwd ]` checks if `passwd` file exists inside `/etc/`.

`File` operators (tests)
* `-d FILE` --> True if the file is a directory.
* `-e FILE` --> True if the file exists.
* `-f FILE` --> True if the file exists & is a regular file.
* `-r FILE` --> True if the file is readable by you.
* `-s FILE` --> True if the file exists & is not empty.
* `-w FILE` --> True if the file is writable by you.
* `-x FILE` --> True if the file is executable by you.

`String` operators (tests)
* `-z STRING` --> True if the string is empty.
* `-n STRING` --> True if the string is not empty.
* `STRING1=STRING2` --> True if the strings are equal.
* `STRING1!=STRING2` --> True if the strings are not equal.

`Arithmetic` operators (tests)
* `arg1 -eq arg2` --> True if arg1 is equal to arg2.
* `arg1 -ne arg2` --> True if arg1 is not equal to arg2.

* `arg1 -lt arg2` --> True if arg1 is less than arg2.
* `arg1 -le arg2` --> True if arg1 is less than or equal to arg2.

* `arg1 -gt arg2` --> True if arg1 is greater than arg2.
* `arg1 -ge arg2` --> True if arg1 is greater than or equal to arg2.

## 5. Shell Scripting, Part I

### `if`, `elif` & `else` statement

Syntax:

```bash
if [ condition-is-true]
then
    command 1
elif [ condition-is-true ]
then
    command 2
else
    command N
fi
```

Example:
```bash
#!/bin/bash
MY_SHELL="csh"

if [ "$MY_SHELL" = "bash" ]
then
    echo "You seem to like the bash shell."
elif [ "$MY_SHELL" = "csh" ]
then
    echo "You seem to like the csh shell."
else
    echo "You don't seem to like the bash or csh shells."
fi
```

### `for` loop

Syntax:
```bash
for VARIABLE_NAME in ITEM_1 ITEM_N
do
    command 1
    command 2
    command N
done
```

Example 1:
```bash
#!/bin/bash
for COLOR in red green blue
do
    echo "COLOR: $COLOR"
done
```

Output:
```console
COLOR: red
COLOR: green
COLOR: blue
```

Example 2:
```bash
#!/bin/bash
COLORS="red green blue"

for COLOR in $COLORS
do
    echo "COLOR: $COLOR"
done
```

`rename-pics.sh`
```bash
#!/bin/bash
PICTURES=$(ls *jpg)
DATE=$(date +%F)

for PICTURE in $PICTURES
do
    echo "Renaming ${PICTURE} to ${DATE}-${PICTURE}"
    mv ${PICTURE} ${DATE}-${PICTURE}
done
```

CLI:
```command
$ ls
bear.jpg    man.jpg     pig.jpg     rename-pics.sh
$ ./rename-pics.sh
Renaming bear.jpg to 2015-03-06-bear.jpg
Renaming man.jpg to 2015-03-06-man.jpg
Renaming pig.jpg to 2015-03-06-pig.jpg
$ ls
2015-03-06-bear.jpg     2015-03-06-man.jpg
2015-03-06-pig.jpg      rename-pics.sh
```

### Positional Parameters

```command
$ script.sh parameter1 parameter2 parameter3
```

```command
$0: "script.sh"
$1: "parameter1"
$2: "parameter2"
$3: "parameter3"
```

`archive_user.sh`
```bash
#!/bin/bash

echo "Executing script: $0"
echo "Archiving user: $1"

# Lock the account
passwd -l $1

# Create an archive of the home directory.
tar cf /archives/${1}.tar.gz /home/${1}
```

CLI:
```command
$ ./archive_user.sh elvis
Executing script: ./archive_user.sh
Archiving user: elvis
passwd: password expiry information changed.
tar: Removing leading '/' from member names
```

```bash
#!/bin/bash

echo "Executing script: $0"
echo "Archiving user: $1"

# Lock the account
passwd -l $1

# Create an archive of the home directory.
tar cf /archives/${1}.tar.gz /home/${1}
```

```bash
#!/bin/bash
USER=$1 # The first parameter is the user.

echo "Executing script: $0"
echo "Archiving user: $USER"

# Lock the account
passwd -l $USER

# Create an archive of the home directory.
tar cf /archives/${USER}.tar.gz /home/${USER}
```

`archive_user.sh`
```bash
#!/bin/bash

echo "Executing script: $0"
for USER in $@
do
    echo "Archiving user: $USER"
    # Lock the account
    passwd -l $USER
    # Create an archive of the home directory.
    tar cf /archives/${USER}.tar.gz /home/${USER}
done
```
_Note: `$@` does not contain `$0`, i.e., the script name itself._

CLI:
```command
$ ./archive_user.sh chet joe
Executing script: ./archive_user.sh
Archiving user: chet
passwd: password expiry information changed.
tar: Removing leading '/' from member names
Archiving user: joe
passwd: password expiry information changed.
tar: Removing leading '/' from member names
```

### Accepting User Input (STDIN)

The read command accepts STDIN.

Syntax:
```bash
read -p "PROMPT" VARIABLE
```

`archive_user.sh`
```bash
#!/bin/bash

read -p "Enter a user name: " USER
echo "Archiving user: $USER"

# Lock the account
passwd -l $USER

# Create an archive of the home directory.
tar cf /archives/${USER}.tar.gz /home/${USER}
```

CLI:
```command
$ ./archive_user.sh
Enter a user name: mitch
Archiving user: mitch
passwd: password expiry information changed.
tar: Removing leading '/' from member names
```

# Section 3: Return Codes & `exit` Statuses

## 7. `exit` Statues & Return Codes

### `exit` Status/Return Code

* Every command returns an `exit` status
* Range from `0` to `255`
* `0` = success
* Other than `0` = error condition
* Use for error checking
* Use `man` or `info` to find meaning of `exit` status

### Checking the `exit` Status

* `$?` contains the return code of the previously executed command.

Example 1:
```bash
ls /not/here
echo "$?"
```

Output:
```command
2
```

Example 2:
```bash
HOST="google.com"
ping -c 1 $HOST                 # "-c 1" means 1 packet.

if [ "$?" -eq "0" ]
then
    echo "$HOST reachable."
else
    echo "$HOST unreachable."
fi
```

Example 2:
```bash
HOST="google.com"
ping -c 1 $HOST
RETURN_CODE=$?

if [ "$RETURN_CODE" -ne "0" ]
then
    echo "$HOST unreachable."
fi
```

### `&&` and `||`

`&&` = AND
```command
$ mkdir /tmp/bak && cp test.txt /tmp/bak/
```

`||` = OR
```command
$ cp test.txt /tmp/bak/ || cp test.txt /tmp
```

Example 1:
```bash
#!/bin/bash

HOST="google.com"
ping -c 1 $HOST && echo "$HOST reachable."
```

Example 2:
```bash
#!/bin/bash

HOST="google.com"
ping -c 1 $HOST || echo "$HOST unreachable."
```

### The `;` (semicolon)

Separate commands with a `;` (semicolon) to ensure they all get executed.
```command
$ cp test.txt /tmp/bak/ ; cp test.txt /tmp
```

Same as:
```command
$ cp test.txt /tmp/bak/
$ cp test.txt /tmp
```

### `exit` Command

Explicitly define the return code `exit 0`, `exit 1`, `exit 2`, `exit 255`, etc..

_Note: The default value is that of the last command executed._

Example 1:
```bash
#!/bin/bash

HOST="google.com"
ping -c 1 $HOST

if [ "$?" -ne "0" ]
then
    echo "$HOST unreachable."
    exit 1
fi
exit 0
```

Example 2:
```console
$ ping -c 1 google.com
...
$ echo $?
0
$ ping -c 1 -w 1 amazon.com
...
$ echo $?
1
$ ping -c 1 amazon.com.blah
...
$ echo $?
2
```

Check `error` codes:
```console
$ man ping      # Open ping documentation.
...
$ /code         # Searches for "code" in the documentation.
...
$ q             # Quit the documentation.
```

Example 3:
```console
$ mkdir /tmp/jason/bak && cp -v /etc/hosts /tmp/jason/bak
...
$ echo $?
1
$ mkdir -p /tmp/jason/bak && cp -v /etc/hosts /tmp/jason/bak    # Creates parent directory as well.
...
$ cp -v /etc/hosts /tmp/bak/ || cp -v /etc/hosts /tmp/
...
$ cp -v /etc/hosts /tmp/ || cp -v /etc/hosts /tmp/bak/
...
$ ls /etc/hosts ; hostname ; uptime
...
```

# Section 4: Shell Functions

## 10. Functions, Part I

### `function`

* Must be defined before use.
* Has parameter support.

Syntax:
```bash
function function-name() {
    # Code goes here.
}

function-name() {
    # Code goes here.
}
```

Example 1:
```bash
#!/bin/bash
function hello() {
    echo "Hello!"
}
hello
```

Example 2:
```bash
#!/bin/bash

function hello() {
    echo "Hello!"
    now
}

function now() {
    echo "It's $(date +%r)"
}

hello
```

### Positional Parameters

* Functions can accept parameters.
* The first parameter is stored in `$1`.
* The second parameter is stored in `$2`, etc.
* `$@` contains all of the parameters.
* Just like shell scripts.
    * `$0` = the script itself, not function name.

Example 1:
```bash
#!/bin/bash

function hello() {
    echo "Hello $1"
}

hello Jason
```

Output:
```console
Hello Jason
```

Example 2:
```bash
#!/bin/bash

function hello() {
    for NAME is $@
    do
        echo "Hello $NAME"
    done
}

hello Jason Dan Ryan
```

Output:
```console
Hello Jason
Hello Dan
Hello Ryan
```

### Variable Scope

* By default, variables are global.

If a global variable is inside a `function`, it does not get defined until the `function` is invoked once.
```bash
#!/bin/bash

my_function() {
    GLOBAL_VAR=1
}

# GLOBAL_VAR not available yet.
echo $GLOBAL_VAR

my_function

# GLOBAL_VAR is NOW available.
echo $GLOBAL_VAR
```

### Local Variables

* Can only be accessed within the function.
* Create using the `local` keyword.
    * `local LOCAL_VAR=1`
* Only functions can have local variables.

## 11. Functions, Part II

### `exit` status (`return` codes)

* Functions have an `exit` status.
* Explicitly
    * `return` <RETURN_CODE>
* Implicity
    * The `exit` status of the last command executed in the function.
* Valid `exit` codes range from `0` to `255`.
* `0` = success
* `$?` = the `exit` status

```bash
my_function
echo $?
```

```bash
function backup_file() {
    if [ -f $1 ]
    then
        BACK="/tmp/$(basename ${1}).$(date +%F).$$"
        echo "Backing up $1 to ${BACK}"
        cp $1 $BACK
    fi
}

backup_file /etc/hosts

if [ $? -eq 0 ]
then
    echo "Backup succeeded!"
fi
```

```bash
function backup_file() {
    if [ -f $1 ]
    then
        local BACK="/tmp/$(basename ${1}).$(date +%F).$$"
        echo "Backing up $1 to ${BACK}"
        # The exit status of the function will be
        # the exit status of the cp command.
        cp $1 $BACK
    else
        # The file does not exist.
        return 1
    fi
}

backup_file /etc/hosts

# Make a decision based on the exit status.
if [ $? -eq 0 ]
then
    echo "Backup succeeded!"
else
    echo "Backup failed!"
    # About the script & return a non-zero
    # exit status.
    exit 1
fi
```
