#!/bin/bash

#Question 1
echo "Question 1"
echo "For Loop"
for (( i=1; i<=15; i++ ))
do
        echo "$i"
done

echo "While Loop"
count=1
while [ $count -lt 16 ]
do
	echo "$count"
	count=$(( $count + 1 ))
done

echo "Until Loop"
count=1
until [ $count -gt 15 ]
do
	echo "$count"
	((count++ ))
done

#Question 2
echo "Question 2"

sum=0
count=20
while [ $count -le 40 ]
do
	sum=$(($sum + $count))
	((count++))
done
echo "Sum from 20 to 40: $sum"

sum=0
for (( i=20; i<=40; i++ ))
do
	sum=$(($sum + $i))
done
echo "Sum from 20 to 40: $sum"	


sum=0
count=20
until [ $count -gt 40 ]
do
	sum=$(($sum + $count))
	((count++))
done
echo "Sum from 20 to 40: $sum"



#Question 3
echo "Question 3: Print Prime numbers to 50"
for num in $(seq 1 50)
do
    count=0
    for i in $(seq 2 $(expr $num - 1))
    do 
        if [ $(expr $num % $i) -eq 0 ]
        then
            count=1
            break
        fi
    done
    if [ $count -eq 0 ]
    then
    echo $num
    fi
done



#Question4


echo "Tell us your input"
read var

if [[ $var == Corpus ]] || [[ $var == corpus ]]
then
	echo "Texas A&M University Corpus Christi"
elif [[ $var == Kingsville ]] || [[ $var == kingsville ]]
then                
	echo "Texas A&M University Kingsville"
elif [[ $var == Commerce ]] || [[ $var == commerce ]]
then
	echo "Texas A&M University Commerce"
else
	echo "Texas A&M University"
fi



var=5
#Bonus
if [[ $var -ge 1 ]] && [[ $var -lt 11 ]]
then
        echo "Between 1 and 10"
elif [[ $var -ge 11 ]] && [[ $var -lt 21 ]]
then
        echo "Between 11 and 20"
elif [[ $var -gt 20 ]]
then
        echo "Greater than 20"
else
        echo "Less than 1"
fi

