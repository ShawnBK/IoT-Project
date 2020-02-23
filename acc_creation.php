<html>
<body>
<form action="welcome.html">
<?php
$con=mysqli_connect("localhost","root","","database1");
$a=$_POST['name'];
$b=$_POST['vtype'];
$c=$_POST['wtype'];
$d=$_POST['amt'];
mysqli_query($con,"INSERT INTO toll_management (NAME,VEH_TYPE,WHEELER_TYPE,BALANCE) VALUES('$a','$b','$c','$d') ");
?>

YOUR ACCOUNT HAS BEEN CREATED
<br>
TAG ID WILL BE ISSUED SOON
<br>
<br>
<input type="submit" name="sub" value="GO BACK TO WELCOME PAGE">
</form>
</body>
</html>

