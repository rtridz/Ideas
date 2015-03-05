import paramiko
import console

strComputer = 'ip/server_adress'
strUser = 'login'
strPwd = 'password'
strCommand = 'name_of_command'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=strComputer, username=strUser, password=strPwd)

stdin, stdout, stderr = client.exec_command(strCommand)
# эта строка необходима если мы хотим увидить на экране результат выполнения команды
print stdout.read()

client.close()
