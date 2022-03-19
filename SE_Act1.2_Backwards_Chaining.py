o1 = ['A', 'B', 'C']
o2 = ['A', 'M', 'Y']
o3 = ['A', 'B', 'D']
o4 = ['D', 'X', 'C']
objetos = [o1, o2, o3, o4]

def experto():
  res = ""
  isObject = False

  for i in range (0, len(objetos)):
    for j in range (0, len(objetos[i])):
      res = input("¿Tiene '{0}'? ".format(objetos[i][0]))
      if res == "si":
        if j == len(objetos[i]):
          print("Es el objeto "+ (i+1))
        else:
          j += 1
      else:
        i += 1

#while True:
print('________ Objetos ________')
for i in range (0, len(objetos)):
  print('Objeto {0}: {1}'.format(i+1, objetos[i]))
#print(len(objetos))
print('\n')
experto()