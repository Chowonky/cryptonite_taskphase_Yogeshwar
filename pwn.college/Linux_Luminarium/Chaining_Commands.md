# Chaining Commands

### Chaining with semicolons
- `/challenge/pwn; /challenge/college`
  
### Your first shell script
- `echo /challenge/pwn > x.sh `
- `echo /challenge/college >> x.sh`
- `bash x.sh`

### Redirecting script output
- `echo /challenge/pwn > x.sh; echo /challenge/college >> x.sh`
- `bash x.sh | /challenge/solve`

### Executable shell scripts
- `echo /challenge/solve > x.sh`
- `chmod u=wrx ./x.sh`
- `./x.sh`
