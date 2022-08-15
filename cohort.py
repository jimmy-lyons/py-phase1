cohort = ["Alex", "Anish", "Archie", "Erlantz", "Farzan", "Gawain", "George", "Jimmy", "Laura", "Luke", "Luiza", "Russel", "Sam", "Simon", "Stevie", "Tim", "Tom", "Slava"]

import string
d = dict.fromkeys(string.ascii_lowercase, 0)

for name in cohort:
  for letter in name:
    d[letter.lower()] += 1

print(d)