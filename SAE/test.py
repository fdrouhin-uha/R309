#!/usr/bin/env python3
import subprocess

x = ""
while x != "bye":
    x = str(input("commande: "))
    
    if x != "bye":
        p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)

        try:
            outs, errs = p.communicate(None, 10)
        except subprocess.TimeoutExpired:
            print(f"Timeout on command {x}")
        else:
            txt = outs.decode().rstrip("\r\n")
            print(txt)