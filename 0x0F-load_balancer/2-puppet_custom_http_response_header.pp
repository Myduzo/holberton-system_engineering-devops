#!/usr/bin/env bash
# automate the task of creating a custom HTTP header response with Puppet.
exec { 'http header with puppet':
  command => 'sudo apt-get -y update;
sudo apt-get -y install nginx;

echo "Holberton School" > /var/www/html/index.nginx-debian.html;
echo "Ceci n'est pas une page" > /var/www/html/404.html;
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 http://youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
    add_header X-Served-By $HOSTNAME;
}" > /etc/nginx/sites-available/default;
service nginx restart',
    provider => shell,
      }
