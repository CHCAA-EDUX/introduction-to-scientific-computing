# Exercises 1 #

## Pair programming ##

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

## Check your understanding ##

Which of the following are operators, and which are values?

```py
1. *
2. 'hello'
3. -88.8
4. -
5. /
6. +
7. 5
```

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

1. operator
2. value
3. value
4. operator
5. operator
6. operator
7. value

</details>


---

Starting from `/Users/amanda/data`, which of the following commands could Amanda use to navigate to her home directory, which is `/Users/amanda`?

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

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

1. No: . stands for the current directory.
2. No: / stands for the root directory.
3. No: Amanda’s home directory is /Users/amanda.
4. No: this command goes up two levels, i.e. ends in /Users.
5. Yes: ~ stands for the user’s home directory, in this case /Users/amanda.
6. No: this command would navigate into a directory home in the current directory if it exists.
7. Yes: unnecessarily complicated, but correct.
8. Yes: shortcut to go back to the user’s home directory.
9. Yes: goes up one level.

</details>

---

Using the filesystem diagram below, if pwd displays /Users/thing, what will ls -F ../backup display?

1. `../backup: No such file or directory`
2. `2012-12-01 2013-01-08 2013-01-27`
3. `2012-12-01/ 2013-01-08/ 2013-01-27/`
4. `original/ pnas_final/ pnas_sub/`


| <img src="https://raw.githubusercontent.com/CHCAA-EDUX/introduction-to-scientific-computing/66e4288437bb332dd9be489c25f0e963a9deeb96/lessons/figs/filesystem-challenge_1.svg" alt="fs-challenge-01" width="800"/> |
|:--:|
| *File System Challenge 01* |

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

1. No: there _is_ a directory `backup` in `/Users`.
2. No: this is the content of `Users/thing/backup`, but with `..`, we asked for one level further up.
3. No: see previous explanation.
4. Yes: `../backup/` refers to `/Users/backup/`.

</details>

---

Using the filesystem diagram below, if `pwd` displays `/Users/backup`, and `-r` tells `ls` to display things in reverse order, what command(s) will result in the following output:

```sh
pnas_sub/ pnas_final/ original/
```

| <img src="https://raw.githubusercontent.com/CHCAA-EDUX/introduction-to-scientific-computing/66e4288437bb332dd9be489c25f0e963a9deeb96/lessons/figs/filesystem-challenge_2.svg" alt="fs-challenge-02" width="800"/> |
|:--:|
| *File System Challenge 02* |

1. `ls pwd`
2. `ls -r -F`
3. `ls -r -F /Users/backup`

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

1. No: `pwd` is not the name of a directory.
2. Yes: `ls` without directory argument lists files and directories in the current directory.
3. Yes: uses the absolute path explicitly.

</details>

---

Instead of using an editor to create a file (Windows: `edit <filename>` or Linux: `Vim <filename>`), we can use the following command on Linux:

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

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

1. The `touch` command generates a new file called `sampe_file.txt` in your current directory. You can observe this newly generated file by typing ls at the command line prompt. `sample_file.txt` can also be viewed in your GUI file explorer.
2. When you inspect the file with ls `-l`, note that the size of `sample_file.txt` is 0 bytes. In other words, it contains no data. If you open `sample_file.txt` using your text editor it is blank.
3. Some programs do not generate output files themselves, but instead require that empty files have already been generated. When the program is run, it searches for an existing file to populate with its output. The `touch` command allows you to efficiently generate a blank text file to be used by such programs.

</details>

---

## Practice Questions ##

NA