{{#title Run s&box Server (Proton)}}
# Run the Server (Proton)

1. Follow [the guide for running the game with Proton](../../game/run/proton.md) normally at least once so that the s&box Proton prefix is available

2. Install [protontricks](https://github.com/matoking/protontricks#installation)

> [!CAUTION]
> `protontricks.com` is not affiliated with any of the Protontricks developers. Download only from the `protontricks` Github repo.

3. Install [steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD) so that you can install the official prebuilt s&box dedicated server

4. Use steamcmd to install the official prebuilt s&box dedicated server (Windows version). Adjust the `~/sbox-server-proton` path to where you want the server to be placed:
```sh
steamcmd +@sSteamCmdForcePlatformType windows +force_install_dir ~/sbox-server-proton +login anonymous +app_update 1892930 validate +quit
```
>[!WARNING]
>Relative paths passed to `steamcmd` may not be relative to your current working directory depending on how you install/run `steamcmd`.

5. Navigate to the s&box dedicated server directory you just installed:
```sh
cd ~/sbox-server-proton
```
6. Launch the server using `protontricks-launch`, passing your arguments like normal. Example:
```sh
protontricks-launch --appid 590830 ./sbox-server.exe +game facepunch.sandbox facepunch.flatgrass +hostname "My Dedicated Server"
```
Reference the table at the bottom of <https://sbox.game/dev/doc/networking/dedicated-servers/> for the available arguments.