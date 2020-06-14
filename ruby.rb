array = [1,2,3,4,5,6,7,8,9]
print(array.map{|x| x * x})


b = array.each do |a|
  a*a
end

print b