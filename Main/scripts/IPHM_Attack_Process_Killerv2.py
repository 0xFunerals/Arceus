# -*- coding: utf-8 -*-
import subprocess, time

def killer(cmd):
    subprocess.call(cmd, shell=True)

orange = "\x1b[38;5;202m"
pink = "\x1b[38;5;201m"
purple = "\x1b[38;5;93m"
# v1
killer("pkill ldap; pkill ntp; pkill tftp; pkill ssdp; pkill portmap; pkill chargen; pkill netbios; pkill sentinel; pkill mssql; pkill ts3")
killer("pkill HUN-FUN; pkill ASS-CRK; pkill EFT-PWR; pkill PMP-PMP; pkill ZCH-CRI")
killer("pkill tcpabuse; pkill udpabuse; pkill dominate; pkill winsyn; pkill winseqid; pkill yubina; pkill prowin; pkill essyn; pkill csyn; pkill xsyn; pkill zsyn; pkill issyn; pkill nfobypass; pkill CF_Bypass; pkill ovhbypass; pkill bo4bypass")
# v2
killer("pkill dns; pkill snmp; pkill db2; pkill echo; pkill mdns; pkill memcache; pkill rip; pkill reaper; pkill heartbeat; pkill arc")
killer("pkill zap; pkill wizard; pkill bogus; pkill bogus; pkill rawudp; pkill udp_vse1; pkill udp_vse2; pkill grenade; pkill xanax; pkill frag; pkill arme; pkill omega")
killer("pkill tcp-psh; pkill tcp-rst; pkill tcp-fin; pkill tcp-xmas; pkill tcp-ack; pkill ejunk")

