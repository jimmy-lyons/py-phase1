my_list = ["Cat", "Mouse", "Frog"]

my_list.insert(1, my_list.pop(0))
my_list.insert(1, "Lynx")

print(my_list)

my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

for i in my_list:
  if i.lower() in counters:
    counters[i.lower()] += 1
  else:
    counters[i.lower()] = 1

print(counters)