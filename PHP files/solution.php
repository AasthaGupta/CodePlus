<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="solutiondata.php" method="post">
Choose a Question
<?php
error_reporting(E_ERROR | E_PARSE); 
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$result =  mysql_query("SELECT DISTINCT(`q_code`) FROM `question`");
mysql_close();
?>
<br><select class="textbox" name="qcode">
<option></option>
<?php
while($data = mysql_fetch_array($result))
{
	$display = $data['q_code'];
	?>
	<option value="<?php echo $display;?>"><?php echo $display; ?></option>
    <?php
}
?>
</select>
<br><br>Language Used
<br><select class="textbox" name="language">
<option value="C">C</option>
<option value="C++">C++</option>
<option value="Java">Java</option>
<option value="Python">Python</option>
</select>
<br><br>Solution Status
<br><select class="textbox" name="status">
<option value="Accepted">Accepted</option>
<option value="Wrong-Answer">Wrong Answer</option>
<option value="Compilation-Error">Compilation Error</option>
</select>
<br><br>Submission Date
<br><input class="textbox" type="date" name="sdate">
<br><br>Submission Time
<br><input class="textbox" type="time" name="stime">
<br><br><input type="submit" value="Submit">
</form>
</body>
</html>