# cat, concatenate, print content of files on the screen 
cat course.txt

# less, view file's content piece by piece 
less seasonal/spring.csv seasonal/summer.csv

# print first 10 lines of file 
head people/agarwal.txt
head seasonal/winter.csv -n 5

# list everything below a directory 
ls -R -F

# man, short for manual 
man tail 
tail seasonal/spring.csv -n +7 

# cut, select  columns from file 
cut -d , -f 1 seasonal/spring.csv
cut -d, -f1 seasonal/spring.csv
# both of the commeands select column 1 (-f 1) from the file that uses (-d ,) as the delimiter

# history 
# !head
history
head summer.scv
# !head to rerun the last head command with parameters
!head

# grep, global regular exrepssion print 
grep molar seasonal/autumn.csv
##  result 
# 2017-02-01,molar
# 2017-05-25,molar

# use -v to invert the matchn and use -n to show line numbers
grep -v -n molar seasonal/spring.csv

# use -c to count how the number of occurences of the word incisor in files autumn.csv and winter.csv 
grep -c incisor seasonal/autumn.csv seasonal/winter.csv

# paste, paste columns together / concate lines sequentially from two files 
$ paste -d , seasonal/autumn.csv seasonal/winter.csv

