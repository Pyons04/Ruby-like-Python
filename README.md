# Ruby-like-Python

#### 趣旨
PythonでRubyライクな文法を利用するためのラッパーの自作を通じて、Pythonメタプログラミングの理解を深める

#### 目次
* [Integer::times](#Integer::times)
* [Enumerable::map](#Enumerable::map)
* [Enumerable::each_with_index](#Enumerable::each_with_index)
* [Module::class_eval](#Module::class_eval)

## Integer::times

Rubyの以下の挙動をPythonで再現する

```ruby
10.times do 
  puts "Hello World"
end
```

Pythonでは以下のようにすると近い挙動を再現できる

```python
class int(int):  
  def times(self, callback):
    for times in range(0,self):
      callback()

def print_10():
  print('Hello World')

int(10).times(print_10)
```
```関数ポインタ```（メソッド名にカッコを付けず、関数オブジェクトとして渡す）を使うのがミソ。

実行結果
```
PS C:\Users\broad\OneDrive\products\Ruby-like-Python> python ruby2.py
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
```

```int()```を利用して数字オブジェクトを初期化しているが、こうしないと```times```メソッドは認識されない。また実際には普通の数字とは異なる型だと認識されてしまう。

```python
class int(int):  
  def times(self, callback):
    for times in range(0,self):
      callback()

print(type(int(10))) # <class '__main__.int'>
print(type(10))      # <class 'int'>
```

Rubyのように標準ライブラリの完全に継承してインスタンス化出来ているわけではなさそう。

## Enumerable::map

Rubyの以下の挙動をPythonで実装する。
```ruby
array = [1,2,3,4,5,6,7,8,9]
print(array.map{|x| x * x})
```

Pythonで実装するとこんな感じになる。
```python
class list(list):
  def maps(self, callback):
    return list(map(callback, self))

array = list([1,2,3,4,5,6,7,8,9])
print(array.maps(lambda n:n*n))
```

以下実行結果
```shell
PS C:\Users\broad\OneDrive\products\Ruby-like-Python> python ruby3.py
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

ラムダ式を利用しなくでも、関数を直接引数に指定することもできる。
```python
array = list([1,2,3,4,5,6,7,8,9])
print(array.maps(method))
```


なお、このラッパーに関してもリストオブジェクトの初期化は、通常の```[1,2,3,4,5]```ではなく、クラス名を指定した初期化を行わないと```maps()```が認識されない。

## Enumerable::each_with_index

Rubyの以下のような挙動をPythonで実装して見る

```ruby
array = [1,2,3,4,5,6,7,8,9]

array.each_with_index do |num, index|
  puts "Index: #{index} #{num*num}"
end
```

実行結果はこんな感じ
```shell
[pyons@LAPTOP-SF87NLCB Ruby-like-Python (master)]$ ruby ruby.rb
Index: 0 1
Index: 1 4
Index: 2 9
Index: 3 16
Index: 4 25
Index: 5 36
Index: 6 49
Index: 7 64
Index: 8 81
```
Pythonでの実装について検討する。

```each_with_index```と同じような処理はPythonならfor文だと比較的簡単に出来てしまう。
以下for文を用いた実装

```python
list1 = list([1,2,3,4,5,6,7,8,9])

for num, index in enumerate(list1):
  print(f"Index:{index} {num*num}")
```

ところがこの方法だと、Rubyでメソッドを利用していた人間からするとかなり不自然な挙動になる。

```shell
PS C:\Users\broad\OneDrive\products\Ruby-like-Python> python ruby4.py
Index:1 0
Index:2 1
Index:3 4
Index:4 9
Index:5 16
Index:6 25
Index:7 36
Index:8 49
Index:9 64
```
なぜかIndexが0から始まる上に、リストの最後尾が実行されないという謎仕様...

という訳で実装し直してみる。
```python
class list(list):
  def each(self, callback):
    list(map(callback, self))
    return self

  def each_with_index(self,callback):
    list(map(callback, self, range(0,len(self))))
    return self

list1 = list([1,2,3,4,5,6,7,8,9])

def method(n, index):
  print(f"Index:{index} {n*n}")

print(list1.each_with_index(method))
```

実行結果は以下の通り
```shell
PS C:\Users\broad\OneDrive\products\Ruby-like-Python> python ruby4.py
Index:0 1
Index:1 4
Index:2 9
Index:3 16
Index:4 25
Index:5 36
Index:6 49
Index:7 64
Index:8 81
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

こっちの方が期待通りな感じ。

## Module::class_eval

番外編。

これはPythonで標準についているメソッドをそのまま利用するだけ。ほとんどRubyと同じように操作できる。

```ruby
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
```
PythonでもRubyと同じように、インスタンス化済みのオブジェクトであっても新しく定義したインスタンスメソッドが利用可能。
```python
class TestClass():
  def instance_method(self):
    return "This is method"

obj = TestClass()

def new_method(self):
  return "This is new method"

setattr(TestClass, 'new_method' ,new_method)
print(obj.new_method())
```

実行結果
```shell
PS C:\Users\broad\OneDrive\products\Ruby-like-Python> python ruby5.py
This is new method
```