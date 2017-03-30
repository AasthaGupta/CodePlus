<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$oname=$_POST['oname'];

$result=mysql_query("select * from person where username in (select username from member_of where o_id in (select o_id from organisation where o_name='$oname'))");
$num=mysql_numrows($result);
?>
<table>
<tr>
<td>
Username
</td>
<td>
Password
</td>
<td>
First Name
</td>
<td>
Last Name
</td>
<td>
Country
</td>
<td>
Date of Birth
</td>
</tr>
<?php
$i=0;
while ($i < $num)
{
	$f0=mysql_result($result,$i,"username");
	$f1=mysql_result($result,$i,"password");
	$f2=mysql_result($result,$i,"p_fname");
	$f3=mysql_result($result,$i,"p_lname");
	$f4=mysql_result($result,$i,"country");
	$f5=mysql_result($result,$i,"dob");
	?>
	<tr>
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
<br>
<button type="button" onclick="parent.location='afirst.php'">Back</button>
</body>
</html>