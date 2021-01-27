import os
from datetime import datetime
from datetime import date
#huamos a guachar que pása jajaja
date=date.today()
#ya se sabse qie esyao dsera aborrasd

a=0

archivo = open("arhivo.csv","w")




while a == 0:

    i_vf=int(input("ingresa el valor anterior de medidor cfe: "))
    i_ff=int(input("ingresa el valor actual de medidor cfe: "))
    i_v=int(input("ingresa el valor anterior de medidor generico: "))
    i_f=int(input("ingresa el valor actual de medidor generico: "))


    precio=float(input("ingresa el precio de recibo cfe:"))#417
    precio=precio+1
    resutadocfe=i_ff-i_vf#300 kilowats totales
    resutadog=i_f-i_v#77 kilowatts verdura
    resutadot=resutadocfe-resutadog#223 kilowats paletas

    res=(resutadog*100)/resutadocfe
    rest=res*0.01
    ramon=precio*rest
    ramon=int(ramon)
    print("precio a pagar persona local A(Verdura)\n","$",ramon)
    res=(resutadot*100)/resutadocfe
    rest=res*0.01
    ramon=precio*rest
    ramon=int(ramon)
    print("precio a pagar persona de local B(Donas)\n","$",ramon)
    print("Desea repetir el proceso?\n")
    print("Si:0")
    print("No:1")
    a=int(input("R="))

i_ff= str(i_ff)
i_f=str(i_f)
date=str(date)

archivo.write(i_ff)
archivo.write(",")
archivo.write(i_f)
archivo.write(",")
archivo.write(date)

archivo.close()