import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

iUltimoOutputComporta1 = 0
iUltimoOutputComporta2 = 0
iUltimoOutputComporta3 = 0

while(True):
	
	bChangedState = False
	
	try:
		arq = open('/home/pi/Desktop/Barragem/barragem_input_control.txt', 'r')
	except FileNotFoundError:
		arq = open('/home/pi/Desktop/Barragem/barragem_input_control.txt', 'w')
		arq.write('0|0|0')
		arq = open('/home/pi/Desktop/Barragem/barragem_input_control.txt', 'r')
		bChangedState = True

	comando = arq.read().split("|")
	
	if len(comando) < 3:
		continue
	
	iOutputComporta1 = int(comando[0])
	iOutputComporta2 = int(comando[1])
	iOutputComporta3 = int(comando[2])
	
	if iUltimoOutputComporta1 != iOutputComporta1:
		iUltimoOutputComporta1 = iOutputComporta1
		bChangedState = True
		
	if iUltimoOutputComporta2 != iOutputComporta2:
		iUltimoOutputComporta2 = iOutputComporta2
		bChangedState = True
		
	if iUltimoOutputComporta3 != iOutputComporta3:
		iUltimoOutputComporta3 = iOutputComporta3
		bChangedState = True
	
	
	if bChangedState == True:
		print('Comporta 1: ', comando[0])
		print('Comporta 2: ', comando[1])
		print('Comporta 3: ', comando[2])

	#controle das saidas do rasp
	GPIO.output(16, int(comando[0]))
	GPIO.output(18, int(comando[1]))
	GPIO.output(22, int(comando[2]))
		
	time.sleep(0.1)
	arq.close()

	
