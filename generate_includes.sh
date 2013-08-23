require_clean_work_tree () {
    # Update the index
    git update-index -q --ignore-submodules --refresh
    err=0

    # Disallow unstaged changes in the working tree
    if ! git diff-files --quiet --ignore-submodules --
    then
        echo >&2 "cannot $1: you have unstaged changes."
        git diff-files --name-status -r --ignore-submodules -- >&2
        err=1
    fi

    # Disallow uncommitted changes in the index
    if ! git diff-index --cached --quiet HEAD --ignore-submodules --
    then
        echo >&2 "cannot $1: your index contains uncommitted changes."
        git diff-index --cached --name-status -r --ignore-submodules HEAD -- >&2
        err=1
    fi

    if [ $err = 1 ]
    then
        echo >&2 "Please commit or stash them."
        exit 1
    fi
}

require_clean_work_tree

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
git commit includes/__init__.edited.py -m"updated __init__.py diff"

git reset _includes --hard