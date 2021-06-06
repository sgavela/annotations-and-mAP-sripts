contenido= list()
path_in = "C:/Users/Sergio Gil/Desktop/proces/valciu.txt"
path_out = "C:/Users/Sergio Gil/Desktop/proces/valciu_2.txt"
i = 0
with open(path_in, 'r') as archivo:
   for linea in archivo:
       columnas = linea.split(" ")
       nuevalinea = "data" + columnas[0][1:]
       contenido.append(nuevalinea+'\n')
with open(path_out, 'w') as archivo:
    archivo.writelines(contenido)