print(""+ pink +"╔═══════════════════════╗╔════════════════════╗╔════════════════════╗╔════════════════════╗")
print(""+ pink +"║ "+ orange +"Killed all processes  "+ pink +"║║ "+ orange +"vse "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║"+ orange +" dns "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"Arceus I - Beta 10 "+ pink +"║")
print(""+ pink +"╠═══════════════════════╣║ "+ orange +"telnet "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"snmp "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"IPHM/Amplification "+ pink +"║")
print(""+ pink +"║ "+ orange +"ldap "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║"+ orange +" tcpabuse "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"db2 "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║  "+ orange +"Process Killerv2  "+ pink +"║")
print(""+ pink +"║ "+ orange +"ntp "+ pink +"{"+ purple +"IPHM"+ pink +"}            ║║"+ orange +" udpabuse "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"echo "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║  "+ orange +" Developer"+ pink +": "+ purple +"Cri   "+ pink +"║")
print(""+ pink +"║ "+ orange +"tftp "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║"+ orange +" dominate "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"mdns "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║╚════════════════════╝")
print(""+ pink +"║ "+ orange +"ssdp "+ pink +"{"+ purple +"IPHM"+ pink +"}           ║║"+ orange +" winsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"memcache "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║")
print(""+ pink +"║ "+ orange +"portmap "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" winseqid "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"rip "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║")
print(""+ pink +"║ "+ orange +"chargen "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" yubina "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"reaper "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║")
print(""+ pink +"║ "+ orange +"sentinel "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║"+ orange +" prowin "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"heartbeat "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║╔════════════════════╗")
print(""+ pink +"║ "+ orange +"netbios "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" essyn "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"arceus "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"frag "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║")
print(""+ pink +"║ "+ orange +"mssql "+ pink +"{"+ purple +"IPHM"+ pink +"}          ║║"+ orange +" csyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"zap "+ pink +"{"+ purple +"IPHM"+ pink +"}         ║║ "+ orange +"arme "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║")
print(""+ pink +"║ "+ orange +"ts3 "+ pink +"{"+ purple +"IPHM"+ pink +"}            ║║"+ orange +" xsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"wizard "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"omega "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║")
print(""+ pink +"║ "+ orange +"HUN-FUN "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" zsyn "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║ "+ orange +"bogus "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"tcp-psh "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║")
print(""+ pink +"║ "+ orange +"ASS-CRK "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" issyn "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"rawudp "+ pink +"{"+ purple +"IPHM"+ pink +"}      ║║ "+ orange +"tcp-rst "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║")
print(""+ pink +"║ "+ orange +"EFT-PWR "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" ovhbypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"udp_vse2 "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"tcp-fin "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║")
print(""+ pink +"║ "+ orange +"PMP-PMP "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" cfbypass "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"udp_vse1 "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║║ "+ orange +"tcp-xmas "+ pink +"{"+ purple +"IPHM"+ pink +"}    ║")
print(""+ pink +"║ "+ orange +"ZCH-CRI "+ pink +"{"+ purple +"IPHM"+ pink +"}        ║║"+ orange +" nfobypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"grenade "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║║ "+ orange +"tcp-ack "+ pink +"{"+ purple +"IPHM"+ pink +"}     ║")
print(""+ pink +"║ "+ orange +"Gang <3               "+ pink +"║║ "+ orange +"bo4bypass "+ pink +"{"+ purple +"IPHM"+ pink +"}   ║║ "+ orange +"xanax "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║║ "+ orange +"ejunk "+ pink +"{"+ purple +"IPHM"+ pink +"}       ║")
print(""+ pink +"╚═══════════════════════╝╚════════════════════╝╚════════════════════╝╚════════════════════╝")
# Normal Menu < No Color Codes
#╔═══════════════════════╗╔════════════════════╗╔════════════════════╗╔════════════════════╗
#║ Killed all processes  ║║ vse {IPHM}         ║║ dns {IPHM}         ║║ Arceus I - Beta 10 ║
#╠═══════════════════════╣║ telnet {IPHM}      ║║ snmp {IPHM}        ║║ IPHM/Amplification ║
#║ ldap {IPHM}           ║║ tcpabuse {IPHM}    ║║ db2 {IPHM}         ║║  Process Killerv2  ║
#║ ntp {IPHM}            ║║ udpabuse {IPHM}    ║║ echo {IPHM}        ║║   Developer: Cri   ║
#║ tftp {IPHM            ║║ dominate {IPHM}    ║║ mdns {IPHM}        ║╚════════════════════╝
#║ ssdp {IPHM            ║║ winsyn {IPHM}      ║║ memcache {IPHM}    ║
#║ portmap {IPHM}        ║║ winseqid {IPHM}    ║║ rip {IPHM}         ║
#║ chargen {IPHM}        ║║ yubina {IPHM}      ║║ reaper {IPHM}      ║╔════════════════════╗
#║ sentinel {IPHM}       ║║ prowin {IPHM}      ║║ heartbeat {IPHM}   ║║ xanax {IPHM}       ║
#║ netbios {IPHM}        ║║ essyn {IPHM}       ║║ grenade {IPHM}     ║║ frag {IPHM}        ║
#║ mssql {IPHM}          ║║ csyn {IPHM}        ║║ zap {IPHM}         ║║ arme {IPHM}        ║
#║ ts3 {IPHM}            ║║ xsyn {IPHM}        ║║ wizard {IPHM}      ║║ omega {IPHM}       ║
#║ HUN-FUN {IPHM}        ║║ zsyn {IPHM}        ║║ bogus {IPHM}       ║║ tcp-psh {IPHM}     ║
#║ ASS-CRK {IPHM}        ║║ issyn {IPHM}       ║║ rawudp {IPHM}      ║║ tcp-rst {IPHM}     ║
#║ EFT-PWR {IPHM}        ║║ ovhbypass {IPHM}   ║║ udp_vse2 {IPHM}    ║║ tcp-fin {IPHM}     ║
#║ PMP-PMP {IPHM}        ║║ cfbypass {IPHM}    ║║ udp_vse1 {IPHM}    ║║ tcp-xmas {IPHM}    ║
#║ ZCH-CRI {IPHM}        ║║ nfobypass {IPHM}   ║║ grenade {IPHM}     ║║ tcp-ack {IPHM}     ║
#║ Gang <3               ║║ bo4bypass {IPHM}   ║║ zap {IPHM}         ║║ ejunk {IPHM}       ║
#╚═══════════════════════╝╚════════════════════╝╚════════════════════╝╚════════════════════╝