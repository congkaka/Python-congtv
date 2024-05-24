''' ---------------------** Congkaka python **----------------------- '''
print(__doc__)

list = [11, 2 , 3 , 4, 'Congkaka']

for index in enumerate(list):
  print(index)

# kế thừa trong python
class Parent:
  def __init__(self, name, age, address) -> None:
    # super().__init__()
    self.age = age
    self.name = name
    self.address = address

  def __str__(self):
    return f'Congkaka parent => {self.name}-{self.address}:{self.age}'


class Student(Parent):
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address
  # def __str__(self):
  #   return 'Congkaka => ' + self.name
  
  def age(self):
    return self.age
  
  def showInfo(self):
    print(f''' 
      Name: {self.name}
      age: {self.age}
      address: {self.address}
    ''')
    return True

studen_one = Student('congkaka', 29, "TB")

print(studen_one.name, studen_one.age)
print(studen_one.showInfo())
print(studen_one.age)
print(studen_one)
print('======================*===============================')


fp = open('test.txt', mode= 'a')
# fp.write("\nCongkaka-W-v1")
fp.write('\n'.join(map(str, list)))

fp.close()

file = open("test.txt", mode = 'r')

data = file.read()
print(data)
print('---------------------*------------------')
print('\n')

file.close()
