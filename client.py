  
import socket
import sys

FORM='utf-8'

if(sys.argv[1]=='-h'):
    host=sys.argv[2]
if(sys.argv[3]=='-p'):
    port=int(sys.argv[4])

addres=(host,int(port))

if(sys.argv[7]=='-f'):
    if(sys.argv[8]=='tcp'):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            client.connect(addres)
            print(f"Connect to the server {addres}")
        except:
            print(f"Couldn't connect {addres}")


        if(sys.argv[5]=='-d'):
            msg=sys.argv[6]
            print(f"Send data : {msg}")
            with open(msg,"r") as f:
                content=f.read()
                client.send(msg.encode(FORM))
                client.send("-".encode(FORM))
                client.send(str(content).encode(FORM))
        serv_resp=client.recv(1024).decode(FORM)
        print(serv_resp)
    elif(sys.argv[8]=='udp'):
        client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        if(sys.argv[5]=='-d'):
            msg=sys.argv[6]
            print(f"Send data : {msg}")
            with open(msg,"r") as f:
                content=f.read()
                client.sendto(msg.encode(FORM),addres)
                client.sendto("-".encode(FORM),addres)
                client.sendto(str(content).encode(FORM),addres)
        serv_resp=client.recvfrom(1024)
        print(serv_resp[0].decode(FORM))
    else:
        print("Error occured")




