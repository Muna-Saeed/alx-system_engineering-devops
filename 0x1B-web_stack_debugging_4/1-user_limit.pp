# Puppet manifest to change OS configuration for holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
