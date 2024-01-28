# Attack is the Best Defense
This repository contains solutions to two network security tasks involving ARP spoofing, sniffing unencrypted traffic, and conducting a dictionary attack.

### Introduction
Network security is crucial, and understanding potential vulnerabilities is essential. Unencrypted traffic poses a significant risk, as attackers can intercept sensitive information. This project focuses on sniffing unencrypted traffic, specifically targeting Sendgrid's telnet-based email service.

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

In this task, we focus on sniffing unencrypted traffic to extract information. We start by understanding the vulnerabilities associated with unencrypted communication, particularly through Telnet. The task involves:

- Sniffing unencrypted traffic using tcpdump
- Extracting sensitive information (password) from the sniffed traffic
- Authenticating into a server to perform the sniffing

#### Instructions
1. Clone the repository.
2. Execute the `user_authenticating_into_server` script locally on your Linux machine.
3. Use `tcpdump` to sniff the network and find the password.
4. Paste the password in the provided answer file.

### Task 1: Dictionary Attack

This task involves conducting a dictionary attack on an SSH account. The goal is to break into the SSH account using a dictionary of passwords. The steps include:

- Installing Docker on your Ubuntu machine
- Pulling and running a Docker image provided
- Finding or creating a password dictionary
- Using Hydra to brute force the SSH account
- Sharing the found password in the answer file

#### Instructions
1. Install Docker on your Ubuntu machine.
2. Pull and run the Docker image `sylvainkalache/264-1`.
3. Obtain or create a password dictionary.
4. Install and use Hydra to brute force the SSH account `sylvain`.
5. Share the found password in the answer file.

### Repository Structure

```
|-- attack_is_the_best_defense/
|   |-- 0-sniffing
|   |   |-- user_authenticating_into_server
|   |-- 1-dictionary_attack
```

### Usage

- Clone the repository.
- Follow the instructions provided for each task.

### Disclaimer

Be cautious while performing these tasks and ensure that you adhere to ethical standards and legal regulations.

**Note:** The passwords found is in the respective answer files.

**Repository:** [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)

**Maintainer:** [Muna Mohammed](mailto:munasaeed6367@gmail.com)
