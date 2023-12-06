# Installs a Nginx server with custom HTTP header

exec { 'update':
  provider => shell,
  command  => 'sudo apt-get update',
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
