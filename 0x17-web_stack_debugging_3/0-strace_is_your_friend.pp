# Ensure Apache is installed

package { 'apache2':
  ensure => installed,
}

# To automate the fix
exec { 'fix-apache':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
