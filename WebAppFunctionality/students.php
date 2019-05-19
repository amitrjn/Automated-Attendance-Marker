<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "STUDENTS";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/*$sql = "CREATE TABLE Info (
id VARCHAR(20)  PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50),
phone VARCHAR(15)
)";

if ($conn->query($sql) === TRUE) {
    echo "Table MyGuests created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}*/

$sql1 = "CREATE TABLE Atten (
id VARCHAR(20),
day DATE
)";

if ($conn->query($sql1) === TRUE) {
    echo "Table Attendance created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>
