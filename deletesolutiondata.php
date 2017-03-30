<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php 
error_reporting(E_ERROR | E_PARSE);
session_start();
mysql_connect("localhost","root","") or die("Could not connect");
mysql_select_db("dbp") or die("Could not find database");
$sid=$_POST['sid'];
mysql_query("delete from submits where s_id='$sid'");
mysql_query("delete from solution_of where s_id='$sid'");
mysql_query("delete from solution where s_id='$sid'");
echo "<script type='text/javascript'>confirm('Solution Deleted Successfully');</script>
		<form>
		<br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		</form>";
mysql_close();
?>
</body>
</html>