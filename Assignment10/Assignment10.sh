#!/bin/bash

#------------------------Factorial---------------------------------
factorial() {
(( $1 )) || return 1
factorial $(( $1 - 1 ))
return $(( $1 * $? ))
}

echo "Enter a number to Factorial: "
read value
factorial $value
x="$?"
echo "$x"
echo $x > factorial.txt
#-----------------------Factorial----------------------------------
#-----------------------Sum----------------------------------------

<<comment
summation() {
sum=0
while read -r line
do
(( sum += line ))
done < numbers.txt
echo "$sum"
}

summation

summary() {
local -i val=${val:-($2)}
  local -i count=$(( $2 - $1 ))
  if (( $count <= 1 )); then
        echo $val
        return
  fi
  ((val += ($2 - 1) ))
  (( count-- )) 
  summary $1 $(( $2-1 ))
}



summ(){
while read -r line
if ((line[x+1] -ne True))
then
return $sum+line[x]
else
return
sum = sum + summ[x+1]
sum = sum + line[x]

Can Read from line or recursion itself, not both, shit class not worth effort.
comment
