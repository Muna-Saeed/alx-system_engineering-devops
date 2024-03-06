# Ensure Apache is installed

package { 'apache2':
  ensure => installed,
}

# To automate the fix
exec { 'fix-apache':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

# Ensure Apache is running and restart if necessary
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/sites-available/000-default.conf'],
}
