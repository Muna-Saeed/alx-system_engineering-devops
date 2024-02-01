# Project: HTTPS SSL Configuration

This project involves configuring a web infrastructure with HTTPS and SSL termination using HAproxy. It includes scripts to display information about subdomains and HAproxy configuration files for SSL termination and automatic redirection from HTTP to HTTPS.

## Table of Contents
1. [Scripts](#scripts)
   - [0-world_wide_web](#0-world-wide-web)
2. [HAproxy SSL Termination](#haproxy-ssl-termination)
   - [1-haproxy_ssl_termination](#1-haproxy-ssl-termination)
3. [Automatic HTTP to HTTPS redirection](#automatic-http-to-https-redirection)
   - [100-redirect_http_to_https](#100-redirect_http_to_https)

## Scripts

### 0-world_wide_web
Bash script that displays information about subdomains. It takes a domain name as an argument and optionally a specific subdomain. The script uses `dig`, `awk`, and Bash functions to retrieve and display the DNS information.

#### Usage:
```bash
./0-world_wide_web holberton.online
./0-world_wide_web holberton.online web-02
```

### HAproxy SSL Termination

#### 1-haproxy_ssl_termination
HAproxy configuration file for SSL termination. It sets up HAproxy to listen on port 443, accept SSL traffic, and serve encrypted traffic that returns the root of the web server containing "Holberton School."

## Automatic HTTP to HTTPS Redirection

### 100-redirect_http_to_https
HAproxy configuration file for redirecting HTTP traffic to HTTPS. It returns a 301 status code for HTTP requests and redirects them to the equivalent HTTPS URL.

## Installation and Setup

1. Install HAproxy version 1.5 or higher.
2. Obtain SSL certificate for your domain and update the paths in the HAproxy configuration files accordingly.
3. Update the IP addresses of the servers in the HAproxy configuration files.

## Author
Muna Saeed
