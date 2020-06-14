class int(int):  
  def times(self, callback):
    for times in range(0,self):
      callback()

def print_10():
  print('Hello World')

int(10).times(print_10)