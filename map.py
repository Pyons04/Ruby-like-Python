class list(list):
  def maps(self, callback):
    return list(map(callback, self))

# lambdaを利用する場合
array = list([1,2,3,4,5,6,7,8,9])
print(array.maps(lambda n:n*n))

#関数を引数にとるとき
def method(arg):
  return arg*arg
print(array.maps(method))
