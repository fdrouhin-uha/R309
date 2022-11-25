#!/usr/bin/env python3
import subprocess
import asyncio
# This is our shell command, executed by Popen.
x = str(input("commande: "))
p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)

print(p.communicate())