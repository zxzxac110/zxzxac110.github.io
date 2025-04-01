a = 1
b = 2
def abc(a,b):
  t = a
  a = b
  b = t
  print(a)
  return 0

abc()
print(a)
print(b) 
