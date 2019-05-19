<?php

    require_once('PHPMailer/PHPMailerAutoload.php');

    $myfile = fopen("/Documents/project/attendance.txt", "r") or die("Unable to open file!");
    while(!feof($myfile)) {
      //echo fgets($myfile) . "<br>";
      $id = fgets($myfile);
      echo $id."<br>";
      $mail = new PHPMailer();
      $mail->isSMTP();
      $mail->SMTPAuth = true;
      $mail->SMTPSecure = 'ssl';
      $mail->Host = 'smtp.gmail.com';
      $mail->Port = '465';
      $mail->isHTML();
      $mail->Username = 'hemant77wave@gmail.com';
      $mail->Password = 'HK66@gmail##';
      $mail->setFrom('no-reply@howcode.org');
      $mail->Subject = 'Attendance';
      $mail->Body = 'You have been marked present in today class.';
      $mail->AddAddress($id."@students.iitmandi.ac.in");

      $mail->Send();

    }
 ?>
