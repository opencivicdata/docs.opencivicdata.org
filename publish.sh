git checkout master

# Nuke old gh-pages branch and recreate.
git branch -D gh-pages
git checkout --orphan gh-pages

make html

# Tell jekyll to stop being stupid
touch _build/.nojekyll

# Move build into top level; nuke everything else.
mkdir tmp
mv ./* tmp
mv tmp/_build/html/* .
mv tmp/_static .
mv tmp/_sources .
rm -rf tmp/

# Update the new branch.
git add .
git commit -am"Latest build"

git pull origin gh-pages
git push origin gh-pages

# Now go back to master.
git checkout master
