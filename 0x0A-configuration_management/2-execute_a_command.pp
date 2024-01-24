# 2-execute_a_command.pp - Puppet Manifest to kill a process

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
}
