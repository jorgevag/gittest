git notes and useful links
--------------------------

### Before you begin: 

[Practical Introduction to Git](https://codeburst.io/git-good-a-practical-introduction-to-git-and-github-in-git-we-trust-f18fa263ec48)

[master, origin and origin/master](https://stackoverflow.com/questions/18137175/in-git-what-is-the-difference-between-origin-master-vs-origin-master)


### Print history tree
```
git log --decorate --graph --oneline --all
```

### Use rebase and squash:
* rebase adds current branch on top of specified branch
* commit merges specified branch INTO current branch
```
git checkout my-branch 
git rebase master
# alternatively use 'git rebase master my-branch' (which is shorthand for above two commands)

git checkout master
git merge --squash my-branch
# Resolve any conflicts
git commit -m "added all commits of my-branch squashed into a single commit, on top of master"
```

[More on git-rebase](https://git-scm.com/docs/git-rebase)

[Squashing Commits](https://stackoverflow.com/questions/5308816/how-to-use-git-merge-squash)




### Use cherry-pick to only select certain commits
Current tree:
```
* f747f8f (bugfix) Fixed Bug!
|
* 97c573c          Added print-statements for debugging
|
* 4140052 (master) Added bug to hello.py
|
* (...)
```

Do a cherry-pick:
```
git checkout master
git cherry-pick f747f8f  # doesn't include changes from '97c573c'
# Resolve conflicts if any
git add . && git commit -m "Bug fixed!"
```

Final master branch:
```
* f747f8f (master) Fixed Bug!
|
* 4140052          Added bug to hello.py
|
* (...)
```

Try yourself:
1. add bug (or typo) - commit to master
2. create *bugfix* branch
2. add some code over 1 or more commits (to bugfix) to simulate debugging
3. fix bug/typo - commit to bugfix
3. cherry-pick only the final commit from bugfix-branch containing bugfix


### git reset
use git reset to jump back to an earlier commit to start over.

Continuing from the same tree from cherry-picking
Current tree:
```
* f747f8f (master) Fixed Bug!
|
* 4140052          Added bug to hello.py
|
* (...)
```

```
git reset 4140052
git checkout -f 4140052 # -f to remove local changes (or maybe just use 'git reset --hard')
```

### git revert 
Use git revert to remove commits.

`git revert` allows you to remove changes in specific commits. 
The changes (by removing commits) are included as a new commit. This allows to change


### Additional notes
* git checkout doesn't necessarily remove local changes
  when you change branch/commit. Use ´git checkout -f [branch/commit]´ to get the
  commit clean and as it is supposed to be.
  More on this behaviour on [Stackoverflow](https://stackoverflow.com/questions/25939329/why-are-unstaged-changes-still-present-after-checking-out-a-different-branch)
