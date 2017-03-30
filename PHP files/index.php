<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="login.php" method="post">
Member Login :
<br><br>Username
<br><input  class="textbox" type="text" name="username">
<br><br>Password<br><input class="textbox" type="password" name="password">
<br><br><input type="submit" value="Submit">
</form>
<hr>
New User :
<br><br><button type="button" onclick="parent.location='register.php'">Register</button><br>
<hr>
Administrator :
<br><br><button type="button" onclick="parent.location='amain.php'">Login</button>
</body>
</html>