import os,pwd,subprocess

### User Input
name = raw_input("Enter new PC name: ")

### Variables Setup
user = pwd.getpwuid( os.getuid() )[0]
home = "/home/"+ user

### File System I/O
fs = open( home + "/desktop1.po", 'w')
fs.write('msgid "Ubuntu Desktop"\nmsgstr "' + name + '"')
fs.close()

### Translation
os.chdir("/usr/share/locale/en/LC_MESSAGES/")
subprocess.call( ("sudo msgfmt -o unity.mo " + home + "/desktop1.po").split() )


print "You must Login again to bring changes into effect."
res = raw_input("Logout? (y/n) ")

### Final Work
if res in "y yes".split():
    cmd = "sudo pkill -KILL -u " + user
    subprocess.call( cmd.split() )
else:
    exit(0)