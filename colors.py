BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print("\nEJEMPLO 1: Este texto será normal")
print("\033[34m Este texto es azul \033[39m")

print("\nEJEMPLO 2: Este texto será normal")
print(GREEN+"Este texto será verde"+RESET)
print("Queda mucho más entendible el código del print anterior cierto?")

print(YELLOW+"\nEJEMPLO 3: Este texto será amarillo"+RESET)
print(GREEN+"No te olvides de poner el RESET")
print("o seguira pintando del mismo color"+RESET)
print("Te gustó?")