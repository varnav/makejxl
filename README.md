# makejxl

This tool will bulk encode image files in given directory to [JPEG-XL](https://gitlab.com/wg1/jpeg-xl). JPEG-XL encoder is still under development.

## Supported input file formats:

 * .jpeg/.jpg
 * .exr
 * .gif
 * .pfm
 * .pgm/.ppm
 * .pgx
 * .png

Supports Windows, Linux, MacOS and probably other OSes.

## Linux

```sh
pip install makejxl
makejxl --recursive /home/username/myphotos
```

You will need cjxl in path. You can get it by running build_cjxl.sh as root

### Windows

You can download and use it as single Windows binary, see [Releases](https://github.com/varnav/makejxl/releases/)

Unfortunately antiviruses [don't like packed Python executables](https://github.com/pyinstaller/pyinstaller/issues?q=is%3Aissue+virus), so expect false positives from them if you go this way. Best way is pip.

You will need [cjxl](https://gitlab.com/wg1/jpeg-xl/-/blob/master/doc/developing_in_windows.md) in path. It's best to build it using [this tool](https://github.com/m-ab-s/media-autobuild_suite) and copy to `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps`

```cmd
./makejxl.exe "c:\\Users\\username\\Pictures\\My Vacation"
```

Remember, you need double slashes in Windows.

