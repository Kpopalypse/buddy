import psutil, os, time, traceback, getpass

found = False
sleeptime = 10                                           # amount of time the program waits between reads

theprogram = 'connecttimer.exe'                          # the name of the process you want to check

the_user = getpass.getuser()                             # finds out the windows user profile name

try:

    while True:

        for process in psutil.process_iter():
            try:
                if process.name() == theprogram:         # breaks the loop if the program is found
                    found = True
                    print ('process found')
                    break
            except:
                print ('error')                          # tries again in a minute if another program interferes with the process
                time.sleep(100)
                continue
                
        if found == False:
            print ('process not found')                  # starts the program
            filepath = theprogram
            os.startfile(filepath)
            
        found = False

        time.sleep(sleeptime)
        print ('sleeping')
        continue

except:                                                  # prints traceback to a text file for debugging if there is a crash
    os.chdir("C://Users/" + the_user + "/desktop")
    with open("buddyerror.log", "a") as logfile:
        traceback.print_exc(file=logfile)
    raise   
