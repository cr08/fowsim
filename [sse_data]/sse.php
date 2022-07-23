<?php
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');
header("Access-Control-Allow-Origin: *");

$data = file_get_contents("data.json");

echo 'data: ' . $data . "\n\n";

ob_flush();
flush();
?>