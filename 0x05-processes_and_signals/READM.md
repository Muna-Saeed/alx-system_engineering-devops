# 0x05-processes_and_signals
This directory contains Bash scripts and a C program for handling processes and signals. The tasks cover various aspects, from displaying process information to managing and controlling processes.

### Task 0: What is my PID
- **Script:** `0-what-is-my-pid`
- **Description:**
  - Write a Bash script that displays its own PID.
  - Example:
    ```bash
    sylvain@ubuntu$ ./0-what-is-my-pid
    4120
    sylvain@ubuntu$
    ```

### Task 1: List your processes
- **Script:** `1-list_your_processes`
- **Description:**
  - Write a Bash script that displays a list of currently running processes.
  - Requirements:
    - Show all processes, for all users, including those which might not have a TTY.
    - Display in a user-oriented format.
    - Show process hierarchy.
  - Example:
    ```bash
    sylvain@ubuntu$ ./1-list_your_processes | head -50
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    ...
    sylvain@ubuntu$
    ```

### Task 2: Show your Bash PID
- **Script:** `2-show_your_bash_pid`
- **Description:**
  - Using the command from the previous exercise, write a Bash script that displays lines containing the word 'bash,' allowing you to easily get the PID of your Bash process.
  - Requirements:
    - You cannot use `pgrep`.
    - The third line of your script must be `# shellcheck disable=SC2009`.
  - Example:
    ```bash
    sylvain@ubuntu$ ./2-show_your_bash_pid
    sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
    sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
    sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
    sylvain@ubuntu$
    ```

### Task 3: Show your Bash PID made easy
- **Script:** `3-show_your_bash_pid_made_easy`
- **Description:**
  - Write a Bash script that displays the PID, along with the process name, of processes whose name contains the word 'bash.'
  - Requirements:
    - You cannot use `ps`.
  - Example:
    ```bash
    sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
    4404 bash
    4555 bash
    sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
    4404 bash
    4557 bash
    sylvain@ubuntu$
    ```

### Task 4: To infinity and beyond
- **Script:** `4-to_infinity_and_beyond`
- **Description:**
  - Write a Bash script that displays "To infinity and beyond" indefinitely.
  - Requirements:
    - In between each iteration of the loop, add a `sleep 2`.
  - Example:
    ```bash
    sylvain@ubuntu$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    ^C
    sylvain@ubuntu$
    ```

### Task 5: Don't stop me now!
- **Script:** `5-dont_stop_me_now`
- **Description:**
  - Write a Bash script that stops the `4-to_infinity_and_beyond` process.
  - Requirements:
    - You must use `kill`.
  - Example:
    ```bash
    # Terminal #0
    sylvain@ubuntu$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Terminated
    sylvain@ubuntu$

    # Terminal #1
    sylvain@ubuntu$ ./5-dont_stop_me_now
    sylvain@ubuntu$
    ```

### Task 6: Stop me if you can
- **Script:** `6-stop_me_if_you_can`
- **Description:**
  - Write a Bash script that stops the `4-to_infinity_and_beyond` process.
  - Requirements:
    - You cannot use `kill` or `killall`.
  - Example:
    ```bash
    # Terminal #0
    sylvain@ubuntu$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Terminated
    sylvain@ubuntu$

    # Terminal #1
    sylvain@ubuntu$ ./6-stop_me_if_you_can
    sylvain@ubuntu$
    ```

### Task 7: Highlander
- **Script:** `7-highlander`
- **Description:**
  - Write a Bash script that displays "To infinity and beyond" indefinitely.
  - Requirements:
    - In between each iteration of the loop, add a `sleep 2`.
    - Display "I am invincible!!!" when receiving a `SIGTERM` signal.
  - Example:
    ```bash
    # Terminal #0
    sylvain@ubuntu$ ./7-highlander
    To infinity and beyond
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    ^C
    sylvain@ubuntu$

    # Terminal #1
    sylvain@ubuntu$ ./67-stop_me_if_you_can
    sylvain@ubuntu$ ./67-stop_me_if_you_can
    sylvain@ubuntu$
    ```

