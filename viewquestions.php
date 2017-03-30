<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result=mysql_query("select * from question where q_code in (select q_code from writes where username='" .$_SESSION['username']. "')");
$num=mysql_numrows($result);
?>
<table>
<tr>
<td>
Question
</td>
<td>
Difficulty
</td>
<td>
Tags
</td>
<td>
Present On
</td>
</tr>
<?php
$i=0;
while ($i < $num)
{
	$f0=mysql_result($result,$i,"q_code");
	$f1=mysql_result($result,$i,"difficulty");
	$query=mysql_query("select tag from tags where q_code='$f0'");
	$query2=mysql_query("select domain from exists_on where q_code='$f0'");
	?>
	<tr>
	<td>
	<?php echo $f0; ?>
	</td>
	<td>
	<?php echo $f1; ?>
	</td>
	<td>
	<?php 
	while($f2=mysql_fetch_array($query))
		echo $f2['tag'].' '; 
	?>
	</td>
	<td>
	<?php 
	while($f3=mysql_fetch_array($query2))
		echo $f3['domain'].' '; 
	?>
	</td>
	</tr>
	<?php
	$i++;
}
mysql_close();
?>
</table>
</body>
</html>