class Introducer:
  def __init__(self, name):
    self.name = name

  def announce(self):
    return f"I am {self.name}"

  def introduce(self, name):
    return f"Hello {name}, I'm {self.name}"


introducer = Introducer("Kay")

print(introducer.announce())

print(introducer.introduce("Fred"))
