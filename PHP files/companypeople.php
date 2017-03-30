<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="companypeopledata.php" method="post">
Choose an Organisation
<?php
error_reporting(E_ERROR | E_PARSE); 
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result =  mysql_query("SELECT DISTINCT(`o_name`) FROM `organisation`");
mysql_close();
?>
<br><select class="textbox" name="oname">
<option></option>
<?php
while($data = mysql_fetch_array($result))
{
	$display = $data['o_name'];
	?>
	<option value="<?php echo $display;?>"><?php echo $display; ?></option>
    <?php
}
?>
</select>
<br><br><input type="submit" value="Submit">
</form>
</body>
</html>