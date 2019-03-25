Using this repo to test git merge and rebase.

Created initial commit with hello.py
```Python
def greet():
  print("hello")

if __name__ == '__main__':
  greet()
```

Creating branch `change-greet`, 
´´´
git checkout -b change-greet # create branch + checkout
´´´
changing `greet()` in *hello.py* to use `hi` instead of `hello`.

I then mande another branch from master adding a name variable
to `greet()`:
´´´
git checkout master
git checkout -b add-greet
´´´
with the following changes:
```Python
def greet(name):
+  print("hello", name)

if __name__ == '__main__':
  greet("Jorgen")
```

Current Tree:
```
git log --graph --decorate --oneline --all
  OUTPUT: 
    * 3d403c9 (add-name) Added name to hello.py
    | * 910cc6f (change-greet) Modified hello.py: hello to hi
    |/  
    * 8680edd (HEAD -> master) added hello.py
```


```
git rebase --onto master add-name 
# ...Nothing seemed to happen (master still at commit: 8680edd)

# Trying again:
git rebase --onto add-name change-greet 

git log --graph --decorate --oneline --all
  OUTPUT: 
    * 3d403c9 (HEAD -> master, add-name)   Added name to hello.py
    | * 910cc6f (change-greet)   Modified hello.py: hello to hi
    |/  
    * 8680edd   added hello.py
```

```
git rebase --onto master change-greet add-name 
# ... Don't think this worked... (maybe I fed branches in wrong order)
# Trying again (using other commands):
git checkout change-greet
git rebase master
```
Then I fixed merge conflicts and entered:
```
# Current tree
* 3d403c9 (HEAD, master, add-name) Added name to hello.py
| * 910cc6f (change-greet) Modified hello.py: hello to hi
|/  
* 8680edd added hello.py
```
git rebase --continue
```

```
# Current Tree :
* c409fc4 (HEAD -> change-greet) Modified hello.py: hello to hi
* 3d403c9 (master, add-name) Added name to hello.py
* 8680edd added hello.py
```

```
# Remove branches and update master
git checkout master
git merge change-greet
git branch -d add-name 
git branch -d change-greet
```

```
# Final Tree:
* c409fc4 (HEAD -> master) Modified hello.py: hello to hi
* 3d403c9 Added name to hello.py
* 8680edd added hello.py
```


Continue To Write about git squash...
-------------------------------------
use this .md file with all it's commits and squash them down to a single commit!!
