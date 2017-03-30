<html>
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
<body>
<form action="writequestiondata.php" method="post">
Choose a Question Code
<br><input class="textbox" type="text" name="qcode">
<br><br>Difficulty
<br><select class="textbox" name="difficulty">
<option value="Easy">Easy</option>
<option value="Medium">Medium</option>
<option value="Hard">Hard</option>
<option value="Expert">Expert</option>
</select>
<br><br>Question Tags
<br><input type="checkbox" name="tag[]" value="DP" />Dynamic Programming<br />
<input type="checkbox" name="tag[]" value="GREEDY" />Greedy<br />
<input type="checkbox" name="tag[]" value="IMPLEMENT" />Implementation<br />
<input type="checkbox" name="tag[]" value="MATHS" />Mathematics<br />
<input type="checkbox" name="tag[]" value="DS" />Data Structures
<br><br>Online Judge
<br><input type="checkbox" name="judge[]" value="CODECHEF" />CodeChef<br />
<input type="checkbox" name="judge[]" value="CODEFORCES" />Codeforces<br />
<input type="checkbox" name="judge[]" value="TOPCODER" />TopCoder<br />
<input type="checkbox" name="judge[]" value="SPOJ" />Spoj<br />
<br><input type="submit" value="Submit">
</form>
</body>
</html>