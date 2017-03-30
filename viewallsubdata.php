<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$qcode=$_POST['qcode'];

$result=mysql_query("select * from solution where s_id in (select s_id from solution_of where q_code='$qcode')");
$num=mysql_numrows($result);
?>
<table>
<tr>
<td>
Username
</td>
<td>
Solution Id
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
	$f1=mysql_result($result,$i,"s_date");
	$f2=mysql_result($result,$i,"s_time");
	$f3=mysql_result($result,$i,"language");
	$f4=mysql_result($result,$i,"status");
	$user=mysql_query("select username from submits where s_id='$f0'");
	if($user)
		$userf=mysql_fetch_array($user)['username'];
	?>
	<tr>
	<td>
	<?php echo $userf; ?>
	</td>
	<td>
	<?php echo $f0; ?>
	</td>
	<td>
	<?php echo $f1; ?>
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
	</tr>
	<?php
	$i++;
}
mysql_close();
?>
</table>
<br>
<button type="button" onclick="parent.location='afirst.php'">Back</button>
</body>
</html>