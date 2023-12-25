#0x09. Web infrastructure design

## 1. Simple Web Infrastructure

- User wants to access the website www.foobar.com.
- A server is set up with the following components:
  - Web server (e.g., Nginx) to handle incoming HTTP requests.
  - Application server to execute the website's code and generate dynamic content.
  - Application files containing the website's codebase.
  - Database (e.g., MySQL) to store and retrieve data used by the application.
- The domain name "foobar.com" is configured with a DNS record (A record) that points the "www" subdomain to the server's IP address (e.g., 8.8.8.8).
- The web server communicates with the user's computer over the HTTP protocol.

Issues with this infrastructure:
- Single Point of Failure (SPOF): If the server goes down, the website will become inaccessible.
- Downtime during maintenance: Deploying new code may require restarting the web server, causing temporary downtime.
- Limited scalability: The infrastructure may not handle high traffic loads efficiently.

## 2. Distributed Web Infrastructure

- User wants to access the website www.foobar.com.
- Three servers are set up with the following components:
  - Web server (e.g., Nginx) on two servers to handle incoming HTTP requests.
  - Application server on one server to execute the website's code.
  - Load balancer (e.g., HAproxy) distributes incoming requests across the web servers.
  - Application files containing the website's codebase are deployed on each web server.
  - Database (e.g., MySQL) is set up as a Primary-Replica (Master-Slave) cluster for data redundancy.
- The load balancer uses a distribution algorithm (e.g., round-robin) to evenly distribute requests among the web servers.
- The Primary-Replica cluster ensures data replication and availability.
- The web servers communicate with the user's computer over the HTTP protocol.

Issues with this infrastructure:
- Single Point of Failure (SPOF): If the load balancer or the database Primary node fails, the website's availability and data integrity may be affected.
- Security issues: Lack of firewall and HTTPS can expose the infrastructure to potential threats.
- Lack of monitoring: Without proper monitoring, it's challenging to detect and resolve issues promptly.

## 3. Secured and Monitored Web Infrastructure

- User wants to access the website www.foobar.com.
- Three servers are set up with the following components:
  - Web server (e.g., Nginx) on two servers to handle incoming HTTPS requests.
  - Application server on one server to execute the website's code.
  - Load balancer (e.g., HAproxy) distributes incoming requests across the web servers.
  - Application files containing the website's codebase are deployed on each web server.
  - Database (e.g., MySQL) is set up as a Primary-Replica (Master-Slave) cluster for data redundancy.
  - Firewalls are added to enhance security.
  - SSL certificate is installed to serve the website over HTTPS.
  - Monitoring clients (e.g., Sumologic) collect data for monitoring purposes.
- Firewalls help protect the infrastructure from unauthorized access.
- Serving traffic over HTTPS ensures encryption and data integrity.
- Monitoring tools collect data for performance, availability, and security analysis.
- To monitor web server QPS (Queries Per Second), you can analyze server logs, metrics, or use dedicated monitoring tools.

Issues with this infrastructure:
- Terminating SSL at the load balancer level can limit end-to-end encryption and expose the traffic in the internal network.
- Having only one MySQL server capable of accepting writes can be a single point of failure and affect write scalability.
- Servers with the same components may lead to resource contention and inefficiencies if not properly optimized.

## 4. Scale Up


