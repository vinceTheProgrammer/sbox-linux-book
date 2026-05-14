# Install anneal-casefold

Although you should read the `joshuascript/anneal-casefold` `README.md` for the most up to date instructions, instructions are provided here for convenience. You can install [joshuascript/anneal-casefold](https://github.com/joshuascript/anneal-casefold) via the following steps:

1. Ensure `git` is installed on your system: <https://git-scm.com/install/linux>

2. Ensure you have the `anneal-casefold` dependencies installed on your system:
- python3
- e2fsprogs >= 1.45
- losetup
- findmnt
```sh
python3 -V

# e2fsprogs
mkfs.ext4 -V
debugfs -V

losetup -V
findmnt -V
```

3. Navigate to some directory where you would like to keep the `anneal-casefold` git repo
```sh
cd <some directory that the repo directory will live within>
```

4. Clone the repo
```sh
git clone https://github.com/joshuascript/anneal-casefold.git
```

5. Navigate into the repo
```sh
cd anneal-casefold
```

6. Install the `anneal` command:
```sh
./install.sh
```

You should now have the `anneal` command.