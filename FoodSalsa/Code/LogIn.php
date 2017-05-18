<?php
					session_start();
							if(isset($_POST['submitl']))
							{	
							include 'connect.php';
							
								$username = $_POST['username'];
								
								$password = $_POST['password'];
							
								$sql = "SELECT username,fname,lname,password,role FROM usertbl WHERE Username = '$username' AND Password = '$password'";
                                
								$result = mysqli_query($conn,$sql) or die(mysqli_error());
								$num = mysqli_num_rows($result);
				
								
								if($num==1){
									$_SESSION['logged']=true;
									while($row=$result->fetch_assoc())
									{
										$name = $row["fname"]." ".$row["lname"];
										$a=strcmp($row["role"],"user");
										echo $a;
										if($a==0){
											$_SESSION['username']=$name;
											header('Location: index.php');
										}else{
											$_SESSION['vusername']=$username;
											$_SESSION['username']=$name;
											header('Location: VendorInformation.php');
										}
									}	
									
								}else{
									$_SESSION['logged']=false;
									echo "Invalid username or password";
								}
							}	
						 		
?>
<?php 
						 if(isset($_POST['submit']))
						 {						
							include 'connect.php';
								$sql2 = "INSERT INTO usertbl (username, fname, lname, password, role) VALUES ('$_POST[email]','$_POST[firstname]','$_POST[lastname]','$_POST[password]','$_POST[user]')";
                                if ($conn->query($sql2) === TRUE) {
									echo "User Sign Up Successful";
								} else {
									echo "Error: " . $sql . "<br>" . $conn->error;
								}
								if (!empty($_POST['ResturantName']) && !empty($_POST['ResturantLocation'])) {
									$sql1="INSERT INTO vendortbl (vusername,vfname,vlastname) VALUES ('$_POST[email]','$_POST[firstname]','$_POST[lastname]')";
									if ($conn->query($sql1) === TRUE) {
										echo "Vendor insert successful";
									} else {
										echo "Error: " . $sql . "<br>" . $conn->error;
									}
									$sql = "INSERT INTO restauranttbl (vusername,restaurantname,rlocation) VALUES ('$_POST[email]','$_POST[ResturantName]','$_POST[ResturantLocation]')";
									if ($conn->query($sql) === TRUE) {
										echo "Vendor Sign Up successful";
									} else {
										echo "Error: " . $sql . "<br>" . $conn->error;
									}
								}
								
						 }		
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "input" ).checkboxradio();
  } );
  </script>
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
        <!--<li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login/SignUp</a></li>
        <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> SignUp</a></li>-->
      </ul>
    </div>
  </div>
</nav>
  
