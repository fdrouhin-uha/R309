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
                while data != 'disconnect' and data !='kill' and data!="reset": #"disconnect" command stop the connexion between the server and the client
                    data = conn.recv(1024).decode()
                    if data == "CPU":
                        p = psutil.cpu_percent(interval=1, percpu=True)
                        txt = ', '.join(map(str,p))
                        print(p) 
                        conn.send(txt.encode())
                    elif data =="RAM":
                        p = psutil.virtual_memory()
                        print(p)
                        conn.send(p.encode())
                    elif data == "NAME":
                        p = platform.node()
                        print(p)
                        conn.send(p.encode())
                    elif data == "OS":
                        if sys.platform == "linux":
                            p = platform.freedesktop_os_release()['PRETTY_NAME'] + platform.release()
                            print(p)
                            conn.send(p.encode())
                        else:
                            p = platform.system() + platform.release()
                            print(p)
                            conn.send(p.encode())
                    elif data =='IP':
                        if sys.platform == 'linux':
                            p = subprocess.Popen("ip a | grep inet | grep global | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
                            outs, errs = p.communicate()
                            txt = outs.decode().rstrip("\r\n")
                            print(txt)
                            conn.send(txt.encode())
                            print (f"E/R: {data}")
                    #execute command in the shell using the argument "data"
                    else:
                        p = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
                        try:
                            outs, errs = p.communicate(None, 10)
                        except subprocess.TimeoutExpired:
                            print(f"Timeout on command {data}")
                        else:
                            txt = outs.decode().rstrip("\r\n")
                            conn.send(txt.encode())
                            print (f"E/R: {data}")
                            print (f"E/R: {txt}")
                    
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