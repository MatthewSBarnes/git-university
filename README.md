## A git repo for all of my work + projects in university

#### To download a single file:
1. View the RAW version of a file
2. Refresh page to get the latest valid token
3. Use wget to pull the file

 ```bash
 wget "google.com" -o README.md
 ```

#### To link only a part of the repo
[askubuntu link][1]
[1]: http://askubuntu.com/questions/460885/how-to-clone-git-repository-only-some-directories

```bash
git init <repo>
cd <repo>
git remote add -f origin <url>

git config core.sparseCheckout true

echo "some/dir/" >> .git/info/sparse-checkout
echo "another/sub/tree" >> .git/info/sparse-checkout
```
