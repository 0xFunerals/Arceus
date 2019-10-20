# -*- coding: utf-8 -*-
import subprocess, time

def killer(cmd):
    subprocess.call(cmd, shell=True)

orange = "\x1b[38;5;202m"
pink = "\x1b[38;5;201m"
purple = "\x1b[38;5;93m"

killer("pkill ldapscan; pkill ntpscan; pkill tftpscan; pkill ssdpscan; pkill portmapscan; pkill chargenscan; pkill sentinelscan; pkill netbiosscan; pkill mssqlscan; pkill ts3scan")
killer("pkill dnsscan; pkill snmpscan; pkill db2scan; pkill echoscan; pkill mdnsscan; pkill memcachescan; pkill ripscan; pkill reaperscan; pkill heartbeatscan; pkill arc-methodscan")

print(""+ pink +"╔═════════════════════════════════╗"+ pink +"╔═════════════════╗")
print(""+ pink +"║ "+ orange +"Succesfuly Killed the following "+ pink +"║"+ pink +"║    "+ orange +"Arceus I    "+ pink +" ║")
print(""+ pink +"╠═════════════════════════════════╣"+ pink +"║ "+ orange +"Process Killerv2"+ pink +"║")
print(""+ pink +"║ "+ orange +"ldap "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║"+ pink +"║ "+ orange +"Developer"+ pink +":"+ purple +" Cri  "+ pink +"║")
print(""+ pink +"║ "+ orange +"ntp "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner            "+ pink +"║"+ pink +"╚═════════════════╝")
print(""+ pink +"║ "+ orange +"tftp "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║")
print(""+ pink +"║ "+ orange +"ssdp "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║")
print(""+ pink +"║ "+ orange +"portmap "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner        "+ pink +"║")
print(""+ pink +"║ "+ orange +"chargen "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner        "+ pink +"║")
print(""+ pink +"║ "+ orange +"sentinel "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner       "+ pink +"║")
print(""+ pink +"║ "+ orange +"netbios "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner        "+ pink +"║")
print(""+ pink +"║ "+ orange +"mssql "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner          "+ pink +"║")
print(""+ pink +"║ "+ orange +"ts3 "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner            "+ pink +"║")
print(""+ pink +"║ "+ orange +"dns "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner            "+ pink +"║")
print(""+ pink +"║ "+ orange +"snmp "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║")
print(""+ pink +"║ "+ orange +"db2 "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner            "+ pink +"║")
print(""+ pink +"║ "+ orange +"echo "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║")
print(""+ pink +"║ "+ orange +"mdns "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner           "+ pink +"║")
print(""+ pink +"║ "+ orange +"memcache "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner       "+ pink +"║")
print(""+ pink +"║ "+ orange +"rip "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner            "+ pink +"║")
print(""+ pink +"║ "+ orange +"reaper "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner         "+ pink +"║")
print(""+ pink +"║ "+ orange +"heartbeat "+ pink +"{"+ purple +"IPHM"+ pink +"} "+ pink +"-"+ orange+" Scanner      "+ pink +"║")
print(""+ pink +"╚═════════════════════════════════╝")
# Normal Menu < No Color Codes
#╔═════════════════════════════════╗╔═════════════════╗
#║ Succesfuly Killed the following ║║    Arceus I     ║
#╠═════════════════════════════════╣║ Process Killerv2║
#║ ldap {IPHM} - Scanner           ║║ Developer: Cri  ║
#║ ntp {IPHM} - Scanner            ║╚═════════════════╝
#║ tftp {IPHM} - Scanner           ║
#║ ssdp {IPHM} - Scanner           ║
#║ portmap {IPHM} - Scanner        ║ 
#║ chargen {IPHM} - Scanner        ║
#║ sentinel {IPHM} - Scanner       ║
#║ netbios {IPHM} - Scanner        ║
#║ mssql {IPHM} - Scanner          ║
#║ ts3 {IPHM} - Scanner            ║
#║ dns {IPHM} - Scanner            ║
#║ snmp {IPHM} - Scanner           ║
#║ db2 {IPHM} - Scanner            ║
#║ echo {IPHM} - Scanner           ║
#║ mdns {IPHM} - Scanner           ║
#║ memcache {IPHM} - Scanner       ║
#║ rip {IPHM} - Scanner            ║
#║ reaper {IPHM} - Scanner         ║
#║ heartbeat {IPHM} - Scanner      ║
#╚═════════════════════════════════╝