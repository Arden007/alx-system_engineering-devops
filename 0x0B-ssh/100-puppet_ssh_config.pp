# Configure ssh file to connect to server without password using puppet scripting
include stdlib

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare Identity file':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/ssh-key/ssh-key',
  replace => true,
}
