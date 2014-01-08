#!/bin/sh

#set -ue
set -e
#set -o pipefail

python setup.py check -r

echo ====================================================
echo Running tests

for PYVER in 2.6 2.7 3.1 3.2 3.3; do
	# Assume that virtualenv is installed $HOME/pyenv/ver
	source $HOME/pyenv/${PYVER}/bin/activate
	which python
	python -V
	python setup.py test
	deactivate
done

echo ====================================================

PKG_NAME=$(python setup.py --name)
VER=$(python setup.py --version)

/bin/echo ${PKG_NAME} version ${VER}
/bin/echo -n "Upload? [y/N] "
read answer

if [[ "$answer" =~ ^[y|Y]$ ]]; then
	python setup.py sdist upload
elif [[ "$answer" =~ ^[n|N]$ ]]; then
	echo "Bye."
else
	echo "Answer y or n"
fi

