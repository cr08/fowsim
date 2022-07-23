<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

$json_cardid = $_GET['id'];
$json_timestamp = time();

if ($_GET['jflip'] == "true") {
$json_jflip = "true";
} else {
$json_jflip = "false";
}

$json_array = Array (

	"card" => "$json_cardid",
	"timestamp" => "$json_timestamp",
	"jflip" => "$json_jflip"

);

$json = json_encode($json_array);


$file_handle = fopen('data.json', 'w');
fwrite($file_handle, $json);
fclose($file_handle);

// For info re: writing files in PHP:
// http://php.net/manual/en/function.fwrite.php

?>