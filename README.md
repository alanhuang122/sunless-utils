# sunless-utils
Utilities for serialization of Sunless Sea data.

Python 3.7 is required.

This codebase is largely based off [fl-utils](https://github.com/alanhuang122/fl-utils).

`convert.py` will take individual serialized data files and combine them into a single data file, in a usable format.

`init.py` loads the data file produced by `convert.py`.

`sunless.py` contains methods to format the data.

## How to use
Take the `*_import.json` files from the relevant directory (e.g., on Windows, `C:\Users\<username>\AppData\LocalLow\Failbetter Games\Sunless Sea\entities\`) and place them in a directory.

Inclusion of the `data/settings.json` file from the repository is highly encouraged. The information is not readily available in the game files.

Running `python convert.py` from the directory containing the JSON-serialized data will produce a file suitable for use with `init.py`.

Run `python -i init.py` from the directory containing the data file.

To format Storylets, Qualities, etc., ```print(sunless.Storylet.get(181040))``` or ```print(sunless.Quality.get(114086))```, for example.
