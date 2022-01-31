#*********************************************************************************
# Filename: measure CPU temp&freq.py
# Projekt  : Raspberry Pi CPU temperature and frequency monitor
# Hardware : Raspberry Pi 4, Raspberry Pi Zero 2 W
#
# Description:
# The script reads out the temperature and frequency of the CPU
# and prints their values to the terminal.
#
# Date:       Author:           Version
# 04.01.2021  Thomas S. Perri   V1.1
#*********************************************************************************

import os
import time

def measure_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

def measure_cpuVolt():
    cpu_volt = os.popen("vcgencmd measure_volts core").readline()
    return cpu_volt.replace("volt=", "")

def measure_freq():
    cpu_freq = os.popen("vcgencmd measure_clock arm").readline()
    return cpu_freq.replace("freq=", "")

def clear():
    clear = os.popen("clear").readline()
    return clear.replace("clear=", "")

while True:
    print("-------------")
    print(measure_temp())
    print(measure_freq())
    print(measure_cpuVolt())
    print("-------------")
    time.sleep(1)
    print(clear())
    time.sleep(0.1)


