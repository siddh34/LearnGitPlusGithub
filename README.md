# LearnGitPlusGithub

Learn Git + Github

Hope you have downloaded git from [link](https://git-scm.com/downloads)

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

# Branching out in this repo after clone

```bash
git checkout -b branch_name

# it is important to take pull from main whenever possible

git pull origin main
```
