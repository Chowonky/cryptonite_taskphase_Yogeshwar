# Shell Variables
### Printing Variables
- used `echo $FLAG` 

### Setting Variables
- used `PWN=COLLEGE` to set the value `COLLEGE` to the variable `PWN`  

### Multi-word Variables
- used `PWN="COLLEGE YEAH"` to set the value `COLLEGE YEAH` to the variable `PWN`

### Exporting Variables
- used `export PWN=COLLEGE` to set the value `COLLEGE` to the variable `PWN` and export the `PWN` variable
- used `COLLEGE=PWN`
- used `/challenge/run` to get the flag 

### Printing Exported Variables
- used `env` and found the flag

### Storing Command Output
- `PWN=$(/challenge/run)` sets the output of `/challenge/run` to `PWN` variable
- echo `$PWN` prints the value contained in the variable `PWN`

### Reading Input 
- `read PWN` to read input from user and store it in the variable `PWN`
- entered `COLLEGE` and got the flag

### Reading Files
- `read PWN < /challenge/read_me`, this executes `/challenge/read_me` and redirects its output to `read PWN` as an input