<div class="container-fluid text-center"> 
    <div class="container">    
        <div id="loginbox" style="margin-top:50px;" class="mainbox col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">                    
            <div class="panel panel-info" >
                    <div class="panel-heading">
                        <div class="panel-title">Sign In</div>
                        <div style="float:right; font-size: 80%; position: relative; top:-10px"><a href="#">Forgot password?</a></div>
                    </div>     

                    <div style="padding-top:30px" class="panel-body" >

                        <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>
                            
                        <form id="loginform" class="form-horizontal" role="form" method="post">
                                    
                            <div style="margin-bottom: 25px" class="input-group">
                                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                                        <input id="login-username" type="text" class="form-control" name="username" value="" placeholder="username or email">                                        
                                    </div>
                                
                            <div style="margin-bottom: 25px" class="input-group">
                                        <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                        <input id="login-password" type="password" class="form-control" name="password" placeholder="password">
                                    </div>
                                    

                                
                            <div class="input-group">
                                      <div class="checkbox">
                                        <label>
                                          <input id="login-remember" type="checkbox" name="remember" value="1"> Remember me
                                        </label>
                                      </div>
                                    </div>


                                <div style="margin-top:10px" class="form-group">
                                    <!-- Button -->

                                    <div class="col-sm-12 controls">
										<input type="submit" name="submitl" id = "submitl" value="login" class="btn btn-success">
                                      
                                      

                                    </div>
                                </div>


                                <div class="form-group">
                                    <div class="col-md-12 control">
                                        <div style="border-top: 1px solid#888; padding-top:15px; font-size:85%" >
                                            Don't have an account! 
                                        <a href="#" onClick="$('#loginbox').hide(); $('#signupbox').show()">
                                            Sign Up Here
                                        </a>
                                        </div>
                                    </div>
                                </div>    
                            </form>    
							



                        </div>                     
                    </div>  
        </div>
        <div id="signupbox" style="display:none; margin-top:50px" class="mainbox col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
                    <div class="panel panel-info">
                        <div class="panel-heading">
                            <div class="panel-title">Sign Up</div>
                            <div style="float:right; font-size: 85%; position: relative; top:-10px"><a id="signinlink" href="#" onclick="$('#signupbox').hide(); $('#loginbox').show()">Sign In</a></div>
                        </div>  
                        <div class="panel-body" >
                            <form id="signupform" class="form-horizontal" role="form" method="POST">
                                
                                <div id="signupalert" style="display:none" class="alert alert-danger">
                                    <p>Error:</p>
                                    <span></span>
                                </div>
                                    
                                
                                  
                                <div class="form-group">
                                    <label for="email" class="col-md-3 control-label">Email*</label>
                                    <div class="col-md-9">
                                        <input type="email" class="form-control" name="email" placeholder="Email Address" required>
                                    </div>
                                </div>
                                    
                                <div class="form-group">
                                    <label for="firstname" class="col-md-3 control-label">First Name*</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="firstname" placeholder="First Name" required>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="lastname" class="col-md-3 control-label">Last Name</label>
                                    <div class="col-md-9">
                                        <input type="text" class="form-control" name="lastname" placeholder="Last Name">
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="password" class="col-md-3 control-label">Password*</label>
                                    <div class="col-md-9">
                                        <input type="password" class="form-control" name="password" placeholder="Password" required>
                                    </div>
                                </div>
                                
                                <div class="form-group">
                                    <label for="User" class="col-md-3 control-label">User/Vendor</label>
                                    <div class="col-md-9">
									<label for="user">User</label>
									<input type="radio" name="user" id="user" value ="user" checked="checked" onclick="show1()">
									<label for="vendor">Vendor</label>
									<input type="radio" name="user" id="user" value="vendor" onclick = "show2()">
									
                                        
										 
                                    </div>
                                </div>
								<div class="form-group" id="resturant" style="display:none">
                                    <label for="ResturantName" id="ResturantName1" class="col-md-3 control-label">Resturant Name*</label>
                                    <div class="col-md-9">
                                        <input type="text" id="ResturantName" name="ResturantName" class="form-control" > 
                                    </div>
                                </div>
								<div class="form-group" id="resturant1" style="display:none">
									<label for="ResturantLocation" id="ResturantLocation" class="col-md-3 control-label">Resturant Location*</label>
                                    <div class="col-md-9">
                                        <input type="text" id="ResturantLocation" name="ResturantLocation" class="form-control" > 
                                    </div>
                                </div>
								<script>
									function show1(){
									document.getElementById('resturant').style.display ='none';
									document.getElementById('resturant1').style.display ='none';
											}
									function show2(){
									document.getElementById('resturant').style.display = 'block';
									document.getElementById('resturant1').style.display ='block';
									
								}
								function myFunction() {
									if(document.getElementById('resturant').style.display == 'block'){
										document.getElementById("ResturantName").required=true;
										document.getElementById("ResturantLocation").required=true;
								
									}
								
								}

								</script>
                                <div class="form-group">
                                    <!-- Button -->   
									
                                    <div class="col-md-offset-3 col-md-9">
										<input type="submit" name="submit" value="Sign Up" class="btn btn-success" onclick="myFunction()">
                                        <!--<button id="btn-signup" type="button" class="btn btn-info"><i class="icon-hand-right"></i> &nbsp Sign Up</button>--->
                                        <span style="margin-left:8px;"></span>  
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
