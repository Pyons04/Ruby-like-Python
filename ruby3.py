class list(list):
  def maps(self, callback):
    return list(map(callback, self))

def method(arg):
  return arg*arg

array = list([1,2,3,4,5,6,7,8,9])
#print(array.maps(method))

# array = list([1,2,3,4,5])
print(array.maps(lambda n:n*n))


# print(type(array))
# array2 = [1,2,3,4,5,6,7,8,9]
# print(type(array2))