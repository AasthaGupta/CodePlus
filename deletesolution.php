<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="deletesolutiondata.php" method="post">
Choose a Solution
<?php
error_reporting(E_ERROR | E_PARSE);
session_start(); 
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result =  mysql_query("SELECT s_id FROM `submits` where username='" .$_SESSION['username']. "'");
?>
<br><select class="textbox" name="sid">
<option></option>
<?php
while($data = mysql_fetch_array($result))
{
	$display = $data['s_id'];
	?>
	<option value="<?php echo $display;?>"><?php echo $display; ?></option>
    <?php
}
?>
</select>
<br><br><input type="submit" value="Submit">
<?php
mysql_close();
?>
</form>
</body>
</html>