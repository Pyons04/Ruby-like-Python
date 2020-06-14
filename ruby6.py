class int(int):  
  def times(self, callback):
    for times in range(0,self):
      callback()

print(type(int(10))) # <class '__main__.int'>
print(type(10))      # <class 'int'>