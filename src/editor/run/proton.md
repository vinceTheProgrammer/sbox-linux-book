{{#title Run s&box Editor (Proton)}}
# Run the Editor (Proton)
1. Install s&box normally via Steam
2. .NET is not installed inside the editor's Proton prefix by default, so you will need to install it yourself or run this Python script, written by [Doctor Law](https://github.com/joshuascript), that installs it for you:
```py
{{#include ../../../scripts/sbeditor.py}}
```
3. Right click s&box editor in your library > Properties... > Compatibility > Check "Force the use of a specific Steam Play compatibility tool" > Select "Proton 11.0 (Beta)" or newer

![[Screenshot of s&box editor's Steam compatibility window with Proton 11 selected]](../../images/editor_compat_proton_11.png)

4. Add `PROTON_SET_GAME_DRIVE=0` environment variable to s&box editor's launch options

![[Screenshot of s&box editor's general window with recommended launch options]](../../images/editor_launch_opts_proton_11.png)

5. Run