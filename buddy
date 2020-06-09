import psutil, os, time

found = 0

theprogram = 'stan_gfriend.exe'         # put name of program here, must be in same location

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

    time.sleep(5)                       # seconds between refreshes
    print ('sleeping')
    continue
