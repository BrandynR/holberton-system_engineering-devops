# Removes password authentication
file_line { 'passwd auth':
          path    => '/etc/ssh/ssh_config',
          line    => 'PasswordAuthentication no',
}

#Declare identity file
file_line { 'identity file':
          path       => '/etc/ssh/ssh_config',
          line       => 'IdentityFile ~/.ssh/holberton',
}
