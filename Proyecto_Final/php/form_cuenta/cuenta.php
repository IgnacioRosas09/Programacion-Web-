<?php

include_once('db.php');

$nombre = $_POST['nombre'];
$correo = $_POST['correo'];
$contraseña = $_POST['contraseña'];
$mascota = $_POST['mascota'];
$chequeo = $_POST['chequeo'];

echo "<h2>Usuario</h2>";
echo "El nombre recibido es: " . $nombre . "<br/>";
echo "El correo recibido es: " . $correo . "<br/>";
echo "La contraseña recibida es: " . $contraseña . "<br/>";
echo "La mascota recibida es: " . $mascota . "<br/>";
echo "El check recibido es: " . $chequeo . "<br/>";

$conectar=conn();
$sql="INSERT INTO usuarios (nombre, correo, contraseña, mascota, chequeo) VALUES ('$nombre', '$correo', '$contraseña', '$mascota', '$chequeo')";
$resul = mysqli_query($conectar, $sql) or trigger_error("Query Failed! SQL-Error: " .mysqli_error($conectar), E_USER_ERROR);

echo "$sql";

?>