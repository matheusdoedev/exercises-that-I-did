<?php
# Problem link: https://www.beecrowd.com.br/judge/en/problems/view/1001

$A = (int)readline("Enter number A: ");
$B = (int)readline("Enter number B: ");

function sum($a, $b)
{
	return $a + $b;
}

$result = sum($A, $B);

echo "X = $result" . PHP_EOL;