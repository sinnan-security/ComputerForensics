# Exam deployment instuctions
change ip address in the files:
1. generators/client.py
2. generators/run.sh
```bash
gcc confusers/src/git.c -o confusers/git
gcc confusers/src/mongodb.c -o confusers/mongodb
gcc confusers/src/nginx.c -o confusers/nginx
gcc confusers/src/node.c -o confusers/node
gcc confusers/src/postgres.c -o confusers/postgres
gcc confusers/src/redis.c -o confusers/redis
gcc confusers/src/webhooks.c -o confusers/webhooks
docker-compose build
sudo docker-compose up &
./generators/run.sh &
python3 generators/client.py
```

# Marking scheme with ideal answers!

# Evidence Collection
1. Login to machine via ssh.
```bash
native_machine> ssh -p 7022 root@target
```
2. Copy files from target to local.
```bash
native_machine> scp -r -P 7022 root@target/var/log /home/student/ComputerForensics/data/artifacts/var/log
native_machine> scp -r -P 7022 root@target/home /home/student/ComputerForensics/data/artifacts/home
native_machine> scp -r -P 7022 root@target/etc /home/student/ComputerForensics/data/artifacts/etc
```
3. Extract the process list.
```bash
root@target> ps -aux
```
4. Create memory dumps:
   1. Create the memory dumping script.
```bash
native\_machine> gedit dump_mem.py
```
   2. Modify script to include the process needed.
```python
import sys
pid=[1,2,3,4,5,6,7,8,9....]
for i in pid:
	map_file = f"/proc/{pid}/maps"
	mem_file = f"/proc/{pid}/mem"
	out_file = f"{pid}.dump"
	out_file = f"{pid}.map"
	mapf=open(map_file, 'r')
	memf=open(mem_file, 'rb')
	outf=open('dump_'+str(i), 'wb')
	for line in mapf.readlines():
		section=line.split(' ')
		if section[1][0]=='r':
			addresses=section[0].split('-')
			start=int(addresses[0],16)
			end=int(addresses[1],16)
			memf.seek(int(addresses[0],16))
			try:
				outf.write(memf.read(end-start))
			except OSError:
				print(hex(start), '-', hex(end), '[error,skipped]', file=sys.stderr)
```
   3. Copy the script from local to target.
```bash
native_machine> scp -P 7022 dump_mem.py root@target/tmp/deleteafteruse/script.py
```
   4. Run the script and generate the dumps.
```bash
root@target> cd /tmp/deleteafteruse
root@target> python3 script.py
```
   5. Copy the the dumps from target to local.
```bash
native_machine> scp -r -P 7022 root@target/tmp/deleteafteruse /home/student/ComputerForensics/data/artifacts/mem_dumps
```
# Investiagtion
The environment setup below is optional.
```bash
native_machine> docker-compose build
native_machine> sudo docker-compose up
native_machine> docker ps
native_machine> docker exec -it your_container /bin/bash
your_container>
```
5. The suspicious process is MWzF2MqBWW because its linked to our complaint.
Search for this process in your local container.
```bash
your_container> find / | grep "MWzF2MqBWW"
```
source file is available at /home/src/MWzF2MqBWW.c
```bash
your_container> cat /home/src/MWzF2MqBWW.c
```
first line is "#include <stdio.h>"
6. Extract partial strings from the source file and put them in a YARA rule.
```yara
rule malicious{
	strings:
		$error_msg0="gethostbyname"
		$error_msg1="setsockopt"
		$error_msg2="Usage:"
		$error_msg3="connect"
		$unique_str="GET /Me5HIC2ibF"
	condition:
		$error_msg0 and $error_msg1 and $error_msg2 and $error_msg3 and $unique_str
	}
```
7. Run signature against each memory dump.
```bash
your_container> python -r malicious.yara /home/artifacts/dump_1
your_container> python -r malicious.yara /home/artifacts/dump_2
your_container> python -r malicious.yara /home/artifacts/dump_3
...
```
It matches the dump of the python3 app.py process
8. Find the python source code that is being run.
```bash
your_container> find / | grep "app.py"
your_container> cat app.py
```
/var/log/python/flask/app.log
9. Find any of the partial strings present in the log file.
```regex
Request Log-+ POST \/token\? .*MWzF2MqBWW.*
```
10. Match the regex against the rule file
```
python -r "regex" /home/artifacts/var/log/python/flask/app.log
```
Partial match: body:{"username": "cust1", "password": "RestlessSou7"};p=open("MWzF2MqBWW.c","w")
# Analysis
11.	Attacker exploits the application app.py by injecting executable code
	The code executes causing a file to be written. The file is C source.
	The source file is compiled to a program
	The program is run and the suspicious process is created.
# Conclusion
12.	The attacker leverages a code injection vulerability in the python applicaton to create malicious process on the target machine.
	because the payload contained executable code in python.
13.	cust1 was responsible for the attack
	because the payload contains the correct password for the user account which could only have been known by cust1.
14.	the attack aimed to create a botnet aimed at targeting google.com
	because the malicious process sends requests to google.com.
