#Replaces .phpp with .php
exec { 'fix file name':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
