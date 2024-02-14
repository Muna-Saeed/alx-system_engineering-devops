#0x14. MySQL

# MySQL Setup and Backup Tasks

This repository contains scripts and configurations for setting up MySQL on web-01 and web-02 servers, creating a primary-replica infrastructure, and implementing a backup strategy.

## Task 0: Install MySQL on web-01 and web-02

This task involves installing MySQL on both web-01 and web-02 servers. Ensure that MySQL distribution is version 5.7.x and that the configurations are set appropriately.

### Requirements

- MySQL distribution must be 5.7.x.
- Task #3 of the SSH project must be completed for web-01 and web-02.
- The checker will connect to your servers to check MySQL status.

### Steps

1. Install MySQL on web-01 and web-02.
2. Verify the MySQL version to ensure it is 5.7.x.
3. Confirm that SSH project task #3 is completed on both servers.

### Example

```bash
ubuntu@web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@web-01:~$
```

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql

---

## Task 1: Let us in!

In order to verify server configurations, create a MySQL user named `holberton_user` on both web-01 and web-02 with host set to localhost and the password `projectcorrection280hbtn`. Ensure proper SSH configurations.

### Example

```bash
ubuntu@web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@web-01:~$
```

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql

---

## Task 2: If only you could see what I've seen with your eyes

Set up a database with a table on web-01 to replicate from. Create a database named `tyrell_corp` and a table named `nexus6`. Ensure `holberton_user` has SELECT permissions.

### Example

```bash
ubuntu@web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@web-01:~$
```

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql

---

## Task 3: Quite an experience to live in fear, isn't it?

Create a new user `replica_user` on web-01 for the replica server. Ensure the user has appropriate permissions to replicate the primary MySQL server.

### Example

```bash
ubuntu@web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@web-01:~$
```

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql

---

## Task 4: Setup a Primary-Replica infrastructure using MySQL

Setup a primary-replica infrastructure with MySQL. The primary MySQL server should be hosted on web-01, and the replica should be hosted on web-02.

### Requirements

- MySQL primary must be hosted on web-01 (comment out bind-address).
- MySQL replica must be hosted on web-02.
- Setup replication for the MySQL database named `tyrell_corp`.

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql
- Files: `4-mysql_configuration_primary`, `4-mysql_configuration_replica`

### Example

```bash
# On web-01
ubuntu@web-01:~$ mysql -uholberton_user -p
Enter password:
mysql> show master status;
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog

_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp          |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)
mysql>

# On web-02
root@web-02:/home/ubuntu# mysql -uholberton_user -p
Enter password:
mysql> show slave status\G
# Check Slave_IO_Running and Slave_SQL_Running
```

---

## Task 5: MySQL backup

Create a Bash script that generates a MySQL dump, compresses it, and stores it in a different system in another physical location.

### Requirements

- MySQL dump must contain all your MySQL databases.
- MySQL dump must be named `backup.sql`.
- MySQL dump file has to be compressed to a tar.gz archive.
- Archive must have the following name format: `day-month-year.tar.gz`.
- User to connect to the MySQL database must be `root`.
- Bash script accepts one argument: the password used to connect to the MySQL database.

### Example

```bash
ubuntu@03-web-01:~$ ls
5-mysql_backup
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ more backup.sql
# Contents of MySQL dump file
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
ubuntu@03-web-01:~$
```

### Repository

- GitHub repository: [alx-system_engineering-devops](https://github.com/Muna-Saeed/alx-system_engineering-devops)
- Directory: 0x14-mysql
- File: `5-mysql_backup`

---
