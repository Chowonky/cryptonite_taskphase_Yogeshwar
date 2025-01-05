# Perceiving Permissions

### Changing File Ownership
- `chown hacker /flag` to change owner to `hacker`
- `cat /flag`

### Groups and Files
- `chgrp hacker /flag` to change group to `hacker`
- `cat /flag`
### Fun with Group Names
- `id` to check group name
- `chgrp grp25146 /flag`
- `cat /flag`

### Changing Permissions
- `chmod o+r /flag` to give `read` access to other users

### Executable Files
- `chmod u+x /challenge/run` to give `execute` access to the user `hacker`

### Permission Tweaking Practice 
- `/challenge/run`
- `chmod u+x,o+x /challenge/pwn` had to google how to specify multiple permissions (using `,` operator)
- `chmod g+x /challenge/pwn`
- `chmod g-r /challenge/pwn`
- `chmod u-r,u-x,g-x /challenge/pwn`
- `chmod u-w /challenge/pwn`
- `chmod u+w,u+x,g+x,g+w /challenge/pwn`
- `chmod g-w /challenge/pwn`
- `chmod u-w,u-x,g-x,o-x /challenge/pwn`
- `chmod u+r /flag`
- `cat /flag`

### Permission Setting Practice
- `/challenge/run`
- `chmod u=r,g=x,o=rwx /challenge/pwn`
- `chmod u=-,g=wx,o=rx /challenge/pwn`
- `chmod u=rx,g=x,o=wx /challenge/pwn`
- `chmod u=x,g=w,o=- /challenge/pwn`
- `chmod u=r,g=wx,o=x /challenge/pwn`
- `chmod u=wrx,g=r,o=r /challenge/pwn`
- `chmod u=wx,g=-,o=r /challenge/pwn`
- `chmod u=w,g=wx,o=w /challenge/pwn`
- `chmod u=wrx /flag`
- `cat /flag`

### The SUID Bit
- `chmod u+s /challenge/getroot`
- `/challenge/getroot`
- `cat /flag`

