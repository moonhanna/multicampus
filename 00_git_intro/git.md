```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL
$ git init
Initialized empty Git repository in C:/Users/user/TIL/.git/

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ ls
00_git_intro

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ ls -a
.  ..  .git  00_git_intro

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        00_git_intro/

nothing added to commit but untracked files present (use "git add" to track)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add 00_git_intro/

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   00_git_intro/git-basic.md
        new file:   00_git_intro/images/github_image.jpg
        new file:   00_git_intro/markdown-prac.md


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "first commit"
[master (root-commit) fdbac65] first commit
 3 files changed, 177 insertions(+)
 create mode 100644 00_git_intro/git-basic.md
 create mode 100644 00_git_intro/images/github_image.jpg
 create mode 100644 00_git_intro/markdown-prac.md

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log
commit fdbac65ce2962aacae81ca1d9270d844bb739df3 (HEAD -> master)
Author: moonhanna <mhn97@naver.com>
Date:   Mon Dec 9 17:36:06 2019 +0900

    first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote add origin https://github.com/moonhanna/TIL.git

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote -v
origin  https://github.com/moonhanna/TIL.git (fetch)
origin  https://github.com/moonhanna/TIL.git (push)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 60.91 KiB | 5.54 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0)
To https://github.com/moonhanna/TIL.git
 * [new branch]      master -> master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```



### 깃 로그 확인방법

```bash
$ git log
commit b21da0519db8436a3c70f96765fdff87b3fded81 (HEAD -> master)
Author: moonhanna <mhn97@naver.com>
Date:   Tue Dec 10 10:21:08 2019 +0900

    added git.md file

commit fdbac65ce2962aacae81ca1d9270d844bb739df3 (origin/master)
Author: moonhanna <mhn97@naver.com>
Date:   Mon Dec 9 17:36:06 2019 +0900

    first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --pretty=oneline
b21da0519db8436a3c70f96765fdff87b3fded81 (HEAD -> master) added git.md file
fdbac65ce2962aacae81ca1d9270d844bb739df3 (origin/master) first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
b21da05 (HEAD -> master) added git.md file
fdbac65 (origin/master) first commit
```



### 깃헙 레파지토리 추가

```bash

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote rename origin moon

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote -v
moon    https://github.com/moonhanna/TIL.git (fetch)
moon    https://github.com/moonhanna/TIL.git (push) 

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote rename moon origin

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git remote -v
origin  https://github.com/moonhanna/TIL.git (fetch)
origin  https://github.com/moonhanna/TIL.git (push) 

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```



