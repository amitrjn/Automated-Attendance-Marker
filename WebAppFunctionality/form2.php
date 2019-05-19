<?php
    #echo $POST["date"];
    echo (string)(date("Y.m.d")) . "<br>";
    //echo "jxaj";
   if(isset($_FILES['image'])){
      $errors= array();
      $file_name = $_FILES['image']['name'];
      $file_size = $_FILES['image']['size'];
      $file_tmp = $_FILES['image']['tmp_name'];
      $file_type = $_FILES['image']['type'];
      $file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));

      $extensions= array("jpeg","jpg","png");

      if(in_array($file_ext,$extensions)=== false){
         $errors[]="extension not allowed, please choose a JPEG or PNG file.";
      }

      if($file_size > 2097152) {
         $errors[]='File size must be excately 2 MB';
      }

      if(empty($errors)==true) {
         move_uploaded_file($file_tmp,"uploads/".(string)(date("Y.m.d"))."/".$file_name);
         //echo "Success";
      }else{
         print_r($errors);
      }
      $command = escapeshellcmd('/usr/custom/test.py');
      $output = shell_exec($command);
      echo $output;

   }
?>
<html>
  <head>
    <title>CS671</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
   <body>
     <h1>Attendance for CS-671</h1>
     <p>Instructor :- Aditya Nigam</p>
     <p2></p2>

      <form action = "" method = "POST" enctype = "multipart/form-data">
          Date(DD/MM/YY):<br>
          <input type="text" name="date"><br><br>
         <input type = "file" name = "image" />
         <input type = "submit"/>
         <ul>
            <li>Sent file: <?php echo $_FILES['image']['name'];  ?>
            <li>File size: <?php echo $_FILES['image']['size'];  ?>
            <li>File type: <?php echo $_FILES['image']['type'] ?>
            <li>Date: <?php echo $_FILES['date'] ?>
         </ul>

      </form>

   </body>
</html>
