# LearnGitPlusGithub

Learn Git + Github

You can initialize local git repo by using `git init` command

Hope you have downloaded git from [link](https://git-scm.com/downloads)

Clone this repo `git clone` command

```bash
git clone https://github.com/PracticalEdges/LearnGitPlusGithub.git
```

## Configure git

```bash
git config --global user.name "Your Name"

git config --global user.email "you@example.com"
```

This will configure git on your local

You can either setup gpg or ssh for your git account for github

```bash
# For ssh the below works

git config --global gpg.format ssh

git config --global user.signingkey /PATH/TO/.SSH/KEY.PUB
```

```bash
# For gpg keys

git config --global --unset gpg.format

gpg --list-secret-keys --keyid-format=long

git config --global user.signingkey examplekey

git config --global commit.gpgsign true

```

But we will show you a fun way to login to github without this hasel. That will be at the end

## Branching out in this repo after clone

```bash
git checkout -b my_branch

# it is important to take pull from main whenever possible

git pull origin main
```

## Task 1

After branching out

* Correct the code located in fun.py
* Command to test code locally: `python -m unittest discover -s . -p "test_*.py"`
* Push the code using below command

```bash
# stage the file

git add .

# commit the changes locally

git commit -m "corrected code"

# push to branch

git push
```

* Go to github and check the PR section
* Click on `new pull request`
* Select your branch against main
* Click on create
