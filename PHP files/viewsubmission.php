<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result=mysql_query("select * from solution where s_id in (select s_id from submits where username='" .$_SESSION['username']. "')");
$num=mysql_numrows($result);
?>
<table>
<tr>
<td>
Id
</td>
<td>
Question
</td>
<td>
Date
</td>
<td>
Time
</td>
<td>
Language
</td>
<td>
Status
</td>
</tr>
<?php
$i=0;
while ($i < $num)
{
	$f0=mysql_result($result,$i,"s_id");
	$query=mysql_query("select q_code from solution_of where s_id='$f0'");
	$f1=mysql_fetch_array($query);
	$f2=mysql_result($result,$i,"s_date");
	$f3=mysql_result($result,$i,"s_time");
	$f4=mysql_result($result,$i,"language");
	$f5=mysql_result($result,$i,"status");
	?>
	<tr>
	<td>
	<?php echo $f0; ?>
	</td>
	<td>
	<?php echo $f1['q_code']; ?>
	</td>
	<td>
	<?php echo $f2; ?>
	</td>
	<td>
	<?php echo $f3; ?>
	</td>
	<td>
	<?php echo $f4; ?>
	</td>
	<td>
	<?php echo $f5; ?>
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