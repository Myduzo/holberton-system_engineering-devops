#!/usr/bin/env ruby
SENDER =  ARGV[0].scan(/(?<=\[from:)[^ ]+(?=\])/).join
RECIEVER =  ARGV[0].scan(/(?<=\[to:)[^ ]+(?=\])/).join
FLAGS =  ARGV[0].scan(/(?<=\[flags:)[^ ]+(?=\])/).join
puts "#{SENDER},#{RECIEVER},#{FLAGS}"
