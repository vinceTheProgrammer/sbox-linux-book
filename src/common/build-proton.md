# Build the Game, Editor, and Server (Proton)

The Proton verison of the game, editor, and server can be built in the following ways:

## sbox-win-docker

The tool, by [vinceTheProgrammer](https://github.com/vinceTheProgrammer), `sbox-wine-docker`, simplifies the build process. It is meant to act as single command that can be used to build any instance of the `sbox-public` repo without needing to configure your build environment beyond installing Docker. The following steps can be used to build s&box from source using `sbox-wine-docker`:

1. Ensure Docker is installed.
2. Install `sbox-wine-docker`:
```sh
sudo curl -L https://raw.githubusercontent.com/vinceTheProgrammer/sbox-wine-docker/refs/heads/main/sbox-build -o /usr/local/bin/sbox-build
sudo chmod +x /usr/local/bin/sbox-build
```
You should now have the `sbox-build` command.

3. Clone the s&box source code:
```sh
git clone https://github.com/Facepunch/sbox-public.git
```
or any fork, provided it has the same structure as the official `sbox-public` repo.

4. Navigate into the source code repo:
```sh
cd sbox-public
```

5. Run `sbox-build` and follow its prompts.

6. Run `sbox-build` again, whenever you need to rebuild after making changes.

## Manually

{{#include stub.md}}