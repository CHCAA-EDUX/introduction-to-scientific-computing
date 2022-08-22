# Exercises 1 #

## File manipulation ##

In order for us to be better able to help you solve your problems remotely, we prefer that you have your files in order. So let’s organise a bit:

1. Go to the course Moodle page and download the 'Data' directory to your computer.
2. Identify the file path to your Downloads folder (either in Jupyter or your file browser)
3. Choose a location and create a new folder you call ex, "python_course" – any new materials for this course should go in here. (NOTE: In Python, variable names cannot contain spaces, and special characters other than underscore ( _ ) can be interpreted in unexpected ways, so it is better to avoid those characters to begin with!)
4. Unzip the downloaded file into the new folder (or cut-paste from Downloads folder and unzip in place).

To unzip with python use the following code
```py
import zipfile

with zipfile.ZipFile("<path_to_zip_file>", 'r') as zip_ref:
    zip_ref.extractall("<directory_to_extract_to>")
```

---

## Practice questions ##

1: Which of the following are operators, and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

---

2. Starting from `/Users/amanda/data`, which of the following commands could Amanda use to navigate to her home directory, which is `/Users/amanda`?

```sh
1. cd .
2. cd /
3. cd /home/amanda
4. cd ../..
5. cd ~
6. cd home
7. cd ~/data/..
8. cd
9. cd ..
```

---

3. Using the filesystem diagram below, if pwd displays /Users/thing, what will ls -F ../backup display?

1. `../backup: No such file or directory`
2. `2012-12-01 2013-01-08 2013-01-27`
3. `2012-12-01/ 2013-01-08/ 2013-01-27/`
4. `original/ pnas_final/ pnas_sub/`


| <img src="https://raw.githubusercontent.com/CHCAA-EDUX/introduction-to-scientific-computing/66e4288437bb332dd9be489c25f0e963a9deeb96/lessons/figs/filesystem-challenge_1.svg" alt="fs-challenge-01" width="800"/> |
|:--:|
| *File System Challenge 01* |

---

4. Using the filesystem diagram below, if `pwd` displays `/Users/backup`, and `-r` tells `ls` to display things in reverse order, what command(s) will result in the following output:

```sh
pnas_sub/ pnas_final/ original/
```

| <img src="https://raw.githubusercontent.com/CHCAA-EDUX/introduction-to-scientific-computing/66e4288437bb332dd9be489c25f0e963a9deeb96/lessons/figs/filesystem-challenge_2.svg" alt="fs-challenge-02" width="800"/> |
|:--:|
| *File System Challenge 02* |

1. `ls pwd`
2. `ls -r -F`
3. `ls -r -F /Users/backup`

---
5. Instead of using an editor to create a file (Windows: `edit <filename>` or Linux: `Vim <filename>`), we can use the following command on Linux:

```sh
touch sample_file.txt
```

1. What did the `touch` command do? When you look at your current directory using the GUI file explorer, does the file show up?
2. Use `ls -l` to inspect the files. How large is `sample_file.txt`?
3. When might you want to create a file this way?

Windows does not have a direct equivalent, but we can use `copy` with a `+` at the end of the filename

```sh
copy sample_file.txt+
```
---