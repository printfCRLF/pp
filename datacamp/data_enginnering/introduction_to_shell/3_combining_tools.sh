# use redirection to save any commands's output anywhere you want 
# read last 5 rows from winter.csv, redict the result to last.csv 
$ tail -n 5 seasonal/winter.csv > last.csv

# chain commands together 
tail -n 2 seasonal/winter.csv > bottom.csv
head -n 1 bottom.csv
#2017-08-11,wisdom

# combine commands using pipe | 
# use cut to get 2nd column of the csv file, pipe it to grep, 
# with an inverted search -v, exclude the header column which has text "Tooth"
cut -f 2 -d , seasonal/summer.csv | grep -v Tooth

# more example 
cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 1


# find out how many records in spring/.csv have dates in July 2017 
grep 2017-07 seasonal/spring.csv | wc -l

# use wildcards * to match files 
# display first 3 lines in spring.csv and summer.csv, but not autumn.csv and winter.csv 
head -n 3 seasonal/s*

# Remember the combination of cut and grep to select all the tooth names from column 2 of seasonal/summer.csv?
# sort the names of the teeth in descending alphabetical order 
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r 

# 1. get the second column from seasonal/winter.csv,
# 2. remove the word "Tooth" from the output so that only tooth names are displayed,
# 3. sort the output so that all occurrences of a particular tooth name are adjacent; and
# 4. display each tooth name once along with a count of how often it occurs.
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c 

# wrap it up 
wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1


