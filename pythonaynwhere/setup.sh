#!/bin/bash
folder="/home/Jocomol/kennzahlen_files"
# Renew folder structure
rm -r $folder &> /dev/null
mkdir $folder &> /dev/null

#Make helpscripts executable
chmod +X ./* &> /dev/null
cp * $folder &> /dev/null

#copy the kennzahlenrechner
cp kennzahlenrechner_shell.py $folder/.. &> /dev/null
cd .. &> /dev/null
cp bilanz.yml $folder &> /dev/null
cp kennzahlenrechner.py $folder &> /dev/null
cp std_kennzahlen.yml $folder &> /dev/null

#dowload requirements
pip3 install -r requirements.txt &> /dev/null

echo "the git folder can now be removed"
