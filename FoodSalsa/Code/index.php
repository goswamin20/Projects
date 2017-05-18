<?php
session_start();	
?>	

<!DOCTYPE html>
<html lang="en">
<head>
  <title>FoodSalsa</title>
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
    }body {
  font-family: "Open Sans", sans-serif;
  background-color:#f1f1f1;
}
	.container { position:relative;  }
.left-background {background-color:#f1f1f1; width:20%; height:100%; position:absolute; top:0; bottom:0;left: 0;}
.right-background {background-color:#f1f1f1; width:20%; height:100%;position:absolute; top:0; bottom:0;left: 0;}
.content {position:relative; margin:0 auto 0 auto; width:80%;height:100%;}


.carousel-inner > .item > img, .carousel-inner > .item > a > img {
        display: block;
        height: 400px;
        min-width: 100%;
        width: 100%;
        max-width: 100%;
        line-height: 1;
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
	  
        <li class="active"><a href="#">Home</a></li>
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
  
      

  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
      <li data-target="#myCarousel" data-slide-to="3"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">

      <div class="item active">
        <img src="s1.jpg" alt="photo">
        <div class="carousel-caption">
        </div>
      </div>

      <div class="item">
        <img class="img-responsive center-block" src="restaurant.jpg" alt="photo">
        <div class="carousel-caption">
        </div>
      </div>
    
      <div class="item">
        <img class="img-responsive center-block" src="food.jpeg" alt="food">
        <div class="carousel-caption">
        </div>
      </div>

      <div class="item">
        <img class="img-responsive center-block" src="rest1.jpg" alt="dine">
        <div class="carousel-caption">
        </div>
      </div>
  
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>

  <br>
  <br>
  <br>
  <script>
      $('#myCarousel').carousel();
    var winWidth = $(window).innerWidth();
    $(window).resize(function () {

        if ($(window).innerWidth() < winWidth) {
            $('.carousel-inner>.item>img').css({
                'min-width': winWidth, 'width': winWidth
            });
        }
        else {
            winWidth = $(window).innerWidth();
            $('.carousel-inner>.item>img').css({
                'min-width': '', 'width': ''
            });
        }
    });
	</script>
	
	 <div class="container">
	  
		<div clas="content">  
             <form class="form-group" role="search" method="post">
				<div class="input-group">
				<input type="text" class="form-control" placeholder="Search for Restaurants" name="search" id ="search">
					<div class="input-group-btn">
					<button class="btn btn-default" type="submit" name="submit" value = "search"><i class="glyphicon glyphicon-search"></i></button>
					</div>
				</div>
			</form>
<script>
$(function() {
    $( "#search" ).autocomplete({
        source: 'search.php',
		minLength:1
    });
});

</script>
	<?php
	if (!empty ($_POST["search"]))
		{
		$search_value=$_POST["search"];
		include 'connect.php';
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
		</div>
	
	
	
		
    </div>
  </div>



</body>
</html>
