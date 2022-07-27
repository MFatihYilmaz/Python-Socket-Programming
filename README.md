# Python-Socket-Programming
Basic file transfer script with python on command shell 
it includes some file like CSIntern that doesnt matter.

## How to use ?

### Client

python3 client.py -h 192.168.1.10 -p 5678 -d CSIntern2022 -f tcp
Connected to server: 192.168.1.10:5678
Send data: CSIntern2020
Received data: ok.

python3 client.py -h 192.168.1.14 -p 5678 -d TestData1234 -f tcp
Connected to server: 192.168.1.14:1234
Send data: TestData1234
Received data: drop.

### Server 

python network_server -i 0.0.0.0 -p 5678 -f udp
Listening UDP on 0.0.0.0:5678
Accepted connection from: 192.168.1.12
Received data: CSIntern2020_tarik

python network_server -i 192.168.1.10 -p 1111 -f tcp
Listening TCP on 192.168.1.10:1111
Accepted connection from: 192.168.1.12
Received data: CSIntern2020_tarik
Send data: ok.

