array = [1,2,3,4,5,6,7,8,9]

array.each_with_index do |num, index|
  puts "Index: #{index} #{num*num}"
end