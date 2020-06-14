class list(list):
  def each(self, callback):
    list(map(callback, self))
    return self

new_list = list([1,2,3,4,5,6,7,8,9])
new_array = []
def method(n):
  new_array.append(n*n)

print(new_list.each(method))
print(new_array)