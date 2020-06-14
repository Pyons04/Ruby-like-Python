class int(int):  
  def times(self, callback):
    for times in range(0,self):
      callback()

class list(list):
  def maps(self, callback):
    return list(map(callback, self))

  def each(self, callback):
    list(map(callback, self))
    return self

  # index will sent to the function as a second parameter.
  def each_with_index(self,callback):
    list(map(callback, self, range(0,len(self))))
    return self

# Make sure you initialize object with class name.
# Ex: int(10).times, array = list([1,2,3,4,5])