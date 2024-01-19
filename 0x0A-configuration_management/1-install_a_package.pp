# 1-install_a_package.pp - Puppet Manifest to install Flask package

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
