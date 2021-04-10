# How to deploy to your server using git

## Setting

* You have a git repository on your local machine and you have a server
* SSH connection is set up

## Goal
Commit and push any changes made locally to your server

## Solution

Setup a github hook for deployment:
> https://www.youtube.com/watch?v=H6UU7TsyrGs
> 
> https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa. 

### Post-receive hook

```bash
#!/bin/bash
TARGET="/home/cloudsigma/deploy"
GIT_DIR="/home/cloudsigma/deploy-github-hook.git"
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
