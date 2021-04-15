import sys
import socket
from datetime import datetime

# if len(sys.argv) == 2:
#     target = socket.gethostbyname(sys.argv[1])
# else:
#     print("Invalid amount of arguements")

target = input("Δώσε IP: ")


print("-" * 50)
print("Στόχος: " + target)
print("Ώρα εκκίνησης" + str(datetime.now()))

try:
    for port in range(50, 10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result = s.connect_ex((target, port))#returns error indicator
        print("Τσεκάρω το πόρτ {}".format(port))
        if result == 0:
            print("Το πόρτ {} είναι ανοιχτό".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nΑκύρωση προγράμματος")
    sys.exit()


except socket.error:
    print("Η σύνδεση στο server δεν ήταν δυνατή")
    sys.exit()
