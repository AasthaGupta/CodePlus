<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="registerdata.php" method="post">
<h2>Personal Details</h2>
Username
<br><input class="textbox" type="text" name="username">
<br>Password
<br><input class="textbox" type="password" name="password">
<br>First Name
<br><input class="textbox" type="text" name="p_fname">
<br>Last Name
<br><input class="textbox" type="text" name="p_lname">
<br>Country
<br><input class="textbox" type="text" name="country">
<br>Date of Birth
<br><input class="textbox" type="date" name="dob"><br>
<br><hr>
<h2>Work Details</h2>
Organisation Type
<br><select class="textbox" name="type">
<option value="Instituition">Instituition</option>
<option value="Company">Company</option>
</select>
<br>Name of Organisation
<br><input class="textbox" type="text" name="o_name">
<br>City
<br><input class="textbox" type="text" name="o_city">
<br>Country
<br><input class="textbox" type="text" name="o_country"><br>
<br><input type="submit" value="Submit">
</form>
</body>
</html>