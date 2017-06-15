import RPi.GPIO as GPIO
import time

#while(True):
	#arq = open('/home/pi/Desktop/Barragem/lista.txt', 'w')
	#texto = "1";
	#arq.write(texto)
	#time.sleep(2)
	#arq.close()

while(True):
	comando1 = input('Insira 0 para fechar 1 para abrir a Comporta 1: ')
	comando2 = input('Insira 0 para fechar 1 para abrir a Comporta 2: ')
	comando3 = input('Insira 0 para fechar 1 para abrir a Comporta 3: ')
	arq = open('/home/pi/Desktop/Barragem/barragem_input_control.txt', 'w')
	
	arq.write(comando1 + '|' + comando2 + '|' + comando3)
	arq.close()
