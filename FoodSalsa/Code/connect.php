<?php

$username = 'root';
$password = '';
$db = 'foodsalsa';

// Create connection
$conn = new mysqli('localhost', $username, $password, $db) or die("Unable to connect");
?>