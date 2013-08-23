
# Temporarily copy in the skeleton/example files
# from pupa, then commit the tutorial's changes over
# top fo them and output a diff to include in the
# tutorial.

mkdir _includes

cp ../pupa/example/__init__.py _includes/
initfile="_includes/__init__.py"
git add $initfile
git commit $initfile -m"skeleton __init__.py"

cp albuquerque/__init__.py _includes/
git diff $initfile > includes/__init__.edited.py

rm -rf _includes