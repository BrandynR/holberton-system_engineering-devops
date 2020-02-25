# Changed the limits
exec { 'nginx':
  command => 'sudo sed -i "s/15/15000/" /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin:/bin:/sbin',
}
