import sys
from datetime import datetime as dt

def end(message, starttime):
    print(message)
    print(f"Total gametime elapsed: {dt.now() - starttime}")
    sys.exit()
    
