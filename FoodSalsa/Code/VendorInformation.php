<?php	
session_start();		
							if(isset($_POST['submit2']))
						 {	
					 
							include 'connect.php';
								$username=$_SESSION['vusername'];
								$desc=$_POST["RestaurantDescription"];
								$ot=$_POST["OpeningTime"];
								$ct=$_POST["ClosingTime"];
								$adIn=$_POST["AdditionalInformation"];
								$vcontact=$_POST["contact"];
								$sql1 = "UPDATE restauranttbl SET Description='$desc',OpeningTime='$ot',ClosingTime='$ct',AddInfo='$adIn',vcontact='$vcontact' WHERE  vusername='$username'";
			
								 if ($conn->query($sql1) === TRUE) {
									echo "Resturant and vendor information saved successfully";
								} else {
									echo "Error: " . $sql1 . "<br>" . $conn->error;
								}
								header("Location:vendorInterface.php");
								}
								
						 

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Restaurant</title>
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
                            <div class="panel-title" align="center">Details of Restaurant</div>
                        </div>  
                        <div class="panel-body" >
						</br>
						</br>
						
                            <form id="signupform" class="form-horizontal" role="form" method="post">
                               
							   <div class="form-group">
								<label for="contact" class="col-md-3 control-label">Restaurant Description</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="RestaurantDescription" placeholder="Restaurant Description"><br/>
                                    </div>
								</div>
								<div class="form-group">
								<label for="contact" class="col-md-3 control-label">Opening Time*</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="OpeningTime" placeholder="OpeningTime" required><br/>
                                    </div>
								</div>
								<div class="form-group">
								<label for="contact" class="col-md-3 control-label">Closing Time*</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="ClosingTime" placeholder="ClosingTime" required><br/>
                                    </div>
								</div>
                                <div class="form-group">
								<label for="contact" class="col-md-3 control-label"> Vendor Contact*</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="contact" placeholder="contact" required><br/>
                                    </div>
								</div>
								<div class="form-group">
								<label for="contact" class="col-md-3 control-label"> Additional Information</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="AdditionalInformation" placeholder="Additional Information"><br/>
                                    </div>
								</div> 								
								  
                                
										
									<div class="form-group">
										
                                        <p align="center"><input type="submit"  name="submit2" value="next"  class="btn btn-sucess" ><i class="icon-hand-right"></i></p>
                                        
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
