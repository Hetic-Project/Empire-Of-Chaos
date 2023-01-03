import time
def countDown(secs):
    while secs:
        m, s = divmod(secs, 60)
        sec_format = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        secs -= 1
        print(secs, "s")
    print('countDown finish !')    