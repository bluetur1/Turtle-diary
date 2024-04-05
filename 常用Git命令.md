# 常用 Git 命令

```
　　Git基本常用命令如下：
　　mkdir：         XX (创建一个空目录 XX指目录名)
　　pwd：          显示当前目录的路径。
　　git init          把当前的目录变成可以管理的git仓库，生成隐藏.git文件。
　　git add XX       把xx文件添加到暂存区去。
　　git commit –m “XX”  提交文件 –m 后面的是注释。
　　git status        查看仓库状态
　　git diff  XX      查看XX文件修改了那些内容
　　git log          查看历史记录
　　git reset  --hard HEAD^ 或者 git reset  --hard HEAD~ 回退到上一个版本
　　(如果想回退到100个版本，使用git reset –hard HEAD~100 )
　　cat XX         查看XX文件内容
　　git reflog       查看历史记录的版本号id
　　git checkout -- XX  把XX文件在工作区的修改全部撤销。
　　git rm XX          删除XX文件
　　git remote add origin GitHub - tugenhua0707/testgit 关联一个远程库
　　git push –u(第一次要用-u 以后不需要) origin master 把当前master分支推送到远程库
　　git clone GitHub - tugenhua0707/testgit  从远程库中克隆
　　git checkout –b dev  创建dev分支 并切换到dev分支上
　　git branch  查看当前所有的分支
　　git checkout master 切换回master分支
　　git merge dev    在当前的分支上合并dev分支
　　git branch –d dev 删除dev分支
　　git branch name  创建分支
　　git stash 把当前的工作隐藏起来 等以后恢复现场后继续工作
　　git stash list 查看所有被隐藏的文件列表
　　git stash apply 恢复被隐藏的文件，但是内容不删除
　　git stash drop 删除文件
　　git stash pop 恢复文件的同时 也删除文件
　　git remote 查看远程库的信息
　　git remote –v 查看远程库的详细信息
　　git push origin master  Git会把master分支推送到远程库对应的远程分支上
```

## Git简介

* Git是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。 
* Git是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。 
* Git与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

## Git与SVN的区别
Git不仅仅是个版本控制系统，它也是个内容管理系统(CMS),工作管理系统等。
如果你是一个具有使用SVN背景的人，你需要做一定的思想转换，来适应Git提供的一些概念和特征。
Git 与 SVN 区别点：
1. Git是分布式的，SVN不是：这是Git和其它非分布式的版本控制系统，例如SVN，CVS等，最核心的区别。
2. Git把内容按元数据方式存储，而SVN是按文件：所有的资源控制系统都是把文件的元信息隐藏在一个类似.svn,.cvs等的文件夹里。
3. Git分支和SVN的分支不同：分支在SVN中一点不特别，就是版本库中的另外的一个目录。
4. Git没有一个全局的版本号，而SVN有：目前为止这是跟SVN相比GIT缺少的最大的一个特征。
5. Git的内容完整性要优于SVN：Git的内容存储使用的是SHA-1哈希算法。这能确保代码内容的完整性，确保在遇到磁盘故障和网络问题时降低对版本库的破坏。

经常使用 Git ，但是很多命令还是记不住。一般来说，日常使用只要记住就可以了。但要熟练掌握，恐怕要记住40~60个命令，所以整理了一份常用Git命令清单。



* Workspace：工作区
* Index / Stage：暂存区
* Repository：仓库区（或本地仓库）
* Remote：远程仓库

## 配置用户名和邮箱

