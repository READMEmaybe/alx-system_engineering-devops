# puppet manifest to install nginx and redirect /redirect_me
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

exec { 'append_redirect_me':
  command => "/usr/bin/sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 \"Moved Permanently\";}' /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
