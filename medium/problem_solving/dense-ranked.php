<?php

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

function climbingLeaderboard($ranked, $players) {
    $ranked = array_values(array_unique($ranked));
    print_r($ranked);exit();
    $lenR = count($ranked);
    $midLenR = floor($lenR/2);
    [$firstR,$midR,$lastR] = [$ranked[0],$ranked[$midLenR-1],$ranked[$lenR-1]];
    $return = [];
    foreach($players as $player){
        $firstLoop = ($player > $midR) ? $midLenR : 0 ;
        if($player <= $lastR) 
        for($i = $firstLoop; $i < $lenR; $i++){

        }
    }
    return $return;
}


$ranked_count = intval(trim(fgets(STDIN)));

$ranked_temp = rtrim(fgets(STDIN));

$ranked = array_map('intval', preg_split('/ /', $ranked_temp, -1, PREG_SPLIT_NO_EMPTY));

$player_count = intval(trim(fgets(STDIN)));

$player_temp = rtrim(fgets(STDIN));

$player = array_map('intval', preg_split('/ /', $player_temp, -1, PREG_SPLIT_NO_EMPTY));

$result = climbingLeaderboard($ranked, $player);

print_r( $result);