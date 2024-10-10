# Practicing Piping
### Redirecting output
- `echo PWN > COLLEGE` 
### Redirecting more output
-  `/challenge/run > myflag` 
-  `cat myflag` 
### Appending output
-  `/challenge/run >> /home/hacker/the-flag` 
-  `cat /home/hacker/the-flag` 
### Redirecting errors
-  `/challenge/run > myflag 2> instructions` 
-  `cat instructions` 
-  `cat myflag` 
### Redirecting input
-  `echo COLLEGE > PWN` 
-  `/challenge/run < PWN` 
### Grepping stored results
-  `/challenge/run > /tmp/data.txt` 
-  `cat /tmp/data.txt | grep pwn.college` 
### Grepping live output
-  `/challenge/run | grep pwn.college`
### Grepping errors
-  `/challenge/run 2>& 1 | grep pwn.college` 
### Duplicating piped data with tee
-  `/challenge/pwn | tee pwn_output | /challenge/college` 
-  `/challenge/pwn --secret UMx2IeYJ | /challenge/college` 
### Writing to multiple programs
-  `/challenge/hack | tee >(/challenge/the) >(/challenge/planet)` 
### Split-piping stderr and stdout
-  `/challenge/hack 2> >(/challenge/the) > >(/challenge/planet)` 