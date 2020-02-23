<html>
<body>
<form>
<?php
$con=mysqli_connect("localhost","root","","database1");
$rec=$_POST['amt'];
$a=mysqli_query($con,"SELECT * FROM current_customer" );
$b=mysqli_fetch_array($a);
$c=$b['tag_id'];
$d=mysqli_query($con,"SELECT * FROM toll_management WHERE TAG_ID=$c");
$e=mysqli_fetch_array($d);
$f=$e['BALANCE'];
$g=$rec+$f;
echo "AMOUNT PAID SUCCESSFULLY";
?>
<br>
<br>
<?php 
echo "ACCESS GRANTED";
mysqli_query($con,"UPDATE toll_management SET BALANCE=$g WHERE TAG_ID=$c");
mysqli_query($con,"UPDATE current_customer SET bal_status='1'  WHERE Slno='1'");
?>
</form>
</body>
</html>
