# ComputerForensics
Course Content and Orientation for Computer Forensics

# The Rules
1. Pay attention in class.
2. Do not worry about scoring the best marks.
3. Research vital stuff before showing up.
4. Revise and revsit whats being taught.
5. Practice what you learnt.
6. Eat, drink, talk and have fun everything is allowed unless its explicitly forbidden.

# Assignments:
1. Add a mechanism for creating an integrity record of your disk backups. Your mechanism should be secure.
2. Create (from scratch) a difference tool that checks each file and its contents in a directory against a baseline.
3. Extend the YARA signature matching to search directories.
4. Extend the regular expression matching to search directories.
5. Create your own YARA rules that can detect the samples provided [This]. (https://github.com/ytisf/theZoo/tree/master/malware/Binaries/Ransomware.WannaCry).

# Extra Credit:
1. Point out my mistakes.
2. Contribute to the codebase.
3. Participate in security related contests.
4. Submit a book review on topics related to security.
5. Publish an article related to security.

# Running Containers:
1. go into your container directory where there are docker-compose.yml file reside.
2. run docker-compose build
3. run docker-compose up as sudo
4. open up a new terminal
5. docker ps
6. select the container you want to use and run docker exec -it container_id /bin/bash

# Project Ideas:
1. Deploy Cuckoo sandbox within a container.
- Knowledge required: Dockers, QEMU/KVMs, MongoDB.
- Difficulty rating: 3/10
2. Develop system call injection capabilities for android.
- Knowledge required: C/++,x86-Assembly,Linux Kernel
- Difficulty rating: 7/10
3. Develop system call injection capabilities for windows.
- Knowledge required: C/++,x86-Assembly,Windows kernel
- Difficulty rating: 5/10
4. Create a virtualised enviroment such that it passes most/all checks against [This].(https://github.com/LordNoteworthy/al-khaser)
- Knowledge required: QEMU/KVMs,Research
- Difficulty rating: 4/10
5. Multithread all of the scripts provided in the duration of the course.
- Knowledge required: Python,Data structures and algorithms,Parellal computing
- Difficulty rating: 2/10
6. Develop realtime incident monitoring mechanisms into any web application.
- Knowledge required: Python,Nginx,Web application frameworks.
- Difficulty rating: 6/10
7. You can propose your own as well. But if you do i will set the requirements.

# Examination guidelines:
1. Prepare by practicing and research.
2. You will be asked to demonstrate your learning.
3. All marking schemes will be provided 1 hour after the exam ends.
4. You may bring a single A4 sized sheet with anything written on it in the examination.
5. You will each get a challenge that will be solved the same way but will yield different answers for each of you.
6. It is possible to take shortcuts in the exam but I will immediately know who did so.
7. You will be provided the questions 5 minutes before the start of the examination make sure you read the tasks thoroughly.
8. You will be allowed an additional 15 minutes at the end of the exam to recheck all of your work.
9. Before you leave kindly check if you have attempted all of the questions.

# Grading
Fail:	mean-0.75*std_dev
2.00:	mean-0.50*std_dev
2.33:	mean-0.25*std_dev
2.67:	mean
3.00:	mean+0.25*std_dev
3.33:	mean+0.50*std_dev
3.67:	mean+0.75*std_dev
4.00:	mean+1.00*std_dev

# Thanks!
