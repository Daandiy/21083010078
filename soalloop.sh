#!/bin/bash
echo "INPUTKAN ANGKA = "
read a
for a in {$a..1}
do
if [ $((a%2)) -eq 1 ];
then 
echo $a
fi
done
