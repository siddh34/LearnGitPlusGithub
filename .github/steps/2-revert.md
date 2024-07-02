# Task 2: git revert

* Switch to branch fix/doom
* Fix the branch

```txt
# Scenario the test where green sometime before but now they are red can you revert to the second last commit
```

Steps

* See commit id using `git log`
* Revert to last second commit using `git revert --hard commit id`
* Then commit to the branch
