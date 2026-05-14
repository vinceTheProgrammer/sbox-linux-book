{{#title Run s&box Server (Native)}}
# Run the Server (Native)
As of now there are three ways of running the s&box dedicated server natively that are documented here: via docker, via Docker + Pelican, and manually.

## Docker
I will update this section with more useful information after doing more research, but here's the GitHub repo: <https://github.com/claudflare/sbox-server-native-linux>

## Pelican (with Docker)
I will update this section with more useful information after doing more research, but here's the GitHub repo: <https://github.com/FreshDoktor/sbox_egg>

## Manually

> [!CAUTION]
> THIS SECTION AS OF NOW LIKELY STILL LEADS TO A BROKEN SBOX SERVER. I AM STILL DOING RESEARCH.

> [!NOTE]
> Consider corroborating this information with Facepunch's official documentation page on dedicated servers: <https://sbox.game/dev/doc/networking/dedicated-servers/>

> [!TIP]
> If you have any problems with `steamcmd`, it should be noted that Valve wrote a "Known Issues" section on the SteamCMD wiki page that may be worth taking a look at.
-------------
1. Install `steamcmd` so that you can install the official prebuilt s&box dedicated server. SteamCMD wiki page with install instructions: <https://developer.valvesoftware.com/wiki/SteamCMD>

2. Use `steamcmd` to install the official prebuilt s&box dedicated server:
```sh
steamcmd +login anonymous +app_update 1892930 validate +quit
```

3. [Install anneal-casefold](../../common/install-anneal.md)

4. Navigate to the parent folder of where the official prebuilt s&box dedicated server was installed:
```sh
cd ~/.local/share/Steam/steamapps/common/"sbox dedicated server"/..
```

5. Use `anneal` command installed in step 3 to make "sbox dedicated server" a case insensitive directory:
```
anneal create "sbox dedicated server"
```

6. Navigate into "sbox dedicated server"
```sh
cd "sbox dedicated server"
```

7. Download prebuilt `libssl.so.3` and `libcrypto.so.3` (3.0.13) and make them executable:
```sh
curl -LO \
    https://github.com/vinceTheProgrammer/sbox-linux-book/releases/download/openssl-3.0.13-linux-x86_64/libssl.so.3 \
    -LO \
    https://github.com/vinceTheProgrammer/sbox-linux-book/releases/download/openssl-3.0.13-linux-x86_64/libcrypto.so.3

chmod +x libcrypto.so.3 libssl.so.3
```
OR
Alternatively, [build openssl 3.0.13 yourself](../../common/build-openssl.md) if the prebuilts don't work, or you don't trust them.

8. Add this line above the `dotnet` command within `./sbox-server.sh`:

```sh
LD_PRELOAD=libssl.so.3:libcrypto.so.3
```

9. Fix the `./sbox-server.sh` line endings with `sed`:
```sh
sed -i 's/\r$//' sbox-server.sh
```

10. Run the server using `./sbox-server.sh`, passing the relevant arguments like normal. Example:
```sh
./sbox-server.sh +game facepunch.sandbox facepunch.flatgrass +hostname "My Dedicated Server"
```

11. Reference the table at the bottom of <https://sbox.game/dev/doc/networking/dedicated-servers/> for the available arguments.

> [!CAUTION]
> THIS SECTION AS OF NOW LIKELY STILL LEADS TO A BROKEN SBOX SERVER. I AM STILL DOING RESEARCH.
