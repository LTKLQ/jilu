# git 基本指令

始化：git init
关联远程仓库：git remote add origin （地址）
合并节点：git reset --hard origin/master
强制拉取：git fetch --all
提交所有的变化：git add -A
将本地仓库修改的内容添加到缓存区：git commit -m“注释”
将缓存区的内容推到远程仓库：git push origin master

# python

1.我的第一个程序

a, b = 0, 1
while b < 10 
	print(b,end=',')
	a, b = b, a+b