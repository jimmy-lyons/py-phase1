def add_five(number):
  return number + 5

print(add_five(2132))

def subtract_low_from_high(num1, num2):
  return num1 - num2 if num1 > num2 else num2 - num1

print(add_five(subtract_low_from_high(1463, 16475)))

def superify(word):
  return "super" + word

print(superify("cat"))