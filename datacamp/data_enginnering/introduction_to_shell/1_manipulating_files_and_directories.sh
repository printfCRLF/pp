#print working directory 
pwd

#listing 
ls
ls /home/repl/seasonal

# if the path starts with /, ls interprets it as an absolute path. 
ls /home/repl 
# if the path starts without /, ls interprets it as a relative path. 
ls seasonal/cummser.csv 

# change directory
# if /home/repl is the home directory, what does cd ~/../. do?
# home directory, up on level, here 


# copy 
cp seasonal/summer.csv backup/summer.bck 

cp seasonal/spring.csv seasonal/summer.csv backup 

# move, mv can also rename a file. 
mv seasonal/spring.csv seasonal/summer.csv backup

# tmp is immediately below the root directory
