# **Cheatsheet for GitHub**

## What is GitHub?
**GitHub** is a _version control system_. Simply put, the Google Drive for Coders keeps track of different versions of your files.

## What is a repository in GitHub?
A **repository** is essentially a folder in which you keep all the folders and files relevant to that folder's use. For example, if you're using the folder for a specific project, you should only keep the files and folders relevant to that project.

## Merge Conflicts
A **merge conflict** happens when we try to synchronize changes between the files on GitHub and our local machine but `git` there are some changes that are conflicting in both versions, for example, on our local file a variable `a` might be defined as `a = "apple"` but on GitHub, someone else (or we) might have changed its definition to `a = "arnold"`.

## Branching
- when we are working on something new, such as a new feature, which might break our (currently) working code, to avoid that we create a new __branch__ in which we would write the new code, for a new feature or whatever it is. And, if we feel that the new code works, we can just **merge the branches**, merging the old and new code. Otherwise, we can **switch back to the branch** with the old working code, which was working. This process is called **branching**.
- The default branch which GitHub makes and puts on is '**main**'. It used to be called '**master**' a few years back.
- A visual example of branching is:
```
o---o---o---o---o  (main)
             \
              o---o  (feature)
```

## GitHub Commands
```sh
git clone <url>
```
- this is used to download (clone) a repository from GitHub to our computer
- we can also specify the name of the folder in which we want the repository to be cloned by typing it in double quotes after the URL
---
```sh
git add <filename>
```
- with this command, we can tell git to track the files or folders specified. Git will remember the files or folders and save only those that you added when you commit the changes.
- we can also use a period (.) instead of the file name to add the whole directory in which we are while doing that
---
```sh
git commmit -m "<message>"
```
- this command saves a snapshot, like a screenshot of the files we added with `git add`, which we can (if needed) revert to later
- the message field is a place to add a short description of the commit
---
```sh
git status
```
- this command reports the status of our code, like, if it's committed or not, added or not, or the status of our local code with the code on GitHub
---
```sh
git push
```
- like we have to turn on the Google Drive application on Windows to sync the files with Google Drive, we also have to use this command to sync the commits with GitHub
---
```sh
git pull
```
- opposite of git push; we can download the latest changes from our files on GitHub to sync
---
```sh
git log
```
- if we ever want to see all the things we did to this repository, like what we added, committed, pushed, and pulled, then we just have to run this command, and git will tell us everything we (or anyone) did to this repository (because it keeps a log of what we do!)
---
```sh
git reset --hard <commit hash>
``` 
or 
```sh
git reset --hard <branch name, e.g. 'origin/main'>
```
- the main advantage of it is that we can save different versions of the same files or folders and then later revert to any one of them if we wish, and this command gives us one way to do that
- the ```--hard``` flag tells GitHub that we completely want to revert to that change by resetting all the current files
---
```sh
git branch
```
- lists all the branches in the repository
- indicates the branch we are on right now by showing an asterisk (*) beside its name
---
```sh
git checkout <branch name>
```
- we can **checkout**, __shift the branch we are (working) on__, to a branch with this command. The command to create a branch and shift on it is:
```sh
git checkout -b <branch name>
```
---
