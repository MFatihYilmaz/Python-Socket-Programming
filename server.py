
import sys
import threading
import socket

if(sys.argv[1]=='-i'):
    HOST=sys.argv[2]
if(sys.argv[3]=='-p'):
    PORT=int(sys.argv[4])
ADDR=(HOST,PORT)
FORM='utf-8'
SIZE=1024
if(sys.argv[5]=='-f'):
    if(sys.argv[6]=='tcp'):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"Listening {sys.argv[6]} on {ADDR}")
        while True:
            conn,addr=server.accept()
            def handler(conn,addr):
                print(f"Accepted connection from {addr}")
                filename=str(conn.recv(1024).decode(FORM)).split("-")
                
                if(filename[0].startswith("CSIntern")):
                    print(f"Recieved data : {filename[0]}")
                    conn.send("Recieved data: ok".encode(FORM))
                    print("Send data:ok")
        
                    with open(filename[0],"w+") as f:
                        f.write(filename[1])
                        content=conn.recv(SIZE).decode(FORM)
                        f.write(content)
        
                else:
                    conn.send("Recieved data : drop".encode(FORM))
                    conn.close()
        
            thread=threading.Thread (target=handler,args=(conn,addr))
            thread.start()
        
            print(f"ACTivE CONNECTiON{threading.active_count()-1}") 
    

    elif(sys.argv[6]=='udp'):
        sserver=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sserver.bind(ADDR)
        
        def handlers():
            print(f"Listening UDP on {ADDR}")
            while True:
                data,addres=sserver.recvfrom(SIZE)
                print(data.decode(FORM))
                filesname=data.decode(FORM).split("-")
                if(filesname[0].startswith("CSIntern")):
                        print(f"Recieved data : {filesname[0]}")
                        sserver.sendto("Recieved data: ok".encode(FORM),addres)
                        print("Send data:ok")
            
                        with open(filesname[0],"w+") as f:
                            
                            content=data.decode(FORM)
                            f.write(content)
                    
            
                else:
                    sserver.sendto("Recieved data : drop".encode(FORM),addres)
                    sserver.close()
        thread=threading.Thread(target=handlers)
        thread.start()
             
            
    else:
        print("Error occured")






