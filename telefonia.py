#nombre = str(input("Ingrese el nombre del cliente: "));
min_nac = int(input("Ingrese los minutos nacionales consumidos: "));
min_int = int(input("Ingrese los minutos internacionales consumindos: "));
suma = min_nac + min_int;
total=0;
if (suma<=25):
    print("Minutos gratis");
elif (min_nac<=25):
    acu=min_nac-25;
    min_int+=acu;
    total=min_int*2.5;
else:
    min_nac-=25;
    total=(min_nac*0.5)+(min_int*2.5);
print("Total a pagar Q",total)