# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
    
      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;
    
      server_name _;
    
      location / {
        return 301 http://$host/redirect_me;
      }
    
      location /redirect_me {
        return 301 http://$host/hello.html;
      }
    
      location /hello.html {
        return 200 "Hello World!";
      }
    }
  ',
}

# Enable and start Nginx service
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => Package['nginx'],
}
