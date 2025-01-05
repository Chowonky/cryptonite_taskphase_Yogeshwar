# Processes and Jobs

### Listing Processes
- `ps aux` 
- found `/challenge/6517-run-31780`
- ran it and got the flag

### Killing Processes
- `ps aux | grep dont_run` to get the PID
- `kill 73`
- `/challenge/run` to get the flag
  
### Interupting Processes 
- `/challenge/run`
- `^C` (Ctrl+C) to get the flag
  
### Suspending Processes
- `/challenge/run`
- `^Z` (Ctrl+Z) to suspend the process
- `/challenge/run` again to get the flag

### Resuming Processes
- `/challenge/run`
- `^Z` to suspend
- `fg` to bring back the process to foreground

### Backgrounding Processes
- `/challenge/run`
- `^Z`
- `bg`
- `/challenge/run`  

### Foregrounding Processes
- `/challenge/run`
- `^Z` suspends the process
- `bg` backgrounds the process
- `fg` brings it back to foreground

### Starting Backgrounded Processes
- `/challenge/run &`
  
### Process Exit Codes
- `/challenge/get-code` t
- `echo $?` to get the error code
- `/challenge/submit-code 168` passing the error code as an argument to `/challenge/submit-code` to get the flag
