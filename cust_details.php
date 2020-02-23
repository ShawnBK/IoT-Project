<html>
<body>
<h4> TRAVELLER DETAILS</h4>
<?php
$con=mysqli_connect("localhost","root","","database1");
$id=mysqli_query($con,"SELECT *  FROM current_customer WHERE Slno=1 ");
$p=mysqli_fetch_array($id);
$z=$p['tag_id'];
$b=mysqli_query($con,"SELECT * FROM toll_management WHERE TAG_ID='$z' " );
$r=mysqli_fetch_array($b);
if($p['bal_status']==0)
{?>
<form action="welcome.html">
 ACCESS DENIED

Note:To go back to welcome page and create new account press 'CREATE NEW ACCOUNT'
<input type="submit" name="acc" value="CREATE NEW ACCOUNT">
</form>
<?php
}
else if($p['bal_status']==1)
{?>
NAME:  <?php echo $r['NAME']; ?>  
<br> 
TAG ID:  <?php echo $r['TAG_ID'];?>
<br>  
VEHICLE TYPE:  <?php echo $r['VEH_TYPE']; ?> 
<br>
CURRENT BALANCE:  <?php echo $r['BALANCE'];?>  
<br>
<h5>YOUR PAYMENT HAS BEEN MADE<h5>
<h5>ACCESS GRANTED<h5>
<br>
</table>
<?php
}
else
{
?>
<form method="post" action="recharge.php">
<table>
NAME:<?php   echo $r['NAME'];   ?>
<br>
TAG ID:<?php   echo $r['TAG_ID'];  ?>
<br>
VEHICLE TYPE:<?php   echo $r['VEH_TYPE'];  ?>
<br>
</table>
Alert:INSUFFICIENT BALANCE
<input type="submit" name="rec" value="RECHARGE NOW">
<?php
}
?>
</form>
</body>
</html>