### 커밋 되돌리기

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ ls
00_git_intro  README.md

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ ls -a
.  ..  .git  .gitignore  00_git_intro  README.md

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ mkdir 01_git_reset

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ cd 01_git_reset/

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/01_git_reset (master)
$ touch reset.txt reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/01_git_reset (master)
$ ls
reset.txt  reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/01_git_reset (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/01_git_reset (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   reset.txt
        new file:   reset2.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/01_git_reset (master)
$ cd ../

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   01_git_reset/reset.txt
        new file:   01_git_reset/reset2.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git reset HEAD 01_git_reset/reset.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   01_git_reset/reset2.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01_git_reset/reset.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git rm --cached 01_git_reset/reset2.txt 
rm '01_git_reset/reset2.txt'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01_git_reset/

nothing added to commit but untracked files present (use "git add" to track)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   01_git_reset/reset.txt
        new file:   01_git_reset/reset2.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "Added reset.txt and reset2.txt"
[master d15094d] Added reset.txt and reset2.txt
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 01_git_reset/reset.txt
 create mode 100644 01_git_reset/reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   01_git_reset/reset.txt
        modified:   01_git_reset/reset2.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git reset HEAD 01_git_reset/reset.txt
Unstaged changes after reset:
M       01_git_reset/reset.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git rm --cached 01_git_reset/reset2.txt 
rm '01_git_reset/reset2.txt'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    01_git_reset/reset2.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   01_git_reset/reset.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01_git_reset/reset2.txt

.gitignore 파일에 reset2.txt 내용 추가
그러면 깃이 관리x

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    01_git_reset/reset2.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   01_git_reset/reset.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```



### 커밋 메시지 고치기

```bash

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add 01_git_reset/reset.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "added reset.txt file"
added reset.txt files
[master 21c4f3e] added reset.txt file
 2 files changed, 1 insertion(+)
 delete mode 100644 01_git_reset/reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
21c4f3e (HEAD -> master) added reset.txt file
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit --amend
[master fad53b9] added reset.txt file
 Date: Tue Dec 10 15:23:35 2019 +0900
 2 files changed, 1 insertion(+)
 delete mode 100644 01_git_reset/reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit --amend
[master 66ec630] added reset.txt files
 Date: Tue Dec 10 15:23:35 2019 +0900
 2 files changed, 1 insertion(+)
 delete mode 100644 01_git_reset/reset2.txt
added reset.txt file

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
66ec630 (HEAD -> master) added reset.txt files
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit --amend
[master bcaed59] added reset.txt file
 Date: Tue Dec 10 15:23:35 2019 +0900
 2 files changed, 1 insertion(+)
 delete mode 100644 01_git_reset/reset2.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
bcaed59 (HEAD -> master) added reset.txt file
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
```



### 파일 추가 + 메시지 고치기 

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ touch 01_git_reset/omit_file.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add 01_git_reset/omit_file.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit --amend
[master 30216d9] added reset.txt and omit_file.txt files
 Date: Tue Dec 10 15:23:35 2019 +0900
 2 files changed, 1 insertion(+)
 rename 01_git_reset/{reset2.txt => omit_file.txt} (100%)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
30216d9 (HEAD -> master) added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "updated .gitignore"
[master 452364e] updated .gitignore
 1 file changed, 2 insertions(+)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```



### branch

> branch 생성 및 삭제, 이동방법

```bash

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ mkdir 02_git_branch

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch feature/test

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch
  feature/test
* master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout feature/test 
Switched to branch 'feature/test'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/test)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch --d feature/test 
Deleted branch feature/test (was 452364e).

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch
* master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout -b feature/test
Switched to a new branch 'feature/test'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/test)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch --d feature/test 
Deleted branch feature/test (was 452364e).
```



> merge
>
> > 브랜치만 고쳐서 커밋 후 마스터에서 머지 -> 충돌안남
> >
> > 브랜치가 마스터브랜치를 앞질러서 머지됨

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/test)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout feature/test 
Switched to branch 'feature/test'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/test)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git merge feature/test 
Updating 452364e..e573c59
Fast-forward
 02_git_branch/merge-test.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 02_git_branch/merge-test.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
e573c59 (HEAD -> master, feature/test) added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch --d feature/test 
Deleted branch feature/test (was e573c59).

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch

