# 0x1B. Web stack debugging #4

# Web Stack Debugging 4

## Overview
This directory contains Puppet manifests and configurations to address issues related to web server performance and user access.

## Tasks
### 0. Sky is the limit, let's bring that limit higher
In this task, we optimize the Nginx server configuration to handle a higher volume of requests and ensure that failed requests are minimized.

### 1. User limit
This task focuses on changing the OS configuration to allow the holberton user to log in and open files without encountering any error messages related to file limits.

## Requirements
- Ubuntu 14.04 LTS
- Puppet v3.4
- Puppet-lint v2.1.1
- Ensure all files end with a new line
- Puppet manifests must pass `puppet-lint` without any errors
- Puppet manifests must run without error
- Puppet manifests files must end with the extension `.pp`
- Install puppet-lint:
  ```
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
  ```

## Usage
1. Clone the repository:
   ```
   $ git clone https://github.com/Muna-Saeed/alx-system_engineering-devops.git
   ```
2. Navigate to the appropriate directory:
   ```
   $ cd alx-system_engineering-devops/0x1B-web_stack_debugging_4
   ```
3. Apply the Puppet manifest:
   ```
   $ puppet apply <manifest_file_name.pp>
   ```

## Author
Muna (https://github.com/Muna-Saeed)

```
