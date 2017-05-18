<?php
    include 'connect.php';
	echo 'HERE';
    
    $searchTerm = $_GET['term'];
    
    $query = $db->query("SELECT DISTINCT r.restaurantname FROM restauranttbl as r JOIN menutbl as m ON r.resturantid = m.restaurantid
	WHERE m.cuisinetype LIKE '%".$searchTerm."%' UNION 
	SELECT restaurantname FROM restauranttbl WHERE restaurantname LIKE '%".$searchTerm."%' ");
	
    while ($row = $query->fetch_assoc()) {
        $data[] = 'Sona';
    }
    
    //return json data
    echo json_encode($data);
?>