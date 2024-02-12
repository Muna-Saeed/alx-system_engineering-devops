# 0x13 Firewall

This repository contains scripts to configure firewall settings on web servers.

## Description

This project involves configuring the firewall on web-01 to redirect traffic from port 8080/TCP to port 80/TCP using `ufw` (Uncomplicated Firewall).

## Tasks

### Task 0: Block all incoming traffic but...

Configure the `ufw` firewall on web-01 to block all incoming traffic except for the following TCP ports:

- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS SSL)

#### Answer File: [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but)

### Task 1: Port Forwarding (Advanced)

Configure the `ufw` firewall on web-01 to forward traffic from port 8080/TCP to port 80/TCP.

#### Answer File: [100-port_forwarding](./100-port_forwarding)

## Instructions

### Task 0:

1. Install `ufw` if not already installed.
2. Configure `ufw` to block all incoming traffic except for specified ports.
3. Share the `ufw` commands used in the answer file.

### Task 1:

1. Modify the `ufw` configuration file to enable port forwarding from 8080/TCP to 80/TCP.
2. Share a copy of the modified `ufw` configuration file.

## Usage

Follow the instructions in each task to configure the firewall on web-01. Ensure that the specified ports are accessible, and port forwarding is correctly set up.

## Author

Muna
```
