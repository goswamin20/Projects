<?php	
session_start();		
							if(isset($_POST['submit2']))
						 {	
					 
							include 'connect.php';
								$username=$_SESSION['vusername'];
								
								$sql = "SELECT resturantid FROM restauranttbl WHERE  vusername='$username'";
                                
								$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
				
								if($num==1){
									while($row=$result->fetch_assoc())
									{
										$restroid=$row["resturantid"];
									}	
								}else{
									echo "Invalid";
								}
								$ct1=$_POST["cuisineType1"];
								$f1=$_POST["Food1"];
								$p1=$_POST["Price1"];
								$d1=$_POST["Day1"];
								$t1=$_POST["Time1"];
								if((empty($_POST["cuisineType1"]) && empty($_POST["Food1"]) && empty($_POST["Price1"])&& empty($_POST["Day1"])
									&& empty($_POST["Time1"]))||empty($_POST["Food1"])){
									
								}else{
									$sql1 = "INSERT INTO menutbl(restaurantid,cuisinetype,food,price,day,time) VALUES ('$restroid','$ct1','$f1','$p1','$d1','$t1')";
								if ($conn->query($sql1) === TRUE) {
									echo "1st record saved successfully";
								} else {
									echo "Error: " . $sql1 . "<br>" . $conn->error;
								}
								}
								
                                
								
								$ct2=$_POST["cuisineType2"];
								$f2=$_POST["Food2"];
								$p2=$_POST["Price2"];
								$d2=$_POST["Day2"];
								$t2=$_POST["Time2"];
								if((empty($_POST["cuisineType2"]) && empty($_POST["Food2"]) && empty($_POST["Price2"])&& empty($_POST["Day2"])
									&& empty($_POST["Time2"]))|| empty($_POST["Food2"])){
								
									}else{
										$sql2 = "INSERT INTO menutbl(restaurantid,cuisinetype,food,price,day,time) VALUES ('$restroid','$ct2','$f2','$p2','$d2','$t2')";
								
                                if ($conn->query($sql2) === TRUE) {
									echo "2nd record saved successfully";
								} else {
									echo "Error: " . $sql2 . "<br>" . $conn->error;
								}
									}
								
								$ct3=$_POST["cuisineType3"];
								$f3=$_POST["Food3"];
								$p3=$_POST["Price3"];
								$d3=$_POST["Day3"];
								$t3=$_POST["Time3"];
								if((empty($_POST["cuisineType3"]) && empty($_POST["Food3"]) && empty($_POST["Price3"])&& empty($_POST["Day3"])
									&&empty($_POST["Time3"]))|| empty($_POST["Food3"])){
								
								}else{
									$sql3 = "INSERT INTO menutbl(restaurantid,cuisinetype,food,price,day,time) VALUES ('$restroid','$ct3','$f3','$p3','$d3','$t3')";
								
                                if ($conn->query($sql3) === TRUE) {
									echo "3rd record saved successfully";
								} else {
									echo "Error: " . $sql3 . "<br>" . $conn->error;
									}
								}
								$ct4=$_POST["cuisineType4"];
								$f4=$_POST["Food4"];
								$p4=$_POST["Price4"];
								$d4=$_POST["Day4"];
								$t4=$_POST["Time4"];
								
								if((empty($_POST["cuisineType4"]) && empty($_POST["Food4"]) && empty($_POST["Price4"])&& empty($_POST["Day4"])
									&&empty($_POST["Time4"]))||empty($_POST["Food4"])){
								}else{
									$sql4 = "INSERT INTO menutbl(restaurantid,cuisinetype,food,price,day,time) VALUES ('$restroid','$ct4','$f4','$p4','$d4','$t4')";
								
                                if ($conn->query($sql4) === TRUE) {
									echo "4th record saved successfully";
								} else {
									echo "Error: " . $sql4 . "<br>" . $conn->error;
									}
								}
									
								$ct5=$_POST["cuisineType5"];
								$f5=$_POST["Food5"];
								$p5=$_POST["Price5"];
								$d5=$_POST["Day5"];
								$t5=$_POST["Time5"];
								if((empty($_POST["cuisineType5"]) && empty($_POST["Food5"]) && empty($_POST["Price5"])&& empty($_POST["Day5"])
									&&empty($_POST["Time5"]))||empty($_POST["Food5"])){
								
									}
									
									else{
										$sql5 = "INSERT INTO menutbl(restaurantid,cuisinetype,food,price,day,time) VALUES ('$restroid','$ct5','$f5','$p5','$d5','$t5')";
								
                                if ($conn->query($sql5) === TRUE) {
									echo "5th record saved successfully";
								} else {
									echo "Error: " . $sql5 . "<br>" . $conn->error;
								}
									}
									header('Location: index.php');
						 }
						 

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Menu</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="Star.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    
    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 450px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      padding-top: 20px;
      background-color: #f1f1f1;
      height: 100%;
    }
    
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
    }
    
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height:auto;} 
    }
	body {
  font-family: "Open Sans", sans-serif;
  background-color:#f1f1f1;
}
	.container { position:relative;  }
