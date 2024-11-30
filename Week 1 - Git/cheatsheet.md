# **Cheatsheet for GitHub**

## What is GitHub?
**GitHub** is a _version control system_. In simple words, it's the Google Drive for Coders which keeps track of different versions of your files.

## What is a repository in GitHub?
A **repository** is essentially a folder in which you keep all the folders and files relevant to that folder's use. Like if you're using the folder for a specific project, you should only keep the files and folders relevant to that project.

## GitHub Commands
```git clone <url>```
- this us used to download (clone) a repository from GitHub to our computer
- we can also specify the name of the folder in which we want the repository to be cloned by typing it in double quotes after the URL

```git add <filename>```
- with this command, we can tell git to track the files or folders specified. Git will remember the files or folders and save only those which you added when you commit the changes.
- we can also use a period (.) instead of the file name to add the whole directory in which we are while doing that

```git commmit -m "<message>"```
- this command saves a snapshot, like screen shot of the files we addded with `git add`, which we can (if needed) revert back to later
- the message feild is a place to add a short description of the commit

```git status```
- this command reports the status of our code, like, if it's commited or not, added or not, or the status of our local code with the code on GitHub

```git push```
- like we have to turn on the Google Drive application on Windows to sync the files with Google Drive, we also have to use thi command to sync the commmits with GitHub

```git pull```
- opposite of git push; we can download the latest changes from our files on GitHub to sync