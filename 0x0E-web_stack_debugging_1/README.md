# Web Stack Debugging 1

## Task 0: Nginx likes port 80

I encountered an issue where Nginx was not listening on port 80 in my Ubuntu container. To address this, I performed debugging and created a Bash script to automate the fix.

### Steps:

1. Identified the issue: Nginx was not listening on port 80.
2. Created a Bash script, `0-nginx_likes_port_80`, to configure the server to ensure Nginx is running and listening on port 80.
3. Verified the fix by using `curl` to check if Nginx responds on port 80.

### Usage:

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

Repo:

- [Web Stack Debugging 1](https://github.com/Muna-Saeed/alx-system_engineering-devops/0x0E-web_stack_debugging_1)
- File: [0-nginx_likes_port_80](https://github.com/Muna-Saeed/alx-system_engineering-devops/0x0E-web_stack_debugging_1/0-nginx_likes_port_80)

---

## Task 1: Make it sweet and short (Advanced)

For this advanced task, I further optimized the Bash script to be concise, consisting of 5 lines or fewer.

### Steps:

1. Ensured Nginx is not running using `service nginx status`.
2. Created a Bash script, `1-debugging_made_short`, to fix the issue in 5 lines or fewer.
3. Verified the fix using `curl` to check Nginx's response on port 80.

### Usage:

```bash
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<!-- More HTML content -->
</body>
</html>
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/#
```

Repo:

- [Web Stack Debugging 1](https://github.com/Muna-Saeed/alx-system_engineering-devops/0x0E-web_stack_debugging_1)
- File: [1-debugging_made_short](https://github.com/Muna-Saeed/alx-system_engineering-devops/0x0E-web_stack_debugging_1/1-debugging_made_short)
