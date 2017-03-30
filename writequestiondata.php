<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
$qcode=$_POST['qcode'];
$qcode=strtoupper($qcode);
$difficulty=$_POST['difficulty'];
$difficulty=strtoupper($difficulty);
$tag=$_POST['tag'];
$judge=$_POST['judge'];

if($qcode && $difficulty && !empty($tag) && !empty($judge))
{
	$connect = mysql_connect("localhost","root","") or die("Could not connect");
	mysql_select_db("dbp") or die("Could not find database");
	
	$value=$_SESSION['username'];
	$q1=mysql_query("INSERT INTO `question` VALUES ('$qcode','$difficulty')");
		
	if(!$q1)
	{
		echo "<script type='text/javascript'>confirm('Question already exists');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		    </form>";
	}
	else
	{
	
		mysql_query("INSERT INTO `writes` VALUES ('$qcode','$value')");
		$n1 = count($judge);
        for($i=0; $i < $n1; $i++)
        {
			mysql_query("INSERT INTO `exists_on` VALUES ('$qcode','$judge[$i]')");
		}
		$n2=count($tag);
		for($i=0; $i < $n2; $i++)
        {
			mysql_query("INSERT INTO `tags` VALUES ('$qcode','$tag[$i]')");
		}
		echo "<script type='text/javascript'>confirm('Problem Submitted Successfully');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		    </form>";
	}
}
else
{
	echo "<script type='text/javascript'>confirm('Enter all the required data');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		    </form>";	
}
mysql_close();
?>
</body>
</html>