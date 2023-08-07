<?php

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion($s) {
    [$hour,$minute,$secondsRaw] = explode(":",$s);
    [$seconds,$format] = str_split($secondsRaw,2);
    if($format == "PM" && $hour != "12") $hour = intval($hour)+12;
    if($format == "AM" && $hour == "12") $hour = "00";
    echo $hour.":".$minute.":".$seconds;
}

// $fptr = fopen(getenv("OUTPUT_PATH"), "w");

$s = rtrim(fgets(STDIN), "\r\n");

$result = timeConversion($s);

// fwrite($fptr, $result . "\n");

// fclose($fptr);