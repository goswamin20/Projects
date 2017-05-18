<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Cuisine</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
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

button.accordion {
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 15px;
    transition: 0.4s;
}

button.accordion.active, button.accordion:hover {
    background-color: #ddd; 
}

div.panel {
    padding: 0 18px;
    display: none;
    background-color: white;
}
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
		  <li><a href="#">About Us</a></li>
        <li class="active"><a href="#">Cuisine</a></li>
        
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
    
      <h1>Cuisine</h1>
       
        <form class="form-group" role="search" method="post">
        <div class="input-group">
            <input type="text" class="form-control" name="search" placeholder="Search">
            <div class="input-group-btn">
                <button class="btn btn-default" type="submit" value = "search"><i class="glyphicon glyphicon-search"></i></button>
            </div>
        </div>
        </form>
		
		<?php
		include 'connect.php';
		
		if (!empty ($_POST["search"]))
		{
		$search_value=$_POST["search"];
		$query="SELECT resturantid,restaurantname FROM restauranttbl WHERE restaurantname like '%$search_value%'";
		$res = mysqli_query($conn,$query) or die(mysqli_error($conn));
		$num_rows=mysqli_num_rows($res);
		
			if ($res->num_rows > 0) {
				echo '<div class="panel panel-info"><div class="panel-body" >';
				echo '<table class="container-fluid text-center">';
		      while($row=$res->fetch_assoc()){
			$array[] =$row["restaurantname"]." ".$row["resturantid"];
			echo '<tr>';
			echo '<td>'.'<a href="userInterface.php?id='.urldecode($row['resturantid']).'">'.$row["restaurantname"].'</a>'.'</td>';
			echo '</tr>';
			}
			echo '</div></div>';
			}else{
				echo '<p align="center">No resturant found</p>';
			}
		
		}
		?>
    
    <table class="table">
    <tbody>
      <tr>
        <td width="60%" > <ul>
		<?php 
		include 'connect.php';
		
								
								$sql = "SELECT  DISTINCT cuisinetype FROM menutbl";
                                
								$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
				
								if($num>=1){
									while($row=$result->fetch_assoc())
									{
										echo '<li><a href="Restaurants.php?ct='.urldecode($row['cuisinetype']).'">'.$row["cuisinetype"].'</a></li>';
										
									}	
								}else{
									echo "Invalid";
								}
								
		
		
	
		?>
      </ul></td>
        <td width="40%"><p><a href="pad-thai.jpg"><img height="100%" width="100%" alt="Thai photo" src="pad-thai.jpg"/></a></p></td>
        
      </tr>
      
    </tbody>
  </table>
    </div>
  </div>



</body>
</html>
