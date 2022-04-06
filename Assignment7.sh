#!/bin/bash

#Problem 1 -----------------------------------
echo "This is Assignment 7"
#Problem 2 ------------------------------------
name="Wade Willms"
course1="Capstone"
course2="Scripting"
course3="Mobile Programming"
course4="Survery of Programming Languages"

echo $name
echo $course1
echo $course2
echo $course3
echo $course4

#Problem 3 ----------------------------------
echo "Name: ${1} ${2}"
echo "Course 1: ${3}"
echo "Course 2:${4}"
echo "Course 3:${5}"
echo "Course 4:${6}"

#Problem 4 ----------------------------------
echo "Process ID Number: $$"

#Problem 5 -----------------------------------
RANDOM=$$
#Filling 2 arrays for printing info
courses=("Capstone" "Scripting Intro" "Mobile Programming" "Survery of programming langauges")
grade1=$[RANDOM%100]
grade2=$[RANDOM%100]
grade3=$[RANDOM%100]
grade4=$[RANDOM%100]

grades=($grade1 $grade2 $grade3 $grade4)
count=0
#While loop to cycle through all courses with random grades to determine letter in if satatement and print
while [[ count -lt 4 ]];
do
	if [[ ${grades[count]} -ge 60 ]] && [[ ${grades[count]} -lt 70 ]]
	then
		echo "Class: ${courses[count]} Grade: ${grades[count]} Letter: D"
	elif [[ ${grades[count]} -ge 70 ]] && [[ ${grades[count]} -lt 80 ]]
        then
                echo "Class: ${courses[count]} Grade: ${grades[count]} Letter: C"

	elif [[ ${grades[count]} -ge 80 ]] && [[ ${grades[count]} -lt 90 ]]
        then
                echo "Class: ${courses[count]} Grade: ${grades[count]} Letter: B"
	elif [[ ${grades[count]} -ge 90 ]] && [[ ${grades[count]} -lt 100 ]]
        then
                echo "Class: ${courses[count]} Grade: ${grades[count]} Letter: A"
	else
                echo "Class: ${courses[count]} Grade: ${grades[count]} Letter: Fail"
	fi
	let "count++"
done

#Problem 6
var1=10
var2=20
var3=30
var4=40
var5=50
sum=$(( $var1 + $var2 + $var4 + $var4 + $var5 ))
sub=$(( $var1 - $var2 - $var4 - $var4 - $var5 ))
mult=$(( $var1 * $var2 * $var4 * $var4 * $var5 ))
div=$(( $var5 / $var4 ))

echo "ADD: $var1 + $var2 + $var3 + $var4 + $var5 = $sum"
echo "Subtract: $var1 - $var2 - $var3 - $var4 - $var5 = $sub"
echo "Multiply: $var1 * $var2 * $var3 * $var4 * $var5 = $mult"
echo "Divide: $var5 / $var4 = $div"

