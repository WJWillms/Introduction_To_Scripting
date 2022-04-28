#!/bin/bash
#------------------QUESTION 1------------------------
Max=19
count=0
while [ "$count" -le $Max ]
do
number[$count]=$RANDOM
let "count += 1"
done

echo "${number[*]}"



for ((i = 0; i<20; i++))
do
    
for((j = 0; j<20-i-1; j++))
do
    
if [ ${number[j]} -gt ${number[$((j+1))]} ]
then
temp=${number[j]}
number[$j]=${number[$((j+1))]}  
number[$((j+1))]=$temp
fi

done

done

echo "${number[*]}"

#-----------------------Question 2--------------------------

for ((i = 0; i<20; i++))
do

for((j = 0; j<20-i-1; j++))
do

if [ ${number[j]} -lt ${number[$((j+1))]} ]
then
temp=${number[j]}
number[$j]=${number[$((j+1))]}
number[$((j+1))]=$temp
fi

done

done

echo "${number[*]}"

#------------------Question 3------------------------------

for ((i = 0; i<50; i++))
do
numbers[$i]=$((i+1))
done

echo "${numbers[*]}"

#--------------------Question 4-----------------------------

prime(){
sum=0
for ((j = 1; j<51; j++))
do
counter=0
for ((i = 2; i<$((j/2+1)); i++))
do
if [ $((j%i)) -eq 0 ]
then
((counter+=1))
break
fi
done
if [[ $counter -eq 0 ]] && [[ $j -ne 1 ]]
then
echo "$j"
((sum+=j))
fi
done
echo "SUM: $sum"
}

prime

#-----------------------Question 5------------------------
#ec keeps track of evens array position and oc keeps track of the odds
ec=0
oc=0
esum=0
osum=0
for ((i = 1; i<51; i++))
do
if [ $((i%2)) -eq 0 ]
then
evens[$ec]=$((i))
((esum+=i))
((ec+=1))
else
odds[$oc]=$((i))
((osum+=i))
((oc+=1))
fi
done

echo "Even Numbers ${evens[*]}"
echo "Even sum: $esum"
echo "Odd numbers ${odds[*]}"
echo "Odd sum: $osum"
