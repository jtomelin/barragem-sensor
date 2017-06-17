import RPi.GPIO as GPIO
import time

#while(True):
	#arq = open('/home/pi/Desktop/Barragem/lista.txt', 'w')
	#texto = "1";
	#arq.write(texto)
	#time.sleep(2)
	#arq.close()

while(True):
	
	comando1 = "99"
	comando2 = "99"
	comando3 = "99"
	
	while(comando1 != "0" and comando1 != "1"):
		comando1 = input('Insira 0 para fechar 1 para abrir a Comporta 1: ')
		
	while(comando2 != "0" and comando2 != "1"):	
		comando2 = input('Insira 0 para fechar 1 para abrir a Comporta 2: ')
	
	while(comando3 != "0" and comando3 != "1"):
		comando3 = input('Insira 0 para fechar 1 para abrir a Comporta 3: ')
		
	arq = open('/tmp/barragem_input_control.txt', 'w')
	
	arq.write(comando1 + '|' + comando2 + '|' + comando3)
	arq.close()
