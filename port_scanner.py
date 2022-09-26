import pyfiglet
import socket
import threading
import time

print(pyfiglet.figlet_format("Port Scanner"))
print("[1] Enter")
print("[0] Exit\n")
option=input("[?] Enter your choice: ")
print()
socket.setdefaulttimeout(1)

def execute():
    ipaddr=""
    if host.upper()==host.lower():
        l=host.split(".")
        if len(l)!=4:
            print("Please check the IP address you entered.")
            quit()
        for i in l:
            if i!="":
                if int(i) not in range(256):
                    print("Please check the IP address you entered.")
                    quit()
            else:
                print("Please check the IP address you entered.")
                quit()
        ipaddr=host
    else:
        try:
            ipaddr=socket.gethostbyname(host)
            print("IP address : "+ipaddr)
        except Exception as e:
            print("Please check the hostname you entered.")
            quit()
    
    try:
        print("Connecting to", ipaddr, "...")
        socket.gethostbyaddr(ipaddr)
        print("Connected !")
    except Exception as e:
        print("\nThe host you entered is unreachable.")
        print("Connection Failed !")
        quit()
    return ipaddr

def scan(ipaddr, i):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.25)
    try:
        s.connect((ipaddr, i))
        print("Port", i,"is open")
        s.close()
    except Exception as e:
        pass



if option=="0":
    print("GOOD BYE!")
    quit()
elif option=="1":
    host=input("Enter target IP address or hostname: ")
    init_time=time.time()
    print()
    threads=[]
    ipaddr = execute()
    print("\nScanning ports of "+ipaddr+"\n")
    for i in range(65536):
        t = threading.Thread(target=scan, args=[ipaddr, i])
        t.start()
        threads.append(t)
    for i in threads:
        i.join()
    final_time=time.time()
    time_taken=final_time-init_time
    print("Scanned 65535 ports in", time_taken, "seconds")
    print("END OF SCAN")
else:
    print("Invalid Response !")