### Task 8: Beheaded process
- **Script:** `8-beheaded_process`
- **Description:**
  - Write a Bash script that kills the process `7-highlander`.
  - Example:
    ```bash
    # Terminal #0
    sylvain@ubuntu$ ./7-highlander
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Killed
    sylvain@ubuntu$

    # Terminal #1
    sylvain@ubuntu$ ./8-beheaded_process
    sylvain@ubuntu$
    ```

### Task 9: Process and PID file
- **Script:** `100-process_and_pid_file`
- **Description:**
  - Write a Bash script that:
    - Creates the file `/var/run/myscript.pid` containing its PID.
    - Displays "To infinity and beyond" indefinitely.
    - Displays "I hate the kill command" when receiving a `SIGTERM` signal.
    - Displays "Y U no love me?!" when receiving a `SIGINT` signal.
    - Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal.
  - Example:
    ```bash
    sylvain@ubuntu$ sudo ./100-process_and_pid_file
    To infinity and beyond
    To infinity and beyond
    ^C
    Y U no love me?!
    Executing the 100-process_and_pid_file script and killing it with ctrl+c.
    ```

### Task 10: Manage my process
- **Scripts:** `101-manage_my_process` and `manage_my_process`
- **Description:**
  - Write a Bash script that manages a process that indefinitely writes "I am alive!" to the file `/tmp/my_process`. In between every "I am alive!" message, the program should pause for 2 seconds.
  - Write a Bash (init) script `101-manage_my_process` that manages `manage_my_process`.
  - Requirements:
    - When passing the argument `start`:
      - Starts `manage_my_process`.
      - Creates a file containing its PID in `/var/run/my_process.pid`.
      - Displays "manage_my_process started."
    - When passing the argument `stop`:
      - Stops `manage_my_process`.
      - Deletes the file `/var/run/my_process.pid`.
      - Displays "manage_my_process stopped."
    - When passing the argument `restart`:
      - Stops `manage_my_process`.
      - Deletes the file `/var/run/my_process.pid`.
      - Starts `manage_my_process`.
      - Creates a file containing its PID in `/var/run/my_process.pid`.
      - Displays "manage_my_process restarted."
    - Displays "Usage: manage_my_process {start|stop|restart}" if any other argument or no argument is passed.
  - Example:
    ```bash
    sylvain@ubuntu$ sudo ./101-manage_my_process
    Usage: manage_my_process {start|stop|restart}
    sylvain@ubuntu$ sudo ./101-manage_my_process start
    manage_my_process started
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    I am alive!
    ^C
    sylvain@ubuntu$ sudo ./101-manage_my_process stop
    manage_my_process stopped
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    cat: /var/run/my_process.pid: No such file or directory
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    ^C
    sylvain@ubuntu$ sudo ./101-manage_my_process start
    manage_my_process started
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    11864
    sylvain@ubuntu$ sudo ./101-manage_my_process restart
    manage_my_process restarted
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    11918
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    ^C
    sylvain@ubuntu$
    ```

### Task 11: Zombie
- **Script:** `102-zombie.c`
- **Description:**
  - Write a C program that creates 5 zombie processes.
  - Requirements:
    - For every zombie process created, it displays "Zombie process created, PID: ZOMBIE_PID."
  - Example:
    ```bash
    # Terminal #0
    sylvain@ubuntu$ gcc 102-zombie.c -o zombie
    sylvain@ubuntu$ ./zombie 
    Zombie process created, PID: 13527
    Zombie process created, PID: 13528
    Zombie process created, PID: 13529
    Zombie process created, PID: 13530
    Zombie process created, PID: 13531
    ^C
    sylvain@ubuntu$
    
    # Terminal #1
    sylvain@ubuntu$ ps aux | grep -e 'Z+.*<defunct>'
    sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep

