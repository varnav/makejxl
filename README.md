# makejxl

This tool will bulk encode image files in given directory to [JPEG-XL](https://gitlab.com/wg1/jpeg-xl). It will leave original files intact, creating .jxl file next to each original.

JPEG-XL encoder is still under development, but format is frozen since 2020-12-24 and files encoded today will be readable by later versions of decoders.

**You don't need to use this tool at all. Examples for Shell and PowerShell scripts are below.**

## Supported input file formats:

 * .jpeg/.jpg (conversion is lossless and reversible)
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

Or simpler alternative that doesn't need this script:

```sh
apt install imagemagick parallel
find /path/to/images -type f -iregex '.*\(gif\|jpe?g\|png\)$' | parallel convert {} {.}.jxl
```

## Windows

You can download and use it as single Windows binary, see [Releases](https://github.com/varnav/makejxl/releases/)

Unfortunately antiviruses [don't like packed Python executables](https://github.com/pyinstaller/pyinstaller/issues?q=is%3Aissue+virus), so expect false positives from them if you go this way. Best way is pip.

You will need [cjxl](https://gitlab.com/wg1/jpeg-xl/-/blob/master/doc/developing_in_windows.md) in path. It's best to build it using [this tool](https://github.com/m-ab-s/media-autobuild_suite) and copy to `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps`

```cmd
./makejxl.exe "c:\\Users\\username\\Pictures\\My Vacation"
```

Or simpler alternative that doesn't need this script:

```powershell
cd c:\photos
Get-ChildItem -Path c:\temp\ -File -Include '*.jpg', '*.jpeg' -Name | Foreach {cjxl $_ $([io.path]::ChangeExtension($_, "jxl"))}
```

## See also
* [filmcompress](https://github.com/varnav/filmcompress/)

## TODO

* Decoder mode
