#!/usr/bin/pup
# Install a certain flask version

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}
