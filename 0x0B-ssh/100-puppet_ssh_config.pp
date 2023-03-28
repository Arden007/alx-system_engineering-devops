# Configure ssh file to connect to server without password using puppet scripting
include stdlib

file_line { 'Turn off password auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Identity file':
  ensure => 'present',
  path => '/etc/ssh/ssh_config'
  line => '    IdentityFile ~/.ssh/school',
  replace => true,
}
