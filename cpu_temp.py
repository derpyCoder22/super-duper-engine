from subprocess import check_output
from re import findall
from time import sleep, strftime, time

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    temp = float(findall("\d+\.\d+",temp)[0])
    return(temp)

def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))    

while True:
    temp = get_temp()
    print(get_temp())
    write_temp(temp)
    sleep(1)
