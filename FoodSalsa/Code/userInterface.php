<?php

	session_start();
						 if(isset($_POST['submit2']))
						 {	
					 
							include 'connect.php';
							
								$rating=$_POST['rating'];
								$review=$_POST['review'];
								if(!empty($_SESSION['logged']) && $_SESSION['logged']==true)
								{
								$username=$_SESSION['username'];
								}
								else{
								$username="anonymous";	
								}
								$id = urldecode($_GET['id']);
								echo "restaurant".$id;
							
								$sql = "INSERT INTO userinterfacetbl (username,rating, review,restaurantid) VALUES ('$username','$rating','$review','$id')";
                                if ($conn->query($sql) === TRUE) {
									echo "Review posted successfully";
								} else {
									echo "Error: " . $sql . "<br>" . $conn->error;
								}
								}
								
							
								
?>	

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Resturant</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="Star.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "#tabs" ).tabs();
  } );
  </script>
  <style>
  
  #map {
        height: 300px;
		width: 100%;
      }
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
	.centered {margin: 0 auto; width: 80%; }
	
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

   <br/>
   
  <?php
      include 'connect.php';

      $id = urldecode($_GET['id']);
      $sql = "SELECT  restaurantname FROM restauranttbl WHERE resturantid='$id'";
                                
								$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
				
								if($num==1){
									while($row=$result->fetch_assoc())
									{
										echo '<div align = "center"><h1>'.$row["restaurantname"].'</h1></br></div>';
									}	
								}else{
									echo "Invalid";
								}
		
      ?>
   
      </br>
	 
    
    <div class='centered' align='center' id="tabs">

  <ul>
    <li><a href="#tabs-1">Overview</a></li>
    <li><a href="#tabs-2">Menu</a></li>
    <li><a href="#tabs-3">Reviews</a></li>
  </ul>
  <div id="tabs-1">
  
    <p><?php
      include 'connect.php';

      $id = urldecode($_GET['id']);
      $sql = "SELECT  Description,restaurantname, rlocation, vcontact, menuimage, OpeningTime, ClosingTime, rlatitude, rlongitude FROM restauranttbl WHERE resturantid='$id'";
                                
								$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
				
								if($num==1)
								{
									while($row=$result->fetch_assoc())
									{
										echo '<div class="panel panel-info">
											<div class="panel-body" >
											<p align="left" ><strong><u>About Us</u>&emsp;</strong>'.$row["Description"].'</p><br/>
											<p align="left" ><strong><u>Phone number</u>&emsp;</strong>'.$row["vcontact"].'</p><br/>
											<p align="left" ><strong><u>Opening hours</u>&emsp; </strong>'.$row["OpeningTime"].' '.'-'.$row["ClosingTime"].'</p><br/>
											<p align="left" ><strong><u>Address</u>&emsp; </strong>'.$row["rlocation"].'</p><br/></div></div>';
										
										$showimage=$row["menuimage"];
										$lat=$row["rlatitude"];
										$lon=$row["rlongitude"];
										
									}	
								}
								else
								{
									echo "Invalid";
								}
								
		
      ?></p>
	  
<div id="map"></div>
<script>
var latitude = <?php echo $lat ?>;
var longitude = <?php echo $lon ?>;
function initMap() {
	var myLatLng = {lat: latitude, lng: longitude};
	var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'Hello World!'
        });
      }
 </script>
 <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB46si-RM1EHIeC51bTibEgp2gUrwkzbC4&callback=initMap"></script>
  
  </div>
  
  <div id="tabs-2">
	  <img src="<?php echo $showimage; ?>" style="align:center; height:550px; width:500px;"/>
  </div>
  <div id="tabs-3">
  <!--<div class="container">--->
        <!--<div id="userInterface" style="margin-top:50px  "class="mainbox col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">-->
                    <div class="panel panel-info">
                        <div class="panel-heading">
                            <div class="panel-title">Add a Review</div>
                        </div>  
                        <div class="panel-body" >
                            <form id="signupform" class="form-horizontal" role="form" method="post">
                                    
                                <div class="form-group">
									<label for="review" class="col-md-3 control-label"> Review</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="review" placeholder="review"><br/>
                                    </div>
								</div> 
                                <div class="form-group">
                                    <label for="Rating" class="col-md-3 control-label"> Rating</label>
                                    <ul class="rate-area">
                                    <input type="radio" id="5-star" name="rating" value="5" /><label for="5-star" title="Amazing">5 stars</label>
                                    <input type="radio" id="4-star" name="rating" value="4" /><label for="4-star" title="Good">4 stars</label>
                                    <input type="radio" id="3-star" name="rating" value="3" /><label for="3-star" title="Average">3 stars</label>
                                    <input type="radio" id="2-star" name="rating" value="2" /><label for="2-star" title="Not Good">2 stars</label>
                                    <input type="radio" id="1-star" name="rating" value="1" /><label for="1-star" title="Bad">1 star</label><br/>
                                    </ul>
                                </div>
								   
                                <div class="form-group">
                                    <!-- Button -->                                        
                                    <div class="col-md-offset-3 col-md-9">
                                        <input type="submit" name="submit2" id = "submit2" value="Post" class="btn btn-sucess"><i class="icon-hand-right"></i>
                                    </div>
                                         
                                </div>
                            </div>
                                
                                
                                
                                
                        </form>
                        
						 
						  
					</div>       
                
         
    <p><?php 
	include 'connect.php';
	$id = urldecode($_GET['id']);						
		$sql ="SELECT username, rating, review FROM userinterfacetbl WHERE restaurantid='$id'";
		$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
								
								if($num>=1){
									while($row=$result->fetch_assoc())
									{
										if(empty($row["username"])){
											$username='anonymous';
										}else{
											$username=$row["username"];
							}
							echo '<div class="panel panel-info">
                        <div class="panel-heading">
                            <div class="panel-title">'.$username.'</div>
                        </div>  
                        <div class="panel-body" >
                            <form id="signupform" class="form-horizontal" role="form" method="post">
                                    
                                <div class="form-group">
									
                                    <div class="col-md-9">
                                         <p align ="left"><strong>Rating: </strong>'.$row["rating"].'</p>
										 <p align ="left"><strong>Review: </strong>'.$row["review"].'</p>
                                    </div>
								</div> </div>
								</div>
								';
												
										
										
									}	
									
								}else{
									//echo "Invalid";
								}
		
      ?></p>
 
	</div>
</div>
</div>
</div>
</div>



</body>
</html>
