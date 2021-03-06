# use set to display a list of environment variables 
# use set and grep to display how many old commands by default are stored in the system 
set | grep HISTFILESIZE

echo $OSTYPE

# create temporarily variable in the shell 
testing=seasonal/winter.csv
head -n 1 $testing

# loop
for filetype in docx odt pdf; do echo $filetype; done

# print all the file names in the directory people 
for filename in people/*; do echo $filename; done

#Write a loop that prints the last entry from July 2017 (2017-07) in every seasonal file. It should produce a similar output to:
for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done



