class TestClass():
  def instance_method(self):
    return "This is method"

obj = TestClass()
print(obj.instance_method())
print(dir(obj))

def new_method(self):
  return "This is new method"

setattr(TestClass, 'new_method' ,new_method)

print(dir(obj))
print(obj.new_method())