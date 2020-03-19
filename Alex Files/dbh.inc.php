<?php

$dbServer = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "main";

$conn = mysqli_connect($dbServer, $dbUsername, $dbPassword, $dbName);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}