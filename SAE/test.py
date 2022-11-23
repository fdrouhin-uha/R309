#!/usr/bin/env python3
import command

res = command.run(['ls']) 

print(res.output) 
print(res.exit)