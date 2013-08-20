git checkout master

# Nuke old gh-pages branch and recreate.
git branch -D gh-pages
git checkout --orphan gh-pages

make html

# Move build into top level; nuke everything else.
mkdir tmp
mv ./* tmp
mv tmp/_build/html/* .
rm -rf tmp/

# Update the new branch.
git add .
git commit -am"Latest build"

git pull origin gh-pages
git push origin gh-pages

# Now go back to master.
git checkout master
