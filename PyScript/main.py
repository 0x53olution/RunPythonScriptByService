import sys
import time
import datetime

if __name__ == "__main__":
    argument_error_message = """
This script takes takes parameters:
    1. Username
    2. Password
    3. Environment
"""
    if len(sys.argv) != 4:
        print(argument_error_message)
        time.sleep(5)
        sys.exit(1)
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    environment = str(sys.argv[3])
    creation_time = datetime.now()

    print("Creation time: " + str(creation_time.strftime("%d.%m.%y %H:%M:%S")))
    time.sleep(1000)
    print("Job done!")
