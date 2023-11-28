#!/usr/bin/env ruby

log_data = ARGV[0]

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(?<sender>[\w\d\+\-]+)\] \[to:(?<receiver>[\w\d\+\-]+)\] \[flags:(?<flags>[\w\d:\-]+)\]/

match_data = log_data.match(regex)

if match_data
  sender = match_data[:sender]
  receiver = match_data[:receiver]
  flags = match_data[:flags]
  
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found in the log data."
end
