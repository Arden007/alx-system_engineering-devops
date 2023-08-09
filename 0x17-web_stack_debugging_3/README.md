# 0x17-web_stack_debugging_3

This Puppet manifest provides a solution for resolving the "500 Internal Server Error" that occurs when an HTTP GET request is made to an Apache web server, specifically within a WordPress environment. The error is addressed by targeting the 'wp-settings.php' file located in the '/var/www/html/' directory and replacing occurrences of 'phpp' with 'php'. The correction is achieved through the use of the 'exec' resource type in Puppet.

## Problem Description

When making an HTTP GET request to the Apache web server in a WordPress environment, a "500 Internal Server Error" is encountered. This error prevents the proper execution of the requested resource and negatively impacts the user experience.

## Solution

To address this issue, the provided Puppet code employs the 'exec' resource type to execute a command that performs a replacement operation within the 'wp-settings.php' file. The 'sed' command is utilized for this purpose. Specifically, occurrences of 'phpp' are replaced with 'php' in the mentioned file. This adjustment rectifies the problematic behavior causing the "500 Internal Server Error."

## Puppet Manifest Explanation

The Puppet code snippet is as follows:

```puppet
exec { 'replace':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