.left-background {background-color:#f1f1f1; width:20%; height:100%; position:absolute; top:0; bottom:0;left: 0;}
.right-background {background-color:#f1f1f1; width:20%; height:100%;position:absolute; top:0; bottom:0;left: 0;}
.content {position:relative; margin:0 auto 0 auto; width:80%;height:100%; background-color:#ffffff;}
	

  </style>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <img src = "logo1.png" width ="40%">
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="index.php">Home</a></li>
		<li><a href="about.php">About Us</a></li>
        <li><a href="cuisine.php">Cuisine</a></li>
        <li><a href="Contact.php">Contact</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <?php
		if(!empty($_SESSION['logged']) && $_SESSION['logged']==true)
		{
			echo '<li><a href ="#"><span></span>'.$_SESSION['username'].'</a></li>';
			echo '<li><a href ="logout.php"><span class="glyphicon glyphicon-log-in"></span>Logout </a></li>';
		}
		else
		{
			echo '<li><a href="LogIn.php"><span class="glyphicon glyphicon-log-in"></span> Login/SignUp</a></li>';
        
		}
		?>
      </ul>
    </div>
  </div>
</nav>
  
  <div class="container">
<div class="left-background"></div>
<div class="right-background"></div>
<div class="content">  
				
                    <div class="panel panel-info">
                        <div class="panel-heading">
                            <div class="panel-title">Menu Details</div>
                        </div>  
                        <div class="panel-body" >
						<form action="upload.php" method="post" enctype="multipart/form-data" align="left">
							<p align="left">Upload Menu Image:</p>
							<input type="file" name="fileToUpload" id="fileToUpload"><br/>
							<input type="submit" value="Upload Image" name="submit">
						</form>
						<br/>
                            <form id="signupform" class="form-horizontal" role="form" method="post">
                                <table>
								<tr>
								<th>Cuisine Type</th>
								<th>Food</th>
								<th>Price</th>
								<th>Day</th>
								<th>Time</th>
							  </tr>
							  <tr>
							  <td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="cuisineType1" placeholder="Cuisine Type"><br/>
                                    </div>
								</div> 
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Food1" placeholder="Food"><br/>
                                    </div>
                                </div>
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Price1" placeholder="Price"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Day1" placeholder="Day"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Time1" placeholder="Time"><br/>
                                    </div>
                                </div>
								</td>
                                </tr>
								<tr>
							  <td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="cuisineType5" placeholder="Cuisine Type"><br/>
                                    </div>
								</div> 
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Food5" placeholder="Food"><br/>
                                    </div>
                                </div>
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Price5" placeholder="Price"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Day5" placeholder="Day"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Time5" placeholder="Time"><br/>
                                    </div>
                                </div>
								</td>
                                </tr>
								<tr>
							  <td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="cuisineType2" placeholder="Cuisine Type"><br/>
                                    </div>
								</div> 
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Food2" placeholder="Food"><br/>
                                    </div>
                                </div>
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Price2" placeholder="Price"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Day2" placeholder="Day"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Time2" placeholder="Time"><br/>
                                    </div>
                                </div>
								</td>
                                </tr>
								<tr>
							  <td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="cuisineType3" placeholder="Cuisine Type"><br/>
                                    </div>
								</div> 
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Food3" placeholder="Food"><br/>
                                    </div>
                                </div>
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Price3" placeholder="Price"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Day3" placeholder="Day"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Time3" placeholder="Time"><br/>
                                    </div>
                                </div>
								</td>
                                </tr>
								<tr>
							  <td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="cuisineType4" placeholder="Cuisine Type"><br/>
                                    </div>
								</div> 
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Food4" placeholder="Food"><br/>
                                    </div>
                                </div>
								</td>
								<td>
                                <div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Price4" placeholder="Price"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Day4" placeholder="Day"><br/>
                                    </div>
                                </div>
								</td>
								<td>
								<div class="form-group">
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="Time4" placeholder="Time"><br/>
                                    </div>
                                </div>
								</td>
                                </tr>
                                 </table>  
                                <div class="form-group">
                                    <!-- Button -->                                        
                                    <div align="right">
										<span style="margin-right:8%">
                                        <input type="submit" name="submit2" value="Submit Menu" class="btn btn-sucess" ><i class="icon-hand-right"></i>
                                        </span>
										</div>
                                    </div>
                                </div>
                                
                                
                                
                                
                            </form>
                         </div>
						 
                    </div>

               
               
                
         </div> 
    </div>
    
    </div>


</body>
</html>
