# File: 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => '
server {
    listen 80;
    server_name _;

    location / {
        root   /var/www/html;
        index  index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
	
}
',
}

# Enable the site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [File['/etc/nginx/sites-available/default'], Package['nginx']],
}
