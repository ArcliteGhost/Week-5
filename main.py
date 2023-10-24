#Creating a Class
#By Casey Eads

class Person:
  
  def __init__(self):
    self.name ="n/a"
    self.age = 0
    self.weight = 0.0

  def print_person(self):
    print(f'  Name: {self.name}')
    print(f'  Age: {self.age}')
    print(f'  Weight: {self.weight} lbs.')

if __name__ == "__main__":
  person1 = Person()
  person1.name = "Casey"
  person1.age = 30
  person1.weight = 248.6
  person1.print_person()
  
  person2 = Person()
  person2.name = "John"
  person2.age = 31
  person2.weight = 146.3
  person2.print_person()