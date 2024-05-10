# Install puppet-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# Set PATH environment variable
file_line { 'set_path':
  path    => '/etc/environment',
  line    => 'PATH=$PATH:/usr/local/bin',
  match   => '^PATH=',
  ensure  => present,
  require => Package['Flask']
}
