'''
Created on 30 de nov de 2018

@author: João Paulo Just Peixoto <joao.just@ifba.edu.br>
'''
#!/usr/bin/python3
# coding:utf-8
import serial   # pip install pyserial
import time
import urllib.request
import urllib.parse
debug = True

intervalo = 300 # Intervalo entre as medições em segundos
ser = 0

while True:
        try:
            # Abre a porta serial, caso não tenha sido aberta antes
            if not ser:
                ser = serial.Serial('COM16', 9600, timeout=0)

            # Faz a leitura e tratamento dos dados
            dados = ser.readline()
            linha = dados.decode("ansi")
            if ";" in linha:
                temp, um = linha.split(";")
                temp = eval(temp)
                um = eval(um)
                chuva = 0    # Para uso futuro
                if debug:
                    print("--\nTemperatura: %d ºC\nUmidade: %d %%\nChuva: %d" % (temp, um, chuva))

                # Monta a URL e envia os dados para o webservice
                params = urllib.parse.urlencode({'temp': temp, 'hum': um, 'rain': chuva})
                url = "http://just.pro.br/ifba_sensors.py?%s" % params
                conteudoweb = urllib.request.urlopen(url)
                time.sleep(intervalo - 1)
                
                # Limpa o buffer de entrada para fazer uma nova leitura
                ser.flushInput()
        except serial.SerialException:
            print("Erro ao fazer leitura serial.")
        except urllib.error.URLError:
            print("Erro ao fazer a requisição HTTP.")
        time.sleep(1)