import time
seconds = int(time.time())

if seconds % 15 == 0:
  print("fizzbuzz")
elif seconds % 3 == 0:
  print("fizz")
elif seconds % 5 == 0:
  print("buzz")