* master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
e573c59 (HEAD -> master) added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 (origin/master) added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit
```

> merge commit
>
> > 각각 다른 부분을 수정해서 커밋해줬기 때문에 충돌나지 않고 머지가능

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout -b feature/signup
Switched to a new branch 'feature/signup'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ touch 02_git_branch/signup.html

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git log --oneline
1d615b5 (HEAD -> feature/signup, origin/master, master) Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ commit -m "Complete sugnup.html"
bash: commit: command not found

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git commit -m "Complete sugnup.html"
[feature/signup 85bbf91] Complete sugnup.html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 02_git_branch/signup.html

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git log --oneline
85bbf91 (HEAD -> feature/signup) Complete sugnup.html
1d615b5 (origin/master, master) Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout feature/signup 
Switched to branch 'feature/signup'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   02_git_branch/merge-test.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "updated merge-test.txt file"
[master c3e0c45] updated merge-test.txt file
 1 file changed, 2 insertions(+), 1 deletion(-)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
c3e0c45 (HEAD -> master) updated merge-test.txt file
1d615b5 (origin/master) Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout feature/signup 
Switched to branch 'feature/signup'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git log --oneline
85bbf91 (HEAD -> feature/signup) Complete sugnup.html
1d615b5 (origin/master) Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git merge feature/signup 
Merge made by the 'recursive' strategy.
 02_git_branch/signup.html | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 02_git_branch/signup.html

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
db45cee (HEAD -> master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 (feature/signup) Complete sugnup.html
1d615b5 (origin/master) Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   db45cee (HEAD -> master) Merge branch 'feature/signup'
|\
| * 85bbf91 (feature/signup) Complete sugnup.html
* | c3e0c45 updated merge-test.txt file
|/
* 1d615b5 (origin/master) Complete test.html
* e573c59 added merge-test.txt
* 452364e updated .gitignore
* 30216d9 added reset.txt and omit_file.txt files
* d15094d Added reset.txt and reset2.txt
* 460f617 added README.md
* 255d484 added .gitignore file
* b21da05 added git.md file
* fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch --d feature/signup 
Deleted branch feature/signup (was 85bbf91).

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   db45cee (HEAD -> master) Merge branch 'feature/signup'
|\
| * 85bbf91 Complete sugnup.html
* | c3e0c45 updated merge-test.txt file
|/
* 1d615b5 (origin/master) Complete test.html
* e573c59 added merge-test.txt
* 452364e updated .gitignore
* 30216d9 added reset.txt and omit_file.txt files
* d15094d Added reset.txt and reset2.txt
* 460f617 added README.md
* 255d484 added .gitignore file
* b21da05 added git.md file
* fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```

> merge complete
>
> > 다른 브랜치에서 같은 라인 수정 후 마스터브랜치에서 머지 -> 충돌 
> >
> > (내가 선택해서 머지해줘야함) 

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout -b feature/board
Switched to a new branch 'feature/board'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git status
On branch feature/board
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   02_git_branch/merge-test.txt

no changes added to commit (use "git add" and/or "git commit -a")

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git commit -m "update merge merge-test.txt file"
[feature/board 1b37c58] update merge merge-test.txt file
 1 file changed, 1 insertion(+), 1 deletion(-)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git log --oneline
1b37c58 (HEAD -> feature/board) update merge merge-test.txt file
db45cee (origin/master, master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 Complete sugnup.html
1d615b5 Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
db45cee (HEAD -> master, origin/master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 Complete sugnup.html
1d615b5 Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   02_git_branch/merge-test.txt

no changes added to commit (use "git add" and/or "git commit -a")

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "update merge-test.txt file python!!! -> ~~~"
git commit -m "update merge-test.txt file pythongit add .! -> ~~~"
[master 8219012] update merge-test.txt file pythongit add .! -> ~~~
 1 file changed, 1 insertion(+), 1 deletion(-)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
8219012 (HEAD -> master) update merge-test.txt file pythongit add .! -> ~~~
db45cee (origin/master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 Complete sugnup.html
1d615b5 Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git checkout feature/board
Switched to branch 'feature/board'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git log --oneline
1b37c58 (HEAD -> feature/board) update merge merge-test.txt file
db45cee (origin/master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 Complete sugnup.html
1d615b5 Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (feature/board)
$ git checkout master
Switched to branch 'master'

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git merge feature/board
Auto-merging 02_git_branch/merge-test.txt
CONFLICT (content): Merge conflict in 02_git_branch/merge-test.txt
Automatic merge failed; fix conflicts and then commit the result.

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   02_git_branch/merge-test.txt

no changes added to commit (use "git add" and/or "git commit -a")

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master|MERGING)
$ git add .

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master|MERGING)
$ git commit -m "python ~~~ -> !!!"
git commit -m "python ~~~ -> git add .!"
[master f9914fa] python ~~~ -> git add .!

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline
f9914fa (HEAD -> master) python ~~~ -> git add .!
8219012 update merge-test.txt file pythongit add .! -> ~~~
1b37c58 (feature/board) update merge merge-test.txt file
db45cee (origin/master) Merge branch 'feature/signup'
c3e0c45 updated merge-test.txt file
85bbf91 Complete sugnup.html
1d615b5 Complete test.html
e573c59 added merge-test.txt
452364e updated .gitignore
30216d9 added reset.txt and omit_file.txt files
d15094d Added reset.txt and reset2.txt
460f617 added README.md
255d484 added .gitignore file
b21da05 added git.md file
fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   f9914fa (HEAD -> master) python ~~~ -> git add .!
|\
| * 1b37c58 (feature/board) update merge merge-test.txt file
* | 8219012 update merge-test.txt file pythongit add .! -> ~~~
|/  
*   db45cee (origin/master) Merge branch 'feature/signup'
|\
| * 85bbf91 Complete sugnup.html
* | c3e0c45 updated merge-test.txt file
|/
* 1d615b5 Complete test.html
* e573c59 added merge-test.txt
* 452364e updated .gitignore
* 30216d9 added reset.txt and omit_file.txt files
* d15094d Added reset.txt and reset2.txt
* 460f617 added README.md
* 255d484 added .gitignore file
* b21da05 added git.md file
* fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git branch --d feature/board 
Deleted branch feature/board (was 1b37c58).

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   f9914fa (HEAD -> master) python ~~~ -> git add .!
|\
| * 1b37c58 update merge merge-test.txt file
* | 8219012 update merge-test.txt file pythongit add .! -> ~~~
|/
*   db45cee (origin/master) Merge branch 'feature/signup'
|\  
| * 85bbf91 Complete sugnup.html
* | c3e0c45 updated merge-test.txt file
|/
* 1d615b5 Complete test.html
* e573c59 added merge-test.txt
* 452364e updated .gitignore
* 30216d9 added reset.txt and omit_file.txt files
* d15094d Added reset.txt and reset2.txt
* 460f617 added README.md
* 255d484 added .gitignore file
* b21da05 added git.md file
* fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (12/12), 1.10 KiB | 374.00 KiB/s, done.
Total 12 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/moonhanna/TIL.git
   db45cee..f9914fa  master -> master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   f9914fa (HEAD -> master, origin/master) python ~~~ -> git add .!
|\
| * 1b37c58 update merge merge-test.txt file
* | 8219012 update merge-test.txt file pythongit add .! -> ~~~
|/
*   db45cee Merge branch 'feature/signup'
|\
| * 85bbf91 Complete sugnup.html
* | c3e0c45 updated merge-test.txt file
|/
* 1d615b5 Complete test.html
* e573c59 added merge-test.txt
* 452364e updated .gitignore
* 30216d9 added reset.txt and omit_file.txt files
* d15094d Added reset.txt and reset2.txt
* 460f617 added README.md
* 255d484 added .gitignore file
* b21da05 added git.md file
* fdbac65 first commit

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```



### git stash

> 임시보관소

```bash
user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ mkdir 03_git_stash

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ cd 03_git_stash/

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL/03_git_stash (master)
$ cd ../

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ touch 03_git_stash/stash-test.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        03_git_stash/

nothing added to commit but untracked files present (use "git add" to track)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git add 03_git_stash/stash-test.txt 

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   03_git_stash/stash-test.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash
Saved working directory and index state WIP on master: f9914fa python ~~~ -> git add .!

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash list
stash@{0}: WIP on master: f9914fa python ~~~ -> git add .!

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash apply
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   03_git_stash/stash-test.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   03_git_stash/stash-test.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash drop
Dropped refs/stash@{0} (d00b0ddf33a1592298f2a22e1d4d65fabd910804)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash list

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   03_git_stash/stash-test.txt


user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash
Saved working directory and index state WIP on master: f9914fa python ~~~ -> git add .!

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash list
stash@{0}: WIP on master: f9914fa python ~~~ -> git add .!

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash pop
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   03_git_stash/stash-test.txt

Dropped refs/stash@{0} (16190bef3b070ce3f2907debbfd61a2f7b07ab39)

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git stash list

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git commit -m "added stash-test.txt file"
[master a5f6645] added stash-test.txt file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 03_git_stash/stash-test.txt

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 321 bytes | 321.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/moonhanna/TIL.git
   f9914fa..a5f6645  master -> master

user@LAPTOP-CRKLSAF8 MINGW64 ~/TIL (master)
$
```







