#!/bin/bash

start_time=`date +%s%N`
twint -s '#tamilnaduelection2021' -o 'tnelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s '#assamelection2021' -o 'assamelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s '#keralaelection2021' -o 'klelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s '#caaprotest' -o 'caaprotest.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s '#nrcprotest' -o 'nrcprotest.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time
