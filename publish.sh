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

git checkout master

# Nuke old gh-pages branch and recreate.
git branch -D gh-pages
git push origin :gh-pages
git checkout --orphan gh-pages

make html

# Move build into top level; nuke everything else.
mkdir tmp
mv ./* tmp
mv tmp/_build/html/* .
mv tmp/_static .
mv tmp/_sources .
rm -rf tmp/

# Tell jekyll to stop being stupid
touch .nojekyll

# Update the new branch.
git add .
git commit -am"Latest build"

git pull origin gh-pages
git push origin gh-pages

# Now go back to master.
git checkout master
