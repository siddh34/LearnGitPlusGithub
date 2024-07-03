# Task 2: git revert

* Switch to branch fix/doom
* Fix the branch

```txt
# Scenario the test where green sometime before but now they are red can you revert to the second last commit
```

Steps

* See commit id using `git log`

![1719990613294](image/2-revert/1719990613294.png)

* Revert to last second commit using `git revert --hard commit id`
  * Commit id is infront of commit as you can see in first image
* Then force commit to the branch `git commit -f "revert"`
* Enter `git pull --rebase=false`
* Take pull and commit again
* If conflict is there then use `git status & `git add file.ext``
* Then commit again
* Check the main branch readme should be updated
