num=int(input("Ingrese un numero entero: "));
if(num>0):
    mensaje="El numero es positivo";
elif(num==0):
    mensaje="El numero es neutro";
else:
    mensaje="El numero es negativo";
print(num,mensaje);