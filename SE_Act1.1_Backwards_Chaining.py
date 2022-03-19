o1 = ['A', 'B', 'C']
o2 = ['A', 'M', 'Y']
o3 = ['A', 'B', 'D']
o4 = ['D', 'X', 'C']
objetos = [o1, o2, o3, o4]

def experto():
  false = True
  for i in range(0, len(objetos)):
    res = input("¿Tiene '{0}'? ".format(objetos[i][0]))
    
    if (res.lower() == "si"):
      res = input("¿Tiene '{0}'? ".format(objetos[i][1]))
      
      if(res.lower() == "si"):
        res = input("¿Tiene '{0}'? ".format(objetos[i][2]))
        if (res.lower() == "si"):
          print("Es el objeto {0}.".format(i+1))
          false = False
          break
        # No contiene el atributo 3
        else:
          i += 1
      # No contiene el atributo 2
      else:
        i += 1
    # No contiene el atributo 1
    else:
      i += 1

  if false:
    print("No es ninguno de los objetos conocidos.")

while True:
  print('\n________ Objetos ________')
  for i in range (0, len(objetos)):
    print('Objeto {0}: {1}'.format(i+1, objetos[i]))
  #print(len(objetos))
  print('\n')
  experto()