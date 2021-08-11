#!/bin/bash

start_time=`date +%s%N`
twint -s 'tamil nadu election 2021' -o 'tnelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s 'assam election 2021' -o 'assamelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s 'kerala election 2021' -o 'klelection.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s 'caa protest' -o 'caaprotest.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time

start_time=`date +%s%N`
twint -s 'nrc protest' -o 'nrcprotest.csv' --csv --hashtags --stats -ho
end_time=`date +%s%N`
elapsed_time=`expr $end_time - $start_time`
echo $elapsed_time
