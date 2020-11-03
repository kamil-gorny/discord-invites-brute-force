import socket
import ssl 
import itertools
import select
from sys import argv
from  lxml import html
from selenium import webdriver


def main():
    script, method = argv
    if(method=='socket_method'):
        socket_method()
    elif(method=='selenium_method'):
        selenium_method()
    else:
        print('Niepoprawna nazwa methody')
        exit()



def socket_method():
    target_host = "www.discord.com"
    target_port = 443
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    client = ssl.wrap_socket(client, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    bruteforce_link(client)

def bruteforce_link(client):
    # x = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',repeat = 8)
    x = ['VTMAMg5B', '6UaBjvRD', 'Twoj234s', 'dsaGe2c4', 'DF43vDsK', '7zWErt8B', 'Kd5Vc3fX','6UaBjvRD']
    for i in x:
        # client.send(("GET /invite/{} HTTP/1.1\r\nHost: discord.com\r\nContent-Type: text/html\r\n\r\n".format(''.join(i))).encode())
        print("Sending request")
        client.send(("GET /invite/{} HTTP/1.1\r\nHost: discord.com\r\nContent-Type: text/html\r\n\r\n".format(i)).encode())
        print("Request sent")
        decode_response_and_write_to_file(get_full_response(client))
        check_if_invitation_is_valid('responsefile.txt', ''.join(i))

def get_full_response(client):
    print("Getting full response")
    response_list = []
    for i in range(7):
            print(f"Getting full response:{i}")
            client.recv(4096)
            # response_list.append(client.recv(4096))
    return response_list

def decode_response_and_write_to_file(responses):
    responsefile = open('responsefile.txt', 'w')

    for response in responses:
        responsefile.write(response.decode('utf-8')+'\n')
    responsefile.close()


def check_if_invitation_is_valid(file_name, link):
    with open(file_name, 'r') as read_obj:
        a=0
        for line in read_obj:
            if 'Join' in line:
                parse_server_name(line, link)
                a = 1
                break
        if a != 1:
            print("Niepoprawne zaproszenie")        

def parse_server_name(response_line, link):
    server_name = " ".join(html.fromstring(response_line).xpath('//@content')[0].split(" ")[2:-2])
    print(f"Nazwa serwera: {server_name}\tAdres: www.discord.com/invite/{link}")

main()
