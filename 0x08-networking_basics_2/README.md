Certainly! Below are the README.md details for the provided tasks:

## 0x08. Networking basics #1

### Project Overview:

The goal of this project is to enhance your understanding of networking basics. It covers topics such as localhost, IP resolution, hosts file, and active network interfaces.

### Resources:

Read or watch:

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

Man or help:

- `ifconfig`
- `telnet`
- `nc`
- `cut`

### Learning Objectives:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General:**

1. What is localhost/127.0.0.1
2. What is 0.0.0.0
3. What is /etc/hosts
4. How to display your machine’s active network interfaces

### Requirements:

**General:**

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

---

### Tasks:

#### 0. Change your home IP

**Mandatory**

Write a Bash script that configures an Ubuntu server with the below requirements.

**Requirements:**

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.

Example:

```bash
$ ping localhost
$ ping facebook.com
$ sudo ./0-change_your_home_IP
$ ping localhost
$ ping facebook.com
```

In this example, we can see that:

- Before running the script, localhost resolves to 127.0.0.1, and facebook.com resolves to 157.240.11.35.
- After running the script, localhost resolves to 127.0.0.2, and facebook.com resolves to 8.8.8.8.

If you’re running this script on a machine that you’ll continue to use, be sure to revert localhost to 127.0.0.1. Otherwise, a lot of things will stop working!

**Repo:**

GitHub repository: [alx-system_engineering-devops](repository-link)
Directory: 0x08-networking_basics_2
File: 0-change_your_home_IP

#### 1. Show attached IPs

**Mandatory**

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

Example:

```bash
$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
```

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our localhost IP :)

**Repo:**

GitHub repository: [alx-system_engineering-devops](repository-link)
Directory: 0x08-networking_basics_2
File: 1-show_attached_IPs

#### 2. Port listening on localhost

**Advanced**

Write a Bash script that listens on port 98 on localhost.

**Usage:**

Terminal 0:

Starting my script.

```bash
$ sudo ./100-port_listening_on_localhost
```

Terminal 1:

Connecting to localhost on port 98 using telnet and typing some text.

```bash
$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

Terminal 0:

Receiving the text on the other side.

```bash
$ sudo ./100-port_listening_on_localhost
Hello world
test
```

For the sake of the exercise, this connection is made entirely within localhost. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software, and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!

**Repo:**

GitHub repository: [alx-system_engineering-devops](repository-link)
Directory: 0x08-networking_basics_2
File: 100-port_listening_on_localhost
