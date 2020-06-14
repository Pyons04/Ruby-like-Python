class ten():
  integer = 10
  def times(self, callback):
    for times in range(0,self.integer):
      callback()

ten_object = ten()

def print_10():
  print('Ten!!')

ten_object.times(print_10)

