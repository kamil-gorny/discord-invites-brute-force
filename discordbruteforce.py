import socket
import ssl 
from  lxml import html


target_host = "www.discord.com"
target_port = 443
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client = ssl.wrap_socket(client, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

client.send("GET /invite/K6Yb3vDf HTTP/1.1\r\nHost: discord.com\r\nContent-Type: text/html\r\n\r\n".encode())

def check_if_invitation_is_valid(file_name):
    with open(file_name, 'r') as read_obj:
        a=0
        for line in read_obj:
            if 'Join' in line:
                parse_server_name(line)
                a = 1
                break
        if a == 1:
            print("Zaproszenie poprawne")    
        else:
            print("Niepoprawne zaproszenie")        


def parse_server_name(response_line):
    server_name = " ".join(html.fromstring(response_line).xpath('//@content')[0].split(" ")[2:-2])
    print(server_name)

def get_full_response(client):
    response_list = []
    for i in range(7):
        response_list.append(client.recv(4096))
    return response_list


def decode_and_write_to_file(responses):
    responsefile = open('responsefile2.txt', 'w')

    for response in responses:
        responsefile.write(response.decode('utf-8')+'\n')
    responsefile.close()


decode_and_write_to_file(get_full_response(client))
check_if_invitation_is_valid('responsefile2.txt')



