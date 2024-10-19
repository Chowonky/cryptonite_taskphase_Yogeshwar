# Pondering PATH

### The PATH Variable
- `PATH=""`
- `/challenge/run`

### Setting PATH
- `PATH="/challenge/more_commands/" `
- `/challenge/run `

### Adding Commands
- `echo cat /flag > win`
- `export PATH=$PATH:/home/hacker`
- `chmod u+x,g+x,o+x win`
- `/challenge/run`

### Hijacking Commands
- `nano rm`
  - `read x < /flag`
  - `echo $x`
- `chmod a+x rm`
- `PATH=""`
- `PATH=/home/hacker/`
- `export PATH`
- `/challenge/run`

