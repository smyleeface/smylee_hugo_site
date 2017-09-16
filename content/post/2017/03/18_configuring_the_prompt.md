+++
title = "Configuring the Terminal Prompt"
date = "2017-03-18T17:00:00-08:00"
toc = false
draft = false
categories = ["Step-by-Step Guides"]
tags = ["OSX", "Terminal", "virtualenv", "git-aware-prompt"]
thumbnail = "/images/2017/03/before-git-aware-prompt.png"
+++

I was recommended this tool to help you know what git branch you are working on from the terminal prompt.

https://github.com/jimeh/git-aware-prompt

### Configurations

I added the configuration to my settings in:

`vi ~/.bash_profile`

```
# http://stackoverflow.com/questions/10406926/how-to-change-default-virtualenvwrapper-prompt

export GITAWAREPROMPT=~/.bash/git-aware-prompt
source "${GITAWAREPROMPT}/main.sh"
#/Users/patty/.virtualenvs/postactivate
export PS1="\n\u@\h\n[\w]\n\[$txtcyn\]\$git_branch\[$txtred\]\$git_dirty\[$txtrst\]\$ "
export SUDO_PS1="\n\[$bakred\]\u@\h\n\[$txtrst\][\w]\n\$ "
```

Then in virtualenvs postacivate I added:

`vi /Users/pattyr/.virtualenvs/postactivate`

```
# This hook is sourced after every virtualenv is activated
if [ "${_OLD_VIRTUAL_PS1:0:2}" == "\n" ]; then
    PS1="\n\[$txtylw\](`basename \"$VIRTUAL_ENV\"`)\n\[$txtrst\]${_OLD_VIRTUAL_PS1:2:${#_OLD_VIRTUAL_PS1}}"
fi
```

### Before
<img src="/images/2017/03/before-git-aware-prompt.png" alt="Before git-aware-prompt - with and without venv" title="Before git-aware-prompt - with and without venv">

### After
<img src="/images/2017/03/after-git-aware-prompt.png" alt="After git-aware-prompt - with and without venv" title="After git-aware-prompt - with and without venv">