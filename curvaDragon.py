def curva(n):
    if n == 0: #Si no hay elementos nregresa una lista vavia  
        return []
    else:
        c = curva(n - 1) #Cadena de la curva del Dragon
        r = c[::-1] #Cadena reversa de la curva
        i = ['L' if g == 'R' else 'R' for g in r] # Cadena de r, que hace los giros, y convierte cada L en R y cada Rpor L
        return  c + ['L'] + i #Se concatenan los las 3 variables
        
def curvaDelDragon():
	curvas = int(input("Cuantas curvas quieres?: "))
	for i in range(1,curvas+1):
		print(curva(i))

curvaDelDragon()		

# CurvaDelDragon
