# How to deploy to your server using git

## Setting
_You have_

* a git repository on your local machine 
* a server 
* SSH connection to your server 

## Goal
> _You want to_ 

* Use `git` to push any changes to your server _aka_ deploy local changes to your server

## Solution

Setup a github hook for deployment. I followed these resources

1. https://www.youtube.com/watch?v=H6UU7TsyrGs
2. https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa. 

### Post-receive hook

The hook `post-receive` resides in `/home/[username]/[bare-repo-name].git/hooks`. Edit with `nano post-receive` and change _TARGET_ and _GIT\_DIR_. 

* _TARGET_: Your project folder, for example `/home/username/deploy-project`
* _GIT\_DIR_: Bare repository which you created with `git init --bare ~/deploy-github-hook.git`


```bash
#!/bin/bash
TARGET="/home/cloudsigma/deploy-project" # your project folder 
GIT_DIR="/home/cloudsigma/deploy-project-hook.git" # bare repo
BRANCH="master"

while read oldrev newrev ref
do
    # only checking out the master (or whatever branch you would like to deploy)
    if [ "$ref" = "refs/heads/$BRANCH" ];
    then
        echo "Ref $ref received. Deploying ${BRANCH} branch to production..."
        git --work-tree=$TARGET --git-dir=$GIT_DIR checkout -f $BRANCH
    else
        echo "Ref $ref received. Doing nothing: only the ${BRANCH} branch may be deployed on this server."
    fi
done

```

## Checklist for SSH connection

Tutorial for Win 10: [Use SSh with Putty on Windows](https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/)

1. Created a private key with puttygen `[privatekeyname].ppk`
2. Configure the server side following for example [this tutorial](https://bullseyestock.wordpress.com/2018/02/27/setting-up-an-instance-in-cloudsigma/) or [this tutorial from cloudsigma](https://community.cloudsigma.com/hc/en-us/articles/215936063-How-to-generate-OpenSSH-compatible-Keys-for-use-with-PuTTY-and-using-PuTTY-to-access-CloudSigma-s-cloud-using-SSH-)
3. In terminal check logs with SSH verbose
    `ssh -v [server_username]@[host_address]`

    Working example: `ssh -v cloudsigma@99.123.123.123`
