# 1-install_a_package.pp - Puppet Manifest to install Flask package

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
