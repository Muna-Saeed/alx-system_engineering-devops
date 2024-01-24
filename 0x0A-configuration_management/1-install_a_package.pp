# 1-install_a_package.pp - Puppet Manifest to install Flask package

package { 'python3-pip':
  ensure => 'installed',
}

package { 'libffi-dev':
  ensure => 'installed',
}

package { 'libssl-dev':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  creates => '/usr/local/lib/python3.8/dist-packages/flask',
}
