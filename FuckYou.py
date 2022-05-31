from colorama import Fore, init
import requests
import time,sys
import random
import os

#  diseño


rojo = Fore.RED
V = Fore.GREEN
amarillo = Fore.YELLOW
blanco = Fore.WHITE
cyan = Fore.CYAN
violeta = Fore.MAGENTA


# diseño portada


print(f"""{V}
╔═══╗╔╗─╔╗╔═══╗╔╗╔═╗╔╗──╔╗╔═══╗╔╗─╔╗
║╔══╝║║─║║║╔═╗║║║║╔╝║╚╗╔╝║║╔═╗║║║─║║
║╚══╗║║─║║║║─╚╝║╚╝╝─╚╗╚╝╔╝║║─║║║║─║║
║╔══╝║║─║║║║─╔╗║╔╗║──╚╗╔╝─║║─║║║║─║║
║║───║╚═╝║║╚═╝║║║║╚╗──║║──║╚═╝║║╚═╝║
╚╝───╚═══╝╚═══╝╚╝╚═╝──╚╝──╚═══╝╚═══╝

""")

msg = input("cargando opciones....")
print(msg)
time.sleep(4)


if os.name == "posix":
   os.system ("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")
   
   
   
print(f"""
{rojo}

╔═╗╔═╗╔═╗╔══╗╔═╗╔═╦╗╔═╗╔══╗
║║║║╬║║╔╝╚║║╝║║║║║║║║╦╝║══╣
║║║║╔╝║╚╗╔║║╗║║║║║║║║╩╗╠══║
╚═╝╚╝─╚═╝╚══╝╚═╝╚╩═╝╚═╝╚══╝

{rojo}

{blanco}

[ 1 ] Fuerza bruta a un Correo electronico
[ 2 ] Fuerza bruta a una cuenta de Facebook
[ 3 ] Fuerza bruta a una cuenta de Instagram
""")

opc = int(input("coloca la opcion == "))
if not True:
    print("x/x")
else:
    msg = "cargando opcion..."
    print(msg)
    time.sleep(2)
    
if os.name == "posix":
   os.system ("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")


