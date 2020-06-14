class TestClass():
  def instance_method(self):
    return "This is method"

obj = TestClass()

def new_method(self):
  return "This is new method"

setattr(TestClass, 'new_method' ,new_method)
print(obj.new_method())

