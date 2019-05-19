<?php

    require_once('PHPMailer/PHPMailerAutoload.php');

    $mail = new PHPMailer();
    $mail->isSMTP();
    $mail->SMTPAuth = true;
    $mail->SMTPSecure = 'ssl';
    $mail->Host = 'smtp.gmail.com';
    $mail->Port = '465';
    $mail->isHTML();
    $mail->Username = 'hemant66wave@gmail.com';
    $mail->Password = 'HK77@gmail##';
    $mail->setFrom('no-reply@howcode.org');
    $mail->Subject = 'Mail aaya kya';
    $mail->Body = 'bhej diya';
    $mail->AddAddress('svupgraded2016@gmail.com');

    $mail->Send();
 ?>
