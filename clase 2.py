
''' a = "fin"
b= ""
nombre= ""
cantidad = 0
precio= 0.0

while a!=nombre :
    print ("inserte los datos")
    nombre = input() 
    cantidad = int(input())
    precio = float(input())
    total=cantidad*precio
    respuestafinal= nombre +" a gastado "+str(total)
    print(respuestafinal.upper())
    t=respuestafinal.find("do")
    print(respuestafinal[t+3:])

a="hola mundo"
b=2
c=13.4
mander="c"
print(a[1:4])
indice = a.find("a")
print(a[indice+2:])
'''
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha() :
  print original
else:
  print "empty"