<?php
# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1002

function calculate_circle_area($radius)
{
	return 3.14159 * ($radius * $radius);
}

$radius = (float)readline("Enter radius value: ");

$result = number_format(calculate_circle_area($radius), 4, ".", "");

echo "A={$result}" . PHP_EOL;