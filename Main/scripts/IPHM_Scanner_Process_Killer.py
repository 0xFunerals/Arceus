# -*- coding: utf-8 -*-
import subprocess, time

def killer(cmd):
    subprocess.call(cmd, shell=True)

orange = "\x1b[38;5;202m"
pink = "\x1b[38;5;201m"
purple = "\x1b[38;5;93m"

killer("pkill ldapscan; pkill ntpscan; pkill tftpscan; pkill ssdpscan; pkill portmapscan; pkill chargenscan; pkill sentinelscan; pkill netbiosscan; pkill mssqlscan; pkill ts3scan")

print("\e[38;5;201m╔════════════════════════════════════════╗")
print("\e[38;5;201m║    \e[38;5;202mSuccesfuly Killed the following     \e[38;5;201m║")
print("\e[38;5;201m╠════════════════════════════════════════╣")
print("\e[38;5;201m║ \e[38;5;202mldap \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner    \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mntp \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner     \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mtftp \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner    \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mssdp \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner    \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mportmap \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mchargen \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202msentinel \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner\e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mnetbios \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mmssql \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner   \e[38;5;201m║")
print("\e[38;5;201m║ \e[38;5;202mts3 \e[38;5;201m{\e[38;5;93mIPHM\e[38;5;201m} \e[38;5;201m-  {\e[38;5;93mExternal\e[38;5;201m} \e[38;5;201m+ \e[38;5;202mScanner     \e[38;5;201m║")
print("\e[38;5;201m╚════════════════════════════════════════╝")


# Normal Menu < No Color Codes
#╔════════════════════════════════════════╗
#║    Succesfuly Killed the following     ║
#╠════════════════════════════════════════╣
#║ ldap {IPHM} -  {External} + Scanner    ║
#║ ntp {IPHM} -  {External} + Scanner     ║
#║ tftp {IPHM} -  {External} + Scanner    ║
#║ ssdp {IPHM} -  {External} + Scanner    ║
#║ portmap {IPHM} -  {External} + Scanner ║
#║ chargen {IPHM} -  {External} + Scanner ║                    
#║ sentinel {IPHM} -  {External} + Scanner║                     
#║ netbios {IPHM} -  {External} + Scanner ║                     
#║ mssql {IPHM} -  {External} + Scanner   ║                    
#║ ts3 {IPHM} -  {External} + Scanner     ║                     
#╚════════════════════════════════════════╝