# class list(list):
#   def each(self, callback):
#     list(map(callback, self))
#     return self

#   def each_with_index(self,callback):
#     list(map(callback, self, range(0,len(self))))
#     return self

list1 = list([1,2,3,4,5,6,7,8,9])

# def method(n, index):
#   print(f"Index:{index} {n*n}")

# print(list1.each_with_index(method))

for num, index in enumerate(list1):
  print(f"Index:{index} {num*num}")