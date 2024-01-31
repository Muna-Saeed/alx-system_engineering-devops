# System Engineering & DevOps - Load Balancer

## Tasks

### 0. Double the number of webservers

To accomplish this task, I followed these steps:

1. Configured Nginx on both `web-01` and `web-02` to include a custom HTTP response header (`X-Served-By`).
2. Created a Bash script (`0-custom_http_response_header`) to automate the configuration of a new Ubuntu machine to meet the specified requirements.
3. Implemented a round-robin algorithm for distributing requests.

### 1. Install your load balancer

For this task, I completed the following actions:

1. Installed and configured HAproxy on the `lb-01` server.
2. Configured HAproxy to send traffic to both `web-01` and `web-02` using a round-robin algorithm for request distribution.
3. Ensured HAproxy can be managed via an init script for easy control.
4. Wrote a Bash script to configure a new Ubuntu machine, ensuring it meets the specified requirements.

### 2. Add a custom HTTP header with Puppet (Advanced)

In this advanced task, I achieved the following:

1. Used Puppet to automate the creation of a custom HTTP header response (`X-Served-By`).
2. Ensured the custom header's value is the hostname of the server where Nginx is running.
3. Developed a Puppet manifest (`2-puppet_custom_http_response_header.pp`) to configure a new Ubuntu machine, meeting the specified requirements.
