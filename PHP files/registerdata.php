<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
$username=$_POST['username'];
$password=$_POST['password'];
$fname=$_POST['p_fname'];
$fname=strtoupper($fname);
$lname=$_POST['p_lname'];
$lname=strtoupper($lname);
$country=$_POST['country'];
$country=strtoupper($country);
$dob=$_POST['dob'];
$type=strtoupper($_POST['type']);
$type=strtoupper($type);
$oname=strtoupper($_POST['o_name']);
$oname=strtoupper($oname);
$ocity=strtoupper($_POST['o_city']);
$ocity=strtoupper($ocity);
$ocountry=strtoupper($_POST['o_country']);
$ocountry=strtoupper($ocountry);

if($username && $password && $fname && $lname && $country && $dob && $type && $oname && $ocity && $ocountry)
{
	if(strtotime($dob)>time())
	{
		echo "<script type='text/javascript'>confirm('Date of birth is not correct');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"main.php\"'>Back</button>
		    </form>";
		
	}
	else
	{
		
			$connect = mysql_connect("localhost","root","") or die("Could not connect");
			mysql_select_db("dbp") or die("Could not find database");
			
			$q1=mysql_query("INSERT INTO `person` VALUES ('$username','$password','$fname','$lname','$country','$dob')");
			$oid=mysql_query("SELECT o_id from organisation where o_name='$oname' and type='$type' and o_city='$ocity' and o_country='$ocountry'");
			if($oid)
				$oidr=mysql_fetch_array($oid)['o_id'];
			$numrows=mysql_num_rows($oid);
			if($numrows==0)
			{
				$q2=mysql_query("INSERT INTO `organisation`(`o_name`, `type`, `o_city`, `o_country`) VALUES ('$oname','$type','$ocity','$ocountry')");
				$oidr=mysql_insert_id();
				$q3=mysql_query("INSERT INTO `member_of` VALUES ('$username','$oidr')");
			}
			else
				$q3=mysql_query("INSERT INTO `member_of` VALUES ('$username','$oidr')");
			if(!$q1)
			{
				echo "<script type='text/javascript'>confirm('This username has already been taken');</script>
					<form>
					<br><button type='button' onclick='parent.location=\"main.php\"'>Back</button>
					</form>";
			}
			else
			{
				echo "<script type='text/javascript'>confirm('Registration Successful');</script>
					<form>
					<br><button type='button' onclick='parent.location=\"main.php\"'>Back</button>
					</form>";
			}
	}
}
else 
{
	echo "<script type='text/javascript'>confirm('Enter all the required data');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"main.php\"'>Back</button>
		    </form>";
}
mysql_close();
?>
</body>
</html>