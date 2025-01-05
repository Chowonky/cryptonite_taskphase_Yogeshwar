# File Globbing
### Matchinng with *
- `cd /c*`
- `/c*/r*`
### Matching with ?
- `cd /?ha??enge`
- `/challenge/run`
### Matching with []
- `cd /c*/f*`
- `/c*/r* file_[bash]`
### Matching paths with []
- `/c*/r* /challenge/files/file_[bash]`
### Mixing globs 
- `cd /c*/f*`
- `/challenge/run [cep]*`
### Exclusionary globbing
- `cd /challenge/files/`
- `/c*/r* [!pwn]*`
