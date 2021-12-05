<?php

include_once('db.php');

$nombre = $_POST['nombre'];
$correo = $_POST['correo'];
$telefono = $_POST['telefono'];
$mascota = $_POST['mascota'];
$servicio = $_POST['servicio'];
$agenda = $_POST['agenda'];

echo "<h2>Agenda</h2>";
echo "El nombre recibido es: " . $nombre . "<br/>";
echo "El correo recibido es: " . $correo . "<br/>";
echo "El teléfono recibido es: " . $telefono . "<br/>";
echo "La mascota recibida es: " . $mascota . "<br/>";
echo "El servicio recibido es: " . $servicio . "<br/>";
echo "La fecha recibida es: " . $agenda . "<br/>";

$conectar=conn();
$sql="INSERT INTO agenda (nombre, correo, telefono, mascota, agenda) VALUES ('$nombre', '$correo', '$telefono', '$mascota', '$agenda')";
$resul = mysqli_query($conectar, $sql) or trigger_error("Query Failed! SQL-Error: " .mysqli_error($conectar), E_USER_ERROR);

echo "$sql";

?>