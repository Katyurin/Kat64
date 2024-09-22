from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(96, 4)
result2 = fake_divide(5, 0)
result3 = true_divide(94, 6)
result4 = true_divide(51, 2)

print(result1)
print(result2)
print(result3)
print(result4)