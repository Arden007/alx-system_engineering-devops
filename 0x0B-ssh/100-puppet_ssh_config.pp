# Configure ssh file to connect to server without password using puppet scripting
file_line { 'Turn off password auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

file_line { 'Identity file':
  ensure => 'present',
  path => '/etc/ssh/ssh_config'
  line => '    PasswordAuthentication no',
}
