# 0x18. Webstack monitoring

# Web Stack Monitoring with Datadog

This directory contains scripts and configuration files for setting up web stack monitoring using Datadog. The project includes tasks such as signing up for Datadog, installing the Datadog agent on servers, creating monitors, and setting up a dashboard.

## Directory Structure
- `README.md`
- `2-setup_datadog`: Store the dashboard ID.

## Task 0: Sign Up for Datadog and Install Datadog Agent

### Requirements
- Allowed editors: vi, vim, emacs
- Interpretation environment: Ubuntu 16.04 LTS
- All files should end with a new line
- README.md file is mandatory
- Bash scripts must be executable
- Bash script must pass Shellcheck (version 0.3.7) without any error
- First line of Bash scripts should be #!/usr/bin/env bash
- Second line of Bash scripts should be a comment explaining what the script is doing

### Instructions
1. Sign up for Datadog on the [Datadog US website](https://app.datadoghq.com).
2. Use the US1 region during sign-up.
3. Install the Datadog agent on the `web-01` server.
4. Create an application key in Datadog.
5. Copy and paste your Datadog API key and application key into your Intranet user profile.
6. Ensure that your server `web-01` is visible in Datadog under the hostname `XX-web-01`.
7. Validate server visibility using the provided API.
8. If needed, update the hostname of your server.

## Task 1: Monitor Some Metrics

### Requirements
- Set up monitors within the Datadog dashboard to monitor read and write requests per second.

### Instructions
1. Log in to Datadog and navigate to the Monitors tab.
2. Set up a monitor to check the number of read requests issued to the device per second.
3. Set up a monitor to check the number of write requests issued to the device per second.
4. Adjust thresholds and notification preferences.
5. Save and validate monitors by triggering read and write requests.

## Task 2: Create a Dashboard

### Requirements
- Create a dashboard with at least 4 widgets displaying different metrics.
- Create an answer file `2-setup_datadog` with the dashboard ID on the first line.

### Instructions
1. Log in to Datadog and navigate to the Dashboards tab.
2. Create a new dashboard and add at least 4 widgets of different types.
3. Arrange and customize widgets based on monitored metrics.
4. Save the dashboard with a meaningful name.
5. Retrieve the dashboard ID using Datadog's API.
6. Create the answer file `2-setup_datadog` with the dashboard ID on the first line.

## File Structure

```plaintext
- alx-system_engineering-devops
  - 0x18-webstack_monitoring
    - 2-setup_datadog
  - README.md
```

Feel free to reach out for any clarifications or additional assistance.
```

This README.md file provides a structured overview of the tasks, requirements, and instructions for web stack monitoring project.
