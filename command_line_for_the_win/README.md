# Command line for the win

This project is a collection of tasks to be completed in the command line for the command_line_for_the_win directory.

## Table of Contents

- [General](#general)
- [Tasks](#tasks)
  1. [First 9 tasks](#first-9-tasks)
  2. [Reach completed tasks](#reach-completed-tasks)
  3. [Reach the perfect cube, 27](#reach-the-perfect-cube-27)

## General

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line.

## Tasks

### First 9 tasks

Complete the first 9 tasks.

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: `command_line_for_the_win`
- File: `0-first_9_tasks.jpg`, `0-first_9_tasks.png`

### Reach completed tasks

Complete the next 9 tasks, reaching a total of 18 completed tasks.

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: `command_line_for_the_win`
- File: `1-next_9_tasks.jpg`, `1-next_9_tasks.png`

### Reach the perfect cube, 27

Complete the next 9 tasks, reaching a total of 27 completed tasks.

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: `command_line_for_the_win`
- File: `2-next_9_tasks.jpg`, `2-next_9_tasks.png`

## Steps Followed to Upload Screenshots using SFTP

1. Open a terminal or command prompt on your local machine.
2. Use the SFTP command-line tool to establish a connection to the sandbox environment. Replace `<hostname>` with the hostname provided, `<username>` with your username, and `<password>` with your password.
   ````bash
   sftp <username>@<hostname>
   ```
3. Enter your password when prompted.
4. Once connected, navigate to the directory where you want to upload the screenshots. Use the `cd` command to change directories.
   ````bash
   cd path/to/directory
   ```
5. Use the `put` command to upload the screenshots from your local machine to the sandbox environment. Replace `<local_file>` with the path to your local screenshot file and `<remote_file>` with the desired filename on the sandbox environment.
   ````bash
   put <local_file> <remote_file>
   ```
6. Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
7. Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
