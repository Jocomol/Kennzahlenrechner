#!/bin/bash
folder="/var/kennzahlenrechner"
# Renew folder structure
rm -r $folder
mkdir $folder

#Make helpscripts executable
chmod +X ./*

#move helpscripts to /usr/bin
cp start.sh /usr/bin/start
cp bilanz.sh /usr/bin/bilanz
cp kennzahlen.sh /usr/bin/kennzahlen
cp kennzahlenhelp.sh /usr/bin/kennzahlenhelp

#copy the kennzahlenrechner
cd ..
cp bilanz.yml $folder
cp kennzahlenrechner.py $folder
cp std_kennzahlen.yml $folder

#dowload requirements
pip3 install -r requirements.txt

echo "the git folder can now be removed"