```shell
$ git --version   # 查看git的版本信息
$ git config --global user.name   # 获取当前登录的用户
$ git config --global user.email  # 获取当前登录用户的邮箱
```
登录git
```shell
# 如果刚没有获取到用户配置，则只能拉取代码，不能修改  要是使用git，你要告诉git是谁在使用
$ git config --global user.name 'userName'    # 设置git账户，userName为你的git账号，
$ git config --global user.email 'email'
# 获取Git配置信息，执行以下命令：
$ git config –list
```
## 配置https和ssh推送时保存用户名和密码
```shell
# https提交保存用户名和密码
$ git config --global credential.helper store
# 生成公钥私钥，将公钥配置到GitHub，ssh提交就可以免输入用户名密码
# 三次回车即可生成 ssh key
$ ssh-keygen -t rsa
# 查看已生成的公钥
$ cat ~/.ssh/id_rsa.pub
```
## 推送到远程仓库正确流程
```shell
1. git init # 初始化仓库
2. git add .(文件name) # 添加文件到本地仓库
3. git commit -m "first commit" # 添加文件描述信息
4. git remote add origin 远程仓库地址 # 链接远程仓库，创建主分支
5. git pull origin master --allow-unrelated-histories # 把本地仓库的变化连接到远程仓库主分支
6. git push -u origin master # 把本地仓库的文件推送到远程仓库
```
## 一、新建本地仓库
```shell
# 创建一个文件夹
$ mkdir GitRepositories    # 创建文件夹GitRepositories
$ cd GitRepositories       # 切换到GitRepositories目录下
# 在当前目录新建一个Git代码库
$ git init
# 新建一个目录，将其初始化为Git代码库
$ git init [project-name]
# 下载一个项目和它的整个代码历史
$ git clone [url]
```
## 二、配置(全局和项目)
```shell
# Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。
# 显示当前的Git配置
$ git config --list
# 编辑Git配置文件
$ git config -e [--global]
# 设置提交代码时的用户信息
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
```
## 三、增加/删除文件
```shell
# 添加指定文件到暂存区
$ git add [file1][file2] ...
# 添加指定目录到暂存区，包括子目录
$ git add [dir]
# 添加当前目录的所有文件到暂存区
$ git add .
# 添加每个变化前，都会要求确认
# 对于同一个文件的多处变化，可以实现分次提交
$ git add -p
# 删除工作区文件，并且将这次删除放入暂存区
$ git rm [file1] [file2] ...
# 停止追踪指定文件，但该文件会保留在工作区
$ git rm --cached [file]
# 改名文件，并且将这个改名放入暂存区
$ git mv [file-original] [file-renamed]
```

## 四、代码提交
```shell
# 提交暂存区到仓库区
$ git commit -m [message]
# 提交暂存区的指定文件到仓库区
$ git commit [file1] [file2] ... -m [message]
# 提交工作区自上次commit之后的变化，直接到仓库区
$ git commit -a
# 提交时显示所有diff信息
$ git commit -v
# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
$ git commit --amend -m [message]
# 重做上一次commit，并包括指定文件的新变化
$ git commit --amend [file1] [file2] ...
```
## 五、分支
```shell
# 列出所有本地分支
$ git branch
# 列出所有远程分支
$ git branch -r
# 列出所有本地分支和远程分支
$ git branch -a
# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]
# 新建一个分支，并切换到该分支
$ git checkout -b [branch]
# 新建一个分支，指向指定commit
$ git branch [branch] [commit]
# 新建一个分支，与指定的远程分支建立追踪关系
$ git branch --track [branch] [remote-branch]
# 切换到指定分支，并更新工作区
$ git checkout [branch-name]
# 切换到上一个分支
$ git checkout -
# 建立追踪关系，在现有分支与指定的远程分支之间
$ git branch --set-upstream [branch] [remote-branch]
# 合并指定分支到当前分支
$ git merge [branch]
# 选择一个commit，合并进当前分支
$ git cherry-pick [commit]
# 删除分支
$ git branch -d [branch-name]
# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
```
## 六、标签
```shell
# 列出所有tag
$ git tag
# 新建一个tag在当前commit
$ git tag [tag]
# 新建一个tag在指定commit
$ git tag [tag] [commit]
# 删除本地tag
$ git tag -d [tag]
# 删除远程tag
$ git push origin :refs/tags/[tagName]
# 查看tag信息
$ git show [tag]
# 提交指定tag
$ git push [remote] [tag]
# 提交所有tag
$ git push [remote] --tags
# 新建一个分支，指向某个tag
$ git checkout -b [branch] [tag]
```
## 七、查看信息
```shell
# 查看目录
$ ls -al	或者$ ll
# 查看仓库状态，显示有变更的文件
$ git status
# 显示当前分支的版本历史
$ git log
# 显示commit历史，以及每次commit发生变更的文件
$ git log --stat
# 搜索提交历史，根据关键词
$ git log -S [keyword]
# 显示某个commit之后的所有变动，每个commit占据一行
$ git log [tag] HEAD --pretty=format:%s
# 显示某个commit之后的所有变动，其"提交说明"必须符合搜索条件
$ git log [tag] HEAD --grep feature
# 显示某个文件的版本历史，包括文件改名
$ git log --follow [file]
$ git whatchanged [file]
# 显示指定文件相关的每一次diff
$ git log -p [file]
# 显示过去5次提交
$ git log -5 --pretty --oneline
# 显示所有提交过的用户，按提交次数排序
$ git shortlog -sn
# 显示指定文件是什么人在什么时间修改过
$ git blame [file]
# 显示暂存区和工作区的差异
$ git diff
# 显示暂存区和上一个commit的差异
$ git diff --cached [file]
# 显示工作区与当前分支最新commit之间的差异
$ git diff HEAD
# 显示两次提交之间的差异
$ git diff [first-branch]...[second-branch]
# 显示今天你写了多少行代码
$ git diff --shortstat "@{0 day ago}"
# 显示某次提交的元数据和内容变化
$ git show [commit]
# 显示某次提交发生变化的文件
$ git show --name-only [commit]
# 显示某次提交时，某个文件的内容
$ git show [commit]:[filename]
# 显示当前分支的最近几次提交
$ git reflog
```
## 八、远程同步
```shell
# 下载远程仓库的所有变动
$ git fetch [remote]
# 显示所有远程仓库
$ git remote -v
# 显示某个远程仓库的信息
$ git remote show [remote]
# 增加一个新的远程仓库，并命名
$ git remote add [shortname] [url]
# 取回远程仓库的变化，并与本地分支合并
$ git pull [remote] [branch]
# 上传本地指定分支到远程仓库
$ git push [remote] [branch]
# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force
# 推送所有分支到远程仓库
$ git push [remote] --all
```
## 九、撤销
```shell
# 恢复暂存区的指定文件到工作区
$ git checkout [file]
# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]
# 恢复暂存区的所有文件到工作区
$ git checkout .
# 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
$ git reset [file]
# 重置暂存区与工作区，与上一次commit保持一致
$ git reset --hard
# 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
$ git reset [commit]
# 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
$ git reset --hard [commit]
# 重置当前HEAD为指定commit，但保持暂存区和工作区不变
$ git reset --keep [commit]
# 新建一个commit，用来撤销指定commit
# 后者的所有变化都将被前者抵消，并且应用到当前分支
$ git revert [commit]
# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop
```
## 十、其他
```shell
# 从当前目录的所有文件中查找文本内容：
$ git grep "Hello"
# 在某一版本中搜索文本：
$ git grep "Hello" v2.5
# 生成一个可供发布的压缩包
$ git archive
```
## 附：资料链接
[Git 常用命令总结](https://blog.csdn.net/tomatozaitian/article/details/73515849)
[Git常用命令，很全很详细讲解的也不错](https://blog.csdn.net/afei__/article/details/51476529)
[Git详细使用教程](https://blog.csdn.net/tgbus18990140382/article/details/52886786)
[Git使用详细教程](https://blog.csdn.net/youzhouliu/article/details/78952453)
[Git 安装和使用教程](http://www.cnblogs.com/smuxiaolei/p/7484678.html)
[Git 教程](https://www.w3cschool.cn/git/git-tutorial.html)