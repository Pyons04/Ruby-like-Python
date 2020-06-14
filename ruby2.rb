class TestClass
  def instance_method
    return "This is method"
  end
end

obj = TestClass.new

TestClass.class_eval {
  def new_method
    return "This is new method"
  end
}

puts obj.new_method