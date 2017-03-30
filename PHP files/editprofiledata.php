<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
session_start();
error_reporting(E_ERROR | E_PARSE);
$password=$_POST['password'];
$fname=$_POST['p_fname'];
$fname=strtoupper($fname);
$lname=$_POST['p_lname'];
$lname=strtoupper($lname);
$country=$_POST['country'];
$country=strtoupper($country);
$dob=$_POST['dob'];
$type=$_POST['type'];
$type=strtoupper($type);
$oname=strtoupper($_POST['o_name']);
$oname=strtoupper($oname);
$ocity=strtoupper($_POST['o_city']);
$ocity=strtoupper($ocity);
$ocountry=strtoupper($_POST['o_country']);
$ocountry=strtoupper($ocountry);

if($password && $fname && $lname && $country && $dob && $type && $oname && $ocity && $ocountry)
{
	if(strtotime($dob)>time())
	{
		echo "<script type='text/javascript'>confirm('Date of birth is not correct');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Back</button>
		    </form>";
	}
	else
	{
		$connect = mysql_connect("localhost","root","") or die("Could not connect");
		mysql_select_db("dbp") or die("Could not find database");
		
		$q1=mysql_query("update `person` set password='$password',p_fname='$fname',p_lname='$lname',country='$country',dob='$dob' where username='".$_SESSION['username']."'");
		$oid=$oid=mysql_query("SELECT o_id from organisation where o_name='$oname' and type='$type' and o_city='$ocity' and o_country='$ocountry'");
		if($oid)
			$oidr=mysql_fetch_array($oid)['o_id'];
		$numrows=mysql_num_rows($oid);
		if($numrows==0)
		{
			$q2=mysql_query("INSERT INTO `organisation`(`o_name`, `type`, `o_city`, `o_country`) VALUES ('$oname','$type','$ocity','$ocountry')");
			$oidr=mysql_insert_id();
			$q3=mysql_query("update `member_of` set o_id='$oidr' where username='".$_SESSION['username']."'");
		}
		else
			$q3=mysql_query("update `member_of` set o_id='$oidr' where username='".$_SESSION['username']."'");
		if($q1 && $q3)
		{
			echo "<script type='text/javascript'>confirm('Profile updated successfully');</script>
				<form>
				<br><button type='button' onclick='parent.location=\"first.php\"'>Go Back</button>
				</form>";
		}
	}
}
else 
{
	echo "<script type='text/javascript'>confirm('Enter all the required data');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"first.php\"'>Go Back</button>
		    </form>";
}
mysql_close();
?>
</body>
</html>