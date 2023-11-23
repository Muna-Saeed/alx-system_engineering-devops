# Project: 0x04-loops_conditions_and_parsing

Welcome to the DevOps project "0x04-loops_conditions_and_parsing." This project focuses on strengthening your scripting skills by working with loops, conditions, and parsing in Bash. Follow the tasks outlined below to complete the project.

## Tasks

### Task 0: Create a SSH RSA key pair

In this task, you'll generate an RSA key pair for SSH access to your servers. Follow the instructions in the task description to create the key pair and share the public key. Ensure to keep the private key secure for future server access.

- File: [0-RSA_public_key.pub](0-RSA_public_key.pub)

### Task 1: For Best School loop

Write a Bash script that displays "Best School" 10 times using a for loop. Ensure to follow the provided script template and include necessary comments.

- File: [1-for_best_school](1-for_best_school)

### Task 2: While Best School loop

Write a Bash script that displays "Best School" 10 times using a while loop. Follow the guidelines in the task description and add appropriate comments to your script.

- File: [2-while_best_school](2-while_best_school)

### Task 3: Until Best School loop

Create a Bash script that displays "Best School" 10 times using an until loop. Make sure to adhere to the specified loop type and include descriptive comments in your script.

- File: [3-until_best_school](3-until_best_school)

### Task 4: If 9, say Hi!

Write a Bash script that displays "Best School" 10 times, but for the 9th iteration, display "Best School" and then "Hi" on a new line. Utilize the provided script structure and include appropriate comments.

- File: [4-if_9_say_hi](4-if_9_say_hi)

### Task 5: 4 bad luck, 8 is your chance

Develop a Bash script that loops from 1 to 10 and displays different messages based on the loop iteration. Follow the outlined requirements and provide a well-commented script.

- File: [5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance)

### Task 6: Superstitious numbers

Create a Bash script that displays numbers from 1 to 20 and provides specific messages for certain loop iterations. Utilize the case statement as instructed and ensure your script is well-commented.

- File: [6-superstitious_numbers](6-superstitious_numbers)

### Task 7: Clock

Write a Bash script that displays the time for 12 hours and 59 minutes. Use the while loop as specified, and note that only the first 70 lines are displayed using the head command.

- File: [7-clock](7-clock)

### Task 8: For ls

Develop a Bash script that displays the content of the current directory in a list format, showing only the part of the name after the first dash. Ensure to use the for loop and adhere to the provided example.

- File: [8-for_ls](8-for_ls)

### Task 9: To file, or not to file

Create a Bash script that provides information about the "school" file. Use if and else statements to check if the file exists, if it's empty, and if it's a regular file.

- File: [9-to_file_or_not_to_file](9-to_file_or_not_to_file)

### Task 10: FizzBuzz

Write a Bash script that displays numbers from 1 to 100 and applies specific rules for certain multiples. Implement the provided requirements using a for loop.

- File: [10-fizzbuzz](10-fizzbuzz)

### Task 11: Read and cut (Advanced)

Write a Bash script that displays the content of the file /etc/passwd. Your script should only display:

username
user id
Home directory path for the user

Requirements:

- You must use the while loop (for and until are forbidden)

- File: [100-read_and_cut](100-read_and_cut)

### Task 12: Tell the story of passwd (Advanced)

Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

Requirements:

- You must use the while loop (for and until are forbidden)

- File: [101-tell_the_story_of_passwd](101-tell_the_story_of_passwd)

### Task 13: Let's parse Apache logs (Advanced)

Apache is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.

Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.

Requirement:

- Format: IP HTTP_CODE
- In a list format
- You must use awk
- You are not allowed to use while, for, until, and cut

- File: [102-lets_parse_apache_logs](102-lets_parse_apache_logs)

### Task 14: Dig the data (Advanced)

Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.

Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.

Requirements:

- The exact format must be: OCCURRENCE_NUMBER IP HTTP_CODE
- In list format
- Ordered from the greatest to the lowest number of occurrences
- You must use awk
- You are not allowed to use while, for, until, and cut

- File: [103-dig_the-data](103-dig_the-data)

## Repository Information

- GitHub repository: [Muna-Saeed/alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x04-loops_conditions_and_parsing
