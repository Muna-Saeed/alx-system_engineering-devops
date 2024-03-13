# Puppet manifest to optimize Nginx server configuration

# Install required package 'nginx' and 'apache2-utils' for ApacheBench
package { 'nginx':
  ensure => installed,
}

package { 'apache2-utils':
  ensure => installed,
}

# Ensure Nginx can handle and respond to a higher volume of requests.

exec { 'adjust maximum open files limit for Nginx':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
