# how can I edit a file 
# Ctrl + K, delete a line 
# Ctrl + U, un-delete a line 
# Ctrl + O, save the file (O stands for output)
# Ctrl + X, exit the editor


## How can i record what I just did 
# 1. Copy the files seasonal/spring.csv and seasonal/summer.csv to your home directory.
cp seasonal/spring.csv seasonal/summer.csv ~

# Use grep with the -h flag (to stop it from printing filenames) and 
# -v Tooth (to select lines that don't match the header line) 
# to select the data records from spring.csv and summer.csv 
# in that order and redirect the output to temp.csv.
grep -h -v Tooth spring.csv summer.csv >  temp.csv

# Pipe history into tail -n 3 and redirect the output to steps.txt 
# to save the last three commands in a file. 
# (You need to save three instead of just two because the history command itself will be in the list.)
history > tail -n 3 > steps.txt

## result 


# how can I re-use pipe 
nano teeth.sh
bash teeth.sh > teeth.out
cat teeth.out

# how do I pass filenames to scripts 
bash count-records.sh seasonal/*.csv > num-records.out

# how can one shell script do many things 
bash range.sh seasonal/*.csv > range.out

# find date range
bash date-range.sh seasonal/*.csv | sort