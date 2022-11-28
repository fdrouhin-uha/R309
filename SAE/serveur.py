#!/usr/bin/env python3
import sys, socket, subprocess,psutil,platform
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
        while data != 'kill': #"kill" command shut down the server
            print("waiting !!")
            try:
                conn, address = server_s.accept()
                print("connected !!")
                data = ''
                while data != 'disconnect' and data !='kill': #"disconnect" command stop the connexion between the server and the client
                    data = conn.recv(1024).decode()
                    if data == "CPU":
                        p = psutil.cpu_percent(interval=1, percpu=True)
                        print(p) 
                    elif data =="RAM":
                        p = psutil.virtual_memory()
                        print(p)
                    elif data == "NAME":
                        p = platform.node()
                        print(p)
                    elif data == "OS":
                        if sys.platform == "linux":
                            p = platform.freedesktop_os_release()['PRETTY_NAME']
                            o = platform.release()
                            print(p,o)
                        else:
                            p = platform.system()
                            o = platform.release()
                            print(p,o)
                    #execute command in the shell using the argument "data"
                    else:
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