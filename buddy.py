import psutil, os, time, traceback, getpass

found = 0

theprogram = 'connecttimer.exe'

the_user = getpass.getuser()

try:

    while True:

        for process in psutil.process_iter():
            if process.name() == theprogram:
                found = 1
                print ('process found')
                

        if found == 0:
            print ('process not found')
            filepath = theprogram
            os.startfile(filepath)
            
        found = 0

        time.sleep(10)
        print ('sleeping')
        continue

except:
    os.chdir("C://Users/" + the_user + "/desktop")
    with open("buddyerror.log", "a") as logfile:
        traceback.print_exc(file=logfile)
    raise   
