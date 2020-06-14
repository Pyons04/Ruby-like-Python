class int(int):
  def __init__(self, args):
    self.num = args
  
  def times(self, callback):
    for times in range(0,self.num):
      callback()

def print_10():
  print('Ten!!')

int(10).times(print_10)
print(type(10))