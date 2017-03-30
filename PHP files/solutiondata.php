<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
$qcode=$_POST['qcode'];
$qcode=strtoupper($qcode);
$language=$_POST['language'];
$language=strtoupper($language);
$status=$_POST['status'];
$status=strtoupper($status);
$sdate=$_POST['sdate'];
$stime=$_POST['stime'];

if($qcode && $language && $status && $sdate && $stime)
{
	if(strtotime($sdate.' '.$stime.':00')>time())
	{
		echo "<script type='text/javascript'>confirm('The Submission time is not correct');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		    </form>";
	}
	else
	{
		$connect = mysql_connect("localhost","root","") or die("Could not connect");
		mysql_select_db("dbp") or die("Could not find database");
		
		$value=$_SESSION['username'];
		$sid=mysql_query("SELECT s_id from solution natural join submits where username='$value' and s_date='$sdate' and s_time='$stime'");
		$numrows=mysql_num_rows($sid);
		if($numrows==0)
		{
			$q1=mysql_query("INSERT INTO `solution`(`s_date`, `s_time`, `language`, `status`) VALUES ('$sdate','$stime','$language','$status')");
			$sid=mysql_insert_id();
			$q2=mysql_query("INSERT INTO `submits` VALUES ('$sid','$value')");
			$q3=mysql_query("INSERT INTO `solution_of` VALUES ('$sid','$qcode')");
			echo "<script type='text/javascript'>confirm('Submission Successful');</script>
				<form>
				<br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
				</form>";
		}
		else
		{
			echo "<script type='text/javascript'>confirm('This solution has already been submitted');</script>
				<form>
				<br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
				</form>";
		}
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