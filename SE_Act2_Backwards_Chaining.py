o1 = ['A', 'B', 'C']
o2 = ['A', 'M', 'Y']
o3 = ['D', 'X', 'C']
o4 = ['A', 'B', 'D']
objetos = [o1, o2, o3, o4]

buscados = []


def fse():
    res = ""
    isObject = False
    fin = 0

    for i in range(0, len(objetos)):
        for j in range(0, len(objetos[i])):
            print(f"{j}")
            buscados.append(objetos[i][j])
            res = input("¿Tiene {0} ?: ".format(objetos[i][j]))
            if res != "si":
                j = 0  # inicia elemento de lista actual
                i += 1  # cambia de numero de lista
            else:
                if j == 2:
                    print("Es el objeto {0} ".format(i + 1))
                    fin = 1
                    break
                else:
                    j += 1
        if fin==1:
            break

for x in range(0, len(buscados)):
    print(buscados[x])


if __name__ == '__main__':
    fse()
