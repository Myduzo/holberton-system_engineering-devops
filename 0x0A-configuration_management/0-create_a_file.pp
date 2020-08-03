# create a file in /tmp.
file { '/tmp/holberton': #path of the new file
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
