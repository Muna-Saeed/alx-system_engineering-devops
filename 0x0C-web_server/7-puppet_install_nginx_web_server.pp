# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Configure Nginx for Hello World! on root
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

nginx::resource::vhost { 'default':
  listen_port => '80',
  proxy       => 'http://localhost:8080',
}

# Configure Nginx for redirection
nginx::resource::location { '/redirect_me':
  ensure   => present,
  location => '/',
  rewrite  => '^(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent',
}
