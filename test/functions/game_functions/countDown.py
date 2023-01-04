import time

def countDown(secs):
    while secs:
        time.sleep(1)
        secs -= 1
        print(secs,"s")
    print('countDown finish !')    