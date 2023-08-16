import socket

nomehost = input("Passe o dominio: ")
porta = [22, 80, 443]

try:

    for p in porta:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.8)
        scan = cliente.connect_ex((nomehost, p))
        if scan == 0:
            print("Porta aberta: ", p, socket.getservbyport(p))

except:
    print("Alvo inexistente")