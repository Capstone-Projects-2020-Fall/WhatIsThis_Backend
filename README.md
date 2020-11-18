# WhatIsThis_Backend

## Version Control
For the course of this project, the branching strategy will involve using [git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

This means we will use a master branch for releases and a develop branch to work off of for integrating features. See link above for a more detailed explanation. Whenever a new feature is to be implemented, a feature branch will be created. It's highly recommended that you check out the link above as it will give you a better understanding of what this branching strategy is. This will align with our Rally tickets. The format for creating a new branch is as follows:

*TicketNumber*/*type*-*name*

See an example below

If the rally ticket number is TA111 and it's title is "Implement login feature" it is a feature, then the branch will be named as follows
    TA111/feature-implement-login-feature

If the rally ticket is TA111 "Fix login bug" for a bug fix it will look like 
    TA111/bug-fix-login-bug

Remember, everytime you wish to create a new feature, branch off of develop. This will help to avoid merge conflicts, make it easier to code review changes, amongst many other benefits.

If there is any confusion, see the link above, or talk to the team leader.

If you need a refresher on git, there is a good cheatsheet [here](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet).

## Building Backend server
1. Clone WhatIsThis_Backend repository into desired directory.
2a. If building on Windows, set up WSL 2 https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10
2b. Install Docker ( https://docs.docker.com/get-docker/ ), create Docker account or log into account.
3. Once Docker is successfully downloaded, navigate to "WhatIsThis_Backend/containerized" directory in your shell of choice.
4. Use command "docker build -t <dockerusername>/<appname> ." replacing <dockerusername> with your personal Docker username and <appname> with whatever name you want to give.
5. Once the image has successfully been built from step 4, use command "docker run -p 8080:5000 <dockerusername>/<appname>"
6a. Now your docker container is running, and you can access the image recognition at localhost:8080/predict.
6b. This backend receives POST requests with a base64 encoded image as "imgsource". (To ensure container is running properly, you can check localhost:8080, and you should see a "Hello World!" message)

## Development Environment
1. Python Version : 3.7.9 (64-bit)
2. IDE: Visual Studio Code
3. Libraries (version):
    tensorflow (2.3.1)
    keras (2.4.3)
    opencv (4.0.1)
    numpy (1.18.5)
    flask (1.1.2)