## A git repo for all of my work + projects in university

<details>
  <summary><b>To download a single file:</b></summary>

1. View the RAW version of a file
2. Refresh page to get the latest valid token
3. Use wget to pull the file

 ```bash
 wget "google.com" -o README.md
 ```

</details>

<details> 
  <summary><b>To link only a part of the repo:</b></summary>

[StackOverflow link][1]

```bash
git init <repo>
cd <repo>
git remote add -f origin <url>

git config core.sparseCheckout true

echo "some/dir/" >> .git/info/sparse-checkout
echo "another/sub/tree" >> .git/info/sparse-checkout
```
</details>


[1]: http://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/13738951#13738951
