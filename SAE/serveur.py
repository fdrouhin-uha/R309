#!/usr/bin/env python3
import sys, socket, subprocess
# info of the server
host= "127.0.0.1"
port= int(sys.argv[1])

#uping the server
server_s= socket.socket()
server_s.bind((host, port))
server_s.listen()
data=''
if __name__ == '__main__':
    try:
        while data != 'shut': #"shut" command shut down the server
            print("waiting !!")
            try:
                conn, address = server_s.accept()
                print("connected !!")
                data = ''
                while data != 'bye' and data !='shut': #"bye" command stop the connexion between the server and the client
                    data = conn.recv(1024).decode()
                    #execute command in the shell using the argument "data"
                    p = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)
                    try:
                        outs, errs = p.communicate(None, 10)
                    except subprocess.TimeoutExpired:
                        print(f"Timeout on command {data}")
                    else:
                        txt = outs.decode().rstrip("\r\n")
                        print(txt)
                        conn.send(txt.encode())
            except ConnectionResetError:
                print("connexion lost")
            except TimeoutError:
                print("time out")
            except BrokenPipeError:
                print("connexion broke")
            finally:
                conn.close()
    except PermissionError:
        print ("connexion port is not correct")
    finally:
        server_s.close()