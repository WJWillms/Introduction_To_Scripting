#!/bin/bash
echo "This is Assignment 7"

salary=$1
echo "$salary"

#Half to do math weird since bash doesnt like floats
if [ $salary -le 10000 ]
then
	gross=$(($salary+(($salary/100)*20)+($salary/100)*80))
	echo "The Gross Salary: $gross"
elif [[ $salary -gt 10000 && $salary -le 20000 ]]
then
        gross=$(($salary+(($salary/100)*25)+($salary/100)*90))
        echo "The Gross Salary: $gross"
else
        gross=$(($salary+(($salary/100)*30)+($salary/100)*95))
        echo "The Gross Salary: $gross"
fi
