<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
$username='admin';
$password=$_POST['password'];

if($username && $password)
{
	$connect = mysql_connect("localhost","root","") or die("Could not connect");
	mysql_select_db("dbp") or die("Could not find database");
	$query=mysql_query("select * from person where username='$username'");
	$numrows=mysql_num_rows($query);
	if($numrows!==0)
	{
		while($row=mysql_fetch_assoc($query))
		{
			$dbusername=$row['username'];
			$dbpassword=$row['password'];
		}
		
		if($username==$dbusername && $password==$dbpassword)
		{
			$_SESSION['username']=$username;
			header('Location: afirst.php');
		}
		else
		{
			echo "<script type='text/javascript'>confirm('Incorrect Password');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"main.php\"'>Go Back</button>
		    </form>";
		}
	}
	else
	{
		echo "<script type='text/javascript'>confirm('This User does not Exist');</script>
			 <form>
		     <br><button type='button' onclick='parent.location=\"main.php\"'>Go Back</button>
		     </form>";
	}
}
else
{	
	echo "<script type='text/javascript'>confirm('Please enter a Username and Password');</script>
			<form>
		    <br><button type='button' onclick='parent.location=\"main.php\"'>Go Back</button>
		    </form>";
}
mysql_close();
?>
</body>
</html>