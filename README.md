import to eccube

python(3.6.0)

## pyenv
    $ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    $ cat << EOF >> ~/.bash_profile
    export PYENV_ROOT="\$HOME/.pyenv"
    export PATH="\$PYENV_ROOT/bin:\$PATH"
    eval "\$(pyenv init -)"
    EOF
    $ source ~/.bash_profile

## conda
    url: https://www.continuum.io/downloads#linux
### linux(x86_64)
    $ curl -O https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
    bash Anaconda3-4.3.0-Linux-x86_64.sh
    ...
    cd ~/anaconda3/env/
    conda create -n project_name python=3.6
    cd project_name
    source activate project_name
    (project_name) $
