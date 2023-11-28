#!/usr/bin/env ruby

# Check if the log file path is provided
if ARGV.empty?
  puts "Usage: ruby 100-textme.rb <log_file>"
  exit
end

# Get the log file path
log_file = ARGV[0]

# Read the log file
log_data = File.read(log_file)

# Define the regular expression pattern
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Extract sender, receiver, and flags using the pattern
matches = log_data.scan(pattern)

# Output the results
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
