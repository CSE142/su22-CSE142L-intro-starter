# Introduction to the Development Environment

[![Build Status](https://travis-ci.com/NVSL/CSE141pp-Lab-Introduction-to-the-Development-Environment.svg?token=93Do9H82syZrfwMiQex8&branch=master)](https://travis-ci.com/NVSL/CSE141pp-Lab-Introduction-to-the-Development-Environment)

In this lab you will set up the lab environment and learn how gather
information about programs using the course tools.  You will download
some starter code, build and run it in a Docker container, modify the
code and push the changes to a git repo.  Run the code in the cloud on
our reference processor to gather some data.

This lab will be completed on your own.  Completing this lab in a
timely manner is necessary for passing this course.

Check the course schedule for due date(s).

**Skills to Learn**

1. Install and use Docker
2. git/GitHub basics
3. Building and modifying lab code
4. Running a job on the autograder

## Academic Integrity Agreement

Open the file `ExcelWithIntegrity.md`, read it, and fill out the form
and sign it as directed.  The document describes the expectations for
this class regarding academic intergrity.

Commit and push the modified file.

## Software You Will Need

1. A computer with Docker installed (either the basement CSE labs, or your own laptop).

2. The lab for the github classroom assignment for this lab:  https://classroom.github.com/a/gNSleHrN

**Note** Starting early on the lab is a form of cheating.  If you are
  in Section B, don't click on the Section A link.  If you do by
  accident, let us know immediately.

## Tasks to Perform

### Fill Out The Self Evaluation

Login to your __@ucsd.edu__ gmail account and fill out [this
survey](https://docs.google.com/forms/d/e/1FAIpQLSfLCN85SHaJr5dGAElpZWOPK0sRrbyWqIBcOD4ZW4rxnjjgJA/viewform).
You do not need to do this again if you already filled it out for CSE
142.

### Get set up Github

We are going to use Github classroom for this course. You'll need to
[create a Github account](https://github.com/), if you don't already
have one.  For each part of the project, there will be an assignment
setup on Github.

First, you'll need to authorize github classroom to access your github account. 
To do that, visit https://classroom.github.com and sign in with your github account.

We will be using Github a lot in class.  If you aren't familiar with
it, there are a bunch of good introductory tutorials.  For example,
[this one](http://try.github.io/).

### Get Docker Working

All your work for the class will be done in a docker container.
Docker containers are self-contained Linux-based workspaces.  Using
docker ensures that your code runs in a consistent environment for you
and the autograder/course staff.

There are several different methods
you can use to get access to a machine running docker.

#### Use dsmlp-login.ucsd.edu

This is the official way to use the class infrastructure.  If you have trouble getting any of the other options to work, use this.

Login to 'dsmlp-login.ucsd.edu' (our primary student Linux SSH server) using you normal student login.

Run the command `launch-142` to connect to a remote Docker container running the development environment image.

Here's a transcript of the login process for user `cs142lsp21zz`:

```
$ ssh cs142lsp21zz@dsmlp-login.ucsd.edu
To see all available software packages, type "prep -l" at the command prompt,
or "prep -h" for more options.
============================ NOTICE =================================
Authorized use of this system is limited to password-authenticated
usernames which are issued to individuals and are for the sole use of
the person to whom they are issued.

Privacy notice: be aware that computer files, electronic mail and 
accounts are not private in an absolute sense.  You are responsible
for adhering to the ETS Acceptable Use Policies, which you can review at:
https://blink.ucsd.edu/faculty/instruction/tech-guide/policies/ets-acceptable-use-policies.html
=====================================================================

*** Data Science and Machine Learning Platform Resources ***
    
    How to Launch Containers From the Command Line: 
    https://support.ucsd.edu/services?id=kb_article_view&sysparm_article=KB0032269

    How to Select and Configure Your Container:
    https://support.ucsd.edu/services?id=kb_article_view&sysparm_article=KB0032273

    Building Your Own Custom Image:
    https://github.com/ucsd-ets/datahub-example-notebook

    Your instructor or TA will be your best resource for course-specific questions.
    
    If you still have questions or need additional assistance, please email dsmlp@ucsd.edu 
    to create a support ticket.


-------------------------------------------------------

quota: No filesystem specified.
Hello cs142lsp21zz, you are currently logged into dsmlp-login.ucsd.edu

You are using 0% CPU on this system

[cs142lsp21zz@dsmlp-login]:~:1$ launch-142
Attempting to create job ('pod') with 4 CPU cores, 16 GB RAM, and 0 GPU units.
   (Adjust command line options, or edit "/software/common64/dsmlp/bin/launch-142.sh" to change this configuration.)
pod/cs142lsp21zz-1435 created
Sat Apr 3 16:40:17 PDT 2021 starting up - pod status: Pending ; Successfully assigned cs142lsp21zz/cs142lsp21zz-1435 to its-dsmlp-n25.ucsd.edu
Sat Apr 3 16:40:23 PDT 2021 pod is running with IP: 10.40.224.4 on node: its-dsmlp-n25.ucsd.edu
ucsdnvsl/cse141pp:latest is now active.

Connected to cs142lsp21zz-1435; type 'exit' to terminate pod/processes.
/course/CSE141pp-Config ~
cat: /course/CSE141pp-Config/secrets/packet_auth_token: No such file or directory
Welcome to the archlab development environment!
STUDENT_MODE enabled
THIS_DOCKER_IMAGE=ucsdnvsl/cse141pp:sp21.142
IN_DEPLOYMENT=DEPLOYED
CLOUD_MODE=CLOUD
[cs142lsp21zz@dsmlp-login]:~:2$
```

To make sure everything is working, you can run `runlab --help`.  You should get this:

```
cs142lsp21zz@cs142lsp21zz-10005:~$ runlab --help
usage: runlab [-h] [-v] [--pristine] [--info [INFO]] [--no-validate] ...

Run a Lab

    Running the lab with this command ensure that your compilation and
    execution enviroment matches the autograder's as closely as possible.

    Useful options include:

    * '--no-validate' to run your code without committing it.
    * '--info' to see the parameters for the current lab.
    * '--pristine' to (as near as possible) exactly mimic how the autograder runs code.

positional arguments:
  command        Command to run (optional). By default, it'll run the command
                 in lab.py.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Be verbose
  --pristine     Clone a new copy of the reference repo.
  --info [INFO]  Print information about this lab an exit. With an argument
                 print that field of lab structure.
  --no-validate  Don't check for erroneously edited files.
cs142lsp21zz@cs142lsp21zz-10005:~$
```

If you go this route, you can skip instructions below regarding running `docker` directly.

You can then clone your repo in the directory that you land in and work on it.

Your files inside the `launch-142` environment are stored in this system: https://datahub.ucsd.edu/hub/login.

#### Run Docker Locally on Your Mac

Start by following the instructions here to install docker:
https://docs.docker.com/install/.  This seems to work pretty easily,
but the course staff is not able to assist in getting docker running
on your Mac.

Once that's done, you should be able to run `docker` in the terminal (see [here](#start-a-docker-container) to learn how
to run the container)

One thing to keep in mind:  The docker image large (~18GB) and you'll need to devote at least 2GB of DRAM to it.


#### Run Docker on Your Windows Machine

It is possible to run Docker on Windows, but we've had many issues
with, and we don't support it.  The lab staff is not able to assist
with getting docker running under windows.

One thing to keep in mind:  The docker image large (~18GB) and you'll need to devote at least 2GB of DRAM to it.

[Here](https://hub.docker.com/editions/community/docker-ce-desktop-windows) is a
short tutorial to help you install Docker on Windows 10.

1.  Install Windows 10 Pro or Education
    - If you have Windows 10 Pro or Education, continue to step 2. If you do not have Windows 10 Pro or Education, follow the steps below.
    - Follow the link below to get a free license for Windows 10 Education. You will have to make an account in order to get the free code. You must use your UCSD email.
[https://ucsd.onthehub.com/WebStore/OfferingDetails.aspx?o=9b3bfdc0-71e9-e611-9425-b8ca3a5db7a1](https://ucsd.onthehub.com/WebStore/OfferingDetails.aspx?o=9b3bfdc0-71e9-e611-9425-b8ca3a5db7a1)
    - Go to your windows 10 settings -> Update & Security -> Activation -> Change Product Key. Copy and paste your free key and install Windows
2.  Install Docker Desktop
    - Follow this link to download the docker desktop installer. You will need to create an account. Please do not install docker toolbox.
[https://hub.docker.com/?overlay=onboarding](https://hub.docker.com/?overlay=onboarding)
    - Run the installer and if it asks to enable hyper-v after it installs say yes. Your computer may need to restart.
    - Upon restarting, run docker desktop. You’ll know docker has started when the icon in your system tray stops animating.
    - Right click the docker icon and go to settings -> shared drives and click the checkbox next to the drive you wish to keep your labs on. You will need to enter your account password.
3.  Test your install
Open powershell and run the command:
```
docker run hello-world
```
Your output should look like this. (You may have extra text pulling the hello-world image)
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
4. To start docker into the development environment for the labs
Run the command replacing the tagged parts  (see [here](#start-a-docker-container) for more details):
```
docker run -it --volume <Directory to your lab folder>:/runner/<Your lab folder name> ucsdnvsl/cse141pp:latest
```


Change directories to land where your files should be.
```
cd ../runner
```

#### Use VirtualBox to Run Linux (on Mac or Windows if you have Intel VT-X or AMD-V support)

1.  Download and install VirtualBox: https://www.virtualbox.org/wiki/Downloads
2.  Open VirtualBox
3.  Click "New"
4.  Set "Type" = "Linux" and "Version" = "Ubuntu (64-bit)".
5.  The VM will need at least a couple GB of memory.
6.  Click through the default to create a disk.  You'll need at least 30GB.
7.  Download this: http://releases.ubuntu.com/16.04/ubuntu-16.04.6-desktop-amd64.iso 
8.  Go to `Settings->Storage`, click the '+' disk icon to add an optical drive.  Then `Add` and select the iso image above.  Click 'ok'.
9.  Click 'start' -- your VM should boot.
10. Click 'Install Ubuntu' and accept all the defaults.
    - If you are unable to see the buttons due to the screen being too small, you can press and hold *Alt* in windows then click the mouse to move the screen around.
11. Restart the VM when asked.
12. When it comes back, right click->Terminal.
13. Install docker with `sudo apt-get install docker.io`.
14. Follow these instructions to install the "Guest Additions": https://www.virtualbox.org/manual/ch04.html#additional-linux-install.  This will make working with the VM easier.
   

Type `docker --help ` at the command line.  It should printout some usage information:

```
Usage:    docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/home/swanson/.docker")
      -D, --debug              Enable debug mode
      -H, --host list          Daemon socket(s) to connect to
...
```

#### Use Docker for Windows (on Windows if you don't have Intel VT-X or AMD-V support)

Follow directions here: https://docs.docker.com/docker-for-windows/

### Start a Docker Container

This only applies if you are running docker on your own machine (i.e., not on `dsmlp-login`).  If you are running on `dsmlp-login`, then you should skip this.

The docker image you'll be using is `ucsdnvsl/CSE141pp:latest`.

You can start it from the command line with `docker run -it ucsdnvsl/cse141pp:latest`.

It may take a while the first time (the docker image is about 9GB), but you should eventually find yourself in a shell. 

**NOTE**: This is very important:  With the command above, none of your work work will be saved when the container exits.  You have several choices:

1. Always commit and push your code to github and re-clone it when you start docker.

2. Use the campus-provider docker facilities in which case you should also commit your work frequently.  Don't rely on the data on those machines being persistent.

3. Use the `--volume` option to give your docker container access to the files from outside of docker.

For example, this command line:

```
docker run -it --volume $HOME:/home/ -w /home --env HOME=/home ucsdnvsl/cse141pp:latest
```

Does the following,

* `-it` makes the docker container interactive.
* `--volume $HOME:/home` will make your home directory appear inside docker as `/home`.
* `-w` will make your working directory inside docker be `/home`.
* `--env HOME=/home` sets your home directory to `/home`.

So that I can do the following (the `root@0d67aa337a42:` prompt means I'm inside the container):

```
root@packet-devel1-test:~# cd $HOME
root@packet-devel1-test:~# ls
cse141pp-archlab  CSE141pp-Config  CSE141pp-Resources  CSE141pp-SimpleCNN  gradescope.zip  labs  old  python-docs-samples  swanson  t  test  toy.cpp  tt
root@packet-devel1-test:~# docker run -it --volume $HOME:/home/ -w /home --env HOME=/home ucsdnvsl/cse141pp:latest
root@0d67aa337a42:~# ls
CSE141pp-Config  CSE141pp-Resources  CSE141pp-SimpleCNN  cse141pp-archlab  gradescope.zip  labs  old  python-docs-samples  swanson  t  test  toy.cpp  tt
root@0d67aa337a42:~# touch hello-world
root@0d67aa337a42:~# exit
exit
root@packet-devel1-test:~# ls
cse141pp-archlab  CSE141pp-Config  CSE141pp-Resources  CSE141pp-SimpleCNN  gradescope.zip  hello-world  labs  old  python-docs-samples  swanson  t  test  toy.cpp  tt
root@packet-devel1-test:~#
```

Note that I can see the contents of my home directory from inside
docker, and changes I make inside remain after I exit.  You may need
to tweak the command to suit you needs.

### Testing Your Docker Container

Once you are in a docker container, you can test it by running:

```
runlab --help
```

You should see something like this:

```
usage: runlab [-h] [-v] [--pristine] [--info [INFO]] [--no-validate] ...

Run a Lab

    Running the lab with this command ensure that your compilation and
        execution enviroment matches the autograder's as closely as possible.

    Useful options include:

    * '--no-validate' to run your code without committing it.
    * '--info' to see the parameters for the current lab.
    * '--pristine' to (as near as possible) exactly mimic how the autograder runs code.

positional arguments:
  command        Command to run (optional). By default, it'll run the command
                   in lab.py.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Be verbose
  --pristine     Clone a new copy of the reference repo.
  --info [INFO]  Print information about this lab an exit. With an argument
                 print that field of lab structure.
  --no-validate  Don't check for erroneously edited files.
```

You can now proceed to clone the git repo as described below.


### Get a Copy of the Starter Code

First, accept the assignement on Github Classroom.  See the links at the top of the lab.

This will set you up with a copy of the starter repository.

Use `git clone` to clone your repo locally.

There are a few files:

- `code.cpp` -- the code you'll modify.
- `main.cpp` -- The "driver" code that calls the code in `code.cpp`.
- `config.env` -- a configuration file you can use to control how your code is built and run on the autograder.
- `Makefile` -- The makefile for the lab.  It builds `code.exe`
- `lab.py` -- A python file that configures the lab.

You should only modify `code.cpp` and `config.env`.  Changes to the
other files __will not affect how things run on the autograder__ but
they will affect how things run locally.  If you change them, your
local results will not match the autograder results, which will probably be
confusing.

### Test the Starter Code Locally

In the example commands that follow, we'll assume your github username is `stevenjswanson`.

Navigate to
`/home/sp21-CSE142L-intro-stevenjswanson` and
run `runlab`.  This will compile the starter code into
`code.exe` and run it.

You can compile and run `code.exe` directly, but using `runlab` mimics how your
code will be run on the autograder, so it's a good idea to use it.

The output will be pretty long, but in middle somewher it should say
"Hello, world!".

Save the output of `code.exe` as `outputs/starter-output.txt` and
commit to Github:

```
git add outputs/starter-output.txt
git commit -m 'starter output'
git push
```

### Modify the Starter Code

Open up `code.cpp`.  The function `greet()' takes two arguments, a name and a
salutation (e.g., "Hello", "Good morning").

Modify the function to output "<salutation>, <name>!" using those variables (e.g., "Hello, Ada!") instead of "Hello, world!".

It's C++, so you should use `std::cout` and the `<<` opererator.

Try to test it:

```
runlab
```

Uh oh!:

```
  code.cpp  | 1 +
  1 files changed, 1 insertions(+), 1 deletion(-)
  ERROR    You have uncommitted changes and/or there is changes in github that you don't have locally.  This means local behavior won't match what the autograder will do.
  ERROR    To run anyway, pass '--no-validate'.  Alternately, to mimic the autograder as closely as possible (and require committing your files), do '--pristine'
```

`runlab` is telling you that the local doesn't match what you've
checked in, so the results you get here won't match what the
autograder will see.  That's ok, since we are still testing, so just do

```
runlab --no-validate
```

You should see the output change to `Howdy, Ada!`.

Push your changes and the output to Github:

```
git add code.cpp outputs/modified-output.txt
git commit -m 'personalized greeting'
git push
```

Now, `runlab` should work without `--no-validate`.  Verify that it does.

### Controlling How the Code Runs

There are factors besides the source code that affect how a program behaves.
You can set these via the `config` file.  `runlab` reads this file to configure
your experiment.

If you open `config.env` you'll see two line:

```
EXTRA_OPTIONS=
salutation=
```

`EXTRA_OPTIONS` lets you pass command line options to `code.exe`.  In this
case, we set the name by passing `--name` (e.g., `EXTRA_OPTIONS=--name Steven`).

`salutation` is a lab-specific configuration option.  A value of
`formal` (i.e., `salutation=formal`) will set the salutation to
"greetings".  You can see the available lab-specific options and
values with `runlab --info` (try it!).

Edit `config.env` to change the salutation to `short` and make it print
your name, and run your code again with

```
runlab  --no-validate
```

You should see those change reflected in the output (e.g., `hi,
Steven`).  Once you have the settings to your liking, commit them.

**NOTE**: You may be tempted to try to add them to `Makefile` instead
of `config`, since there are commandline options in there as well.
However, the autograder ignores the `Makefile` in your
repo, so changes there will have no effect on what runs on the
autograder.

### Running the Course Instrumentation Script in the Cloud

The Gradescope autograder is able to run more tests on your code on
our reference processor.  In this lab we will measure execution time
and energy.

1. Log into Gradescope. 

2. Click on your section of 142L.

3. Click `Introduction to the development environment`.

4. Click `Submit` (bottom right).

5. Select `Github`

6. Enter the name of your repo (e.g., `sp21-CSE142L-intro-stevenjswanson')

7. Select the `master` branch.

8. Click `Upload`

The first contains the `stdout` and `stderr` of your code.

Then, there are several sections that represent different parts of the
assignment.  Each of them has a score associated with it, but many of
them are labeled "0.0/0.0".  This means the box just contains some
information is not a graded part of the assignment.

If a box has a non-zero denominator, then it is actually graded (see the rubric below).

The first box has a url for a zip file with the outputs of this run.
Paste it into a web browser (you may need to log into google), open it, and
you'll find all the inputs and outputs for lab.

This is how you'll access all the inputs and outputs for the lab.

After the URL are the graded sections of the lab.  Here, you'll see
one "question" corresponding to each of the files we asked you to save
during the lab.

Finally, there's some JSON that has some information that might be
useful to course staff in debugging an problems that you have.

## When You Are Done

You can resubmit as many times as you'd like.  We'll use the latest submit before the deadline.

### Rubric

- Successfully submitting something to gradescope (3pts)
- Commiting initial output with "Hello, world!". (1pts)
- Correctly modifying the code and editing `config.env` (3pts)
