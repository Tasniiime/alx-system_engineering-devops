#/usr/bin/puppet
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}

