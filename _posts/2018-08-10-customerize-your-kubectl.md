---
layout:     post
title:      Customerize your kubectl
subtitle:   Show message for specified context
date:       2019-08-10
author:     Keyun Shang
header-img: img/post-bg-mma-0.jpg
catalog: true
tags:
    - kubernetes
    - tips

---

Kubectl is a client tool for managing the kubernetes objects. You can management different kubernetes clusters by specifying different context with the command as below.

    kubectl config use-context myprod-ks

However, if you a bunch of clusters to manage for different purposes such as cluster for development, cluster for test or cluster for production, you may need a way to prevent from using wrong context.

My way is to show an alert for the specified context when running `kubectl` command.


## Steps

1. Create a directory as below.

    `mkdir ~/bin`

2. Create a shell script named `kubectl` as below and place it into the directory you just created.

```
cat > ~/bin/kubectl << EOF
#!/bin/sh

/usr/local/bin/kubectl "$@"

if [[ $(/usr/local/bin/kubectl config current-context) == *"prod"* ]]; then

  RED='\033[0;31m'
  NC='\033[0m' # No Color
  echo "------------------------------------------"
  echo  "You're using the ${RED} PROD ${NC} environment."
  echo "------------------------------------------"

fi
EOF
```

3. Make the script executable.

    `chmod +x ~/bin/kubectl`

4. Add the path of the kubectl shell script to `$PATH` enviroment varaible.

    `export PATH=~/bin:$PATH`



That's all! 

Now, if the current context of your kubectl configuration contains `prod` keyword, the following message will be shown when running any of the `kubectl` commands. 

    ------------------------------------------
    You're using the PROD  environment.
    ------------------------------------------







