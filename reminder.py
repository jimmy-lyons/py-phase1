class Reminder:
  def __init__(self, name):
    self.name = name
    self.event = ""

  def remind_me_to(self, string):
    self.event = string

  def remind(self):
    return f'{self.name}! {self.event}!'


reminder = Reminder("Kay")

reminder.remind_me_to("Walk the dog")

print(reminder.remind())