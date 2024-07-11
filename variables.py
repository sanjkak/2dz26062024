name = 'Ноутбук Asus'
memory = 512
chactota = 3.44


itogskill = 4
status = None

if itogskill >= 4 and itogskill <= 5:
  status = True
  print("Ты отличник")
elif itogskill >5:
  print('Такого не может быть')
else:
  status = False
  print("Ты не отличник")

print(type(status))
print(type(name))
print(type(memory))
print(type(chactota))

print(status)

