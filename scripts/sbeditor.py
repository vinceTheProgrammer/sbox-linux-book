#!/usr/bin/env python3
"""Set up .NET 10 and Wine configuration for s&box in its Proton prefix."""

import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

APP_ID = "2129370"
DOTNET_DOWNLOAD_PAGE = "https://dotnet.microsoft.com/en-us/download/dotnet/10.0"

# Candidate Steam root directories in order of preference
STEAM_ROOTS = [
    Path.home() / ".steam/steam",
    Path.home() / ".local/share/Steam",
    Path.home() / "snap/steam/common/.local/share/Steam",
    Path.home() / ".var/app/com.valvesoftware.Steam/.local/share/Steam",
]


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def install_protontricks():
    mgr = next((shutil.which(t) for t in ("pipx", "pip3", "pip") if shutil.which(t)), None)
    if not mgr:
        die("protontricks not found and no pip/pipx available to install it.\n"
            "Install manually: https://github.com/Matoking/protontricks")
    print(f"Installing protontricks via {Path(mgr).name}...")
    subprocess.run([mgr, "install", "protontricks"], check=True)
    if not shutil.which("protontricks"):
        die("protontricks installed but not on PATH — ensure ~/.local/bin is in PATH and re-run.")


def check_deps():
    if not shutil.which("wine"):
        die("'wine' is not installed or not in PATH")

    pt = shutil.which("protontricks")
    if not pt:
        answer = input("protontricks not found. Install it now? [y/N] ").strip().lower()
        if answer == "y":
            install_protontricks()
        else:
            die("protontricks is required — install it and re-run.")
        pt = shutil.which("protontricks")

    if pt and pt.startswith("/usr/bin"):
        print("warning: system-packaged protontricks detected (apt version is often outdated).")
        print("         Run: pipx install protontricks  to get a current version.")
        print()


def steam_library_paths():
    """Return all Steam library 'common' folders found on this machine."""
    roots = [r for r in STEAM_ROOTS if r.is_dir()]
    if not roots:
        die("Could not find a Steam installation. Checked:\n" +
            "\n".join(f"  {r}" for r in STEAM_ROOTS))

    libraries = set()
    for root in roots:
        vdf = root / "steamapps/libraryfolders.vdf"
        if vdf.is_file():
            for path in re.findall(r'"path"\s+"([^"]+)"', vdf.read_text()):
                common = Path(path) / "steamapps/common"
                if common.is_dir():
                    libraries.add(common)
        # Always include the root's own library even if vdf is missing/empty
        default = root / "steamapps/common"
        if default.is_dir():
            libraries.add(default)

    return libraries


def find_installer():
    for common in steam_library_paths():
        matches = sorted(common.glob("**/dotnet-runtime-10*-win-x64.exe"))
        if matches:
            return matches[0]
    return None


def main():
    check_deps()

    installer = find_installer()
    if installer is None:
        print("No .NET 10 Windows runtime installer found in any Steam library.")
        print(f"Download the Windows x64 runtime installer from:\n  {DOTNET_DOWNLOAD_PAGE}")
        print("Place it anywhere inside a Steam library folder and re-run.")
        sys.exit(1)

    print(f"Installer: {installer}")
    print(f"Configuring Proton prefix for s&box (App ID {APP_ID})...")

    quoted = shlex.quote(str(installer))
    wine_cmd = " && ".join([
        f"wine {quoted} /install /quiet /norestart",
        r"wine reg add 'HKEY_CURRENT_USER\Software\Wine\X11 Driver' /v Decorated /t REG_SZ /d N /f",
        r"wine reg add 'HKEY_CURRENT_USER\Control Panel\Desktop' /v FontSmoothing /t REG_SZ /d 2 /f",
        r"wine reg add 'HKEY_CURRENT_USER\Control Panel\Desktop' /v FontSmoothingType /t REG_DWORD /d 2 /f",
        r"wine reg add 'HKCU\Software\Wine\DllOverrides' /v comdlg32 /d native /f",
    ])

    env = {**os.environ, "STEAM_RUNTIME": "0"}
    result = subprocess.run(["protontricks", "-c", wine_cmd, APP_ID], stderr=subprocess.PIPE, text=True, env=env)
    if result.returncode != 0:
        if "Invalid file magic number" in (result.stderr or ""):
            die("protontricks failed: appinfo.vdf format not supported by this version.\n"
                "Upgrade with: pipx install protontricks")
        if result.stderr:
            print(result.stderr, file=sys.stderr, end="")
        die(f"protontricks exited with code {result.returncode}")

    print("Done.")


if __name__ == "__main__":
    main()
