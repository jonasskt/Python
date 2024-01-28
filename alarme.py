from datetime import datetime
import time



while True:
    time.sleep(1)
    a = datetime.now()
    print(a)
    
    if a.minute == 42:
        print("ALRME TOCANDO") 
        break
        





                


        

    