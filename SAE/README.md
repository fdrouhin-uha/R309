# Documentation

/!\ all of the programs can be run in a command shell 



### serveur.py

This program must be run on the machine you want monitoring. 

To run it you need to specifie the IP address and the port connexion 

    ./serveur.py 192.168.0.19 10000

After that the server will wait for a connection.

When is up the server will execute all the command he will recevie 



### client.py

This program is the link between serveur.py and GUIhome.py he send and recevie all the messages from the serveur and display the result on the graphical interface.



/!\ client.py and GUIhome.py should run on the same machine 

### GUIhome.py

This is the graphical interface of the monitoring system. 

To use it you need to specifie the IP and the prot of the server 

When the connexion is up a second window will pop up


