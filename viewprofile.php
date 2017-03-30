<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result=mysql_query("select * from person where username='".$_SESSION['username']."'");
$result2=mysql_query("select * from organisation where o_id=(select o_id from member_of where username='".$_SESSION['username']."')");
?>
<h2>Personal Details</h2>
<table>
<tr>
<td>
Username
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
$f1=mysql_fetch_array($result);
$f2=mysql_fetch_array($result2);
?>
<tr>
<td>
<?php echo $f1['username']; ?>
</td>
<td>
<?php echo $f1['p_fname']; ?>
</td>
<td>
<?php echo $f1['p_lname']; ?>
</td>
<td>
<?php echo $f1['country']; ?>
</td>
<td>
<?php echo $f1['dob']; ?>
</td>
</tr>
</table>
<h2>Work Details</h2>
<table>
<tr>
<td>
Name
</td>
<td>
Type
</td>
<td>
City
</td>
<td>
Country
</td>
</tr>
<tr>
<td>
<?php echo $f2['o_name']; ?>
</td>
<td>
<?php echo $f2['type']; ?>
</td>
<td>
<?php echo $f2['o_city']; ?>
</td>
<td>
<?php echo $f2['o_country']; ?>
</td>
</tr>
</table>
<?php
mysql_close();
?>
<br><button type='button' onclick='parent.location="first.php"'>Go Back</button>
</body>
</html>