# set limit to 2000 and restart nginx

exec { 'set limit to 2000 and restart nginx':
  path    => '/bin',
  command => 'sed -i "s/15/2000/" /etc/default/nginx && sudo service nginx restart'
}
