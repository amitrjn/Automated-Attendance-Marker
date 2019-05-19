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

$myfile = fopen("Attendance.txt", "r") or die("Unable to open file!");

$date = "2019-05-18";
// Output one line until end-of-file
while(!feof($myfile)) {
  //echo fgets($myfile) . "<br>";
  $id = fgets($myfile);
  echo $id."<br>";
  $sql = "INSERT INTO Attendance (RollNo,day)
  VALUES ('$id', '$date')";
  if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  }
  else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

}
$sql = "DELETE FROM Attendance WHERE LENGTH(RollNo)=0 ";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
}
else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
fclose($myfile);
?>
