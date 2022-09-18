echo -n "berapa berat badanmu?"
read berat

if (( berat <= 60 )); then
  echo "maaf kamu terlalu kurus"
elif (( berat <= 100 )); then
 echo "yeay kamu berat sekali"
else
 echo " maaf beratmu kurang sesuai kriteria:("
fi
