#!/usr/bin/env python3
import subprocess,psutil,platform,sys

x = ""
while x != "bye":
    x = str(input("commande: "))
    
    if x != "bye":
        if x == 'cpu':
           p = psutil.cpu_percent(interval=1, percpu=True)
           txt = ', '.join(map(str,p))
           print(p)
           print(txt)
        elif x == "NAME":
            p = platform.node() 
            print(p)
        elif x =="RAM":
                p = psutil.virtual_memory()
                print(p)
        elif x == "OS":
            if sys.platform == "linux":
                p = platform.freedesktop_os_release()['PRETTY_NAME'],platform.release()
                print(p)
            else:
                p = platform.system()
                o = platform.release()
                print(p,o)
        elif x =='IP':
            if sys.platform == 'linux':
                p = subprocess.Popen("ip a | grep inet | grep global | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
                outs = p.communicate()
                txt = outs.decode().rstrip("\r\n")
                print(txt)
            else:
                pass
        else:
            p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)
            try:
                outs, errs = p.communicate(None, 10)
            except subprocess.TimeoutExpired:
                print(f"Timeout on command {x}")
            else:
                txt = outs.decode().rstrip("\r\n")
                print(txt)