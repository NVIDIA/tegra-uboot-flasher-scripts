Introduction
============

This project provides scripts and data that provide a simple way of using
tegrarcm and U-Boot to write U-Boot (or an alternative image) to the boot
flash of a Tegra device.

This project relies on source and data provided by various other projects.

cbootimage         - Creates Tegra flash images.
cbootimage-configs - Board-specific data for cbootimage.
tegrarcm           - Communicates with Tegra boot ROM over USB.
dtc                - Compiles device tree files, and provides utilities
                     to manipulate device trees.
U-Boot             - A bootloader. Used to write to Tegra's boot flash,
                     and is typically written to the boot flash.

cbootimage, tegrarcm, and dtc are simply utilities used by this project. If
your distro packages up-to-date versions of these tools, then they may be
installed and used. However, this is often not the case, so a script
named "build-tools" has been provided, which will build those tools and place
them into a directory that the other scripts add to their $PATH.

cbootimage-configs and U-Boot are actively used by the "build" script, and
hence must always be available.

For more details how these tools fit together, see the documentation at:

ftp://download.nvidia.com/tegra-public-appnotes/index.html

Obtaining the Source
====================

You are expected to use Google's repo tool to obtain the source.

For more information about repo, see:

http://code.google.com/p/git-repo/

To obtain repo, do the following in a directory in your $PATH:

curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > repo
chmod a+x repo

To obtain the source of the tegra-uboot-flasher project, do:

mkdir tegra-uboot-flasher
cd tegra-uboot-flasher
repo init -u git://github.com/NVIDIA/tegra-uboot-flasher-manifests.git \
        -m MANIFEST # see explanation below
repo sync

There are two separate repo manifests for this project. Use repo's -m option
to specify which you want. Valid values are default.xml (all required
dependencies) and default-notools.xml (excludes the source to potentially
distro-packaged utilities cbootimage, tegrarcm, dtc).

Compiling Potentially Packaged Utilities
========================================

If you have installed distro packages for the utilities mentioned above,
and/or sync'd the default-notools.xml manifest, skip this step.

cd to the scripts sub-directory (i.e. the directory containing this README),
and execute:

./build-tools

Creating Flash Images
=====================

This step creates the target binaries and supporting data files necessary to
run the tegra-uboot-flasher script. You will always need to perform this step.

You will need an ARM cross-compiler in order to compile U-Boot. This may be
obtained from a distribution package, or be a custom-built toolchain. The
environment variable CROSS_COMPILE should be set to select the compiler to
use. CROSS_COMPILE should contain the common prefix of all the binaries in
the cross-compiler, for example if gcc is arm-linux-gnueabi-gcc, then
CROSS_COMPILE should be set to arm-linux-gnueabi-, or
/path/to/arm-linux-gnueabi-. If this variable is not set, then the build
script assumes a value of arm-linux-gnueabi-.

cd to the scripts sub-directory (i.e. the directory containing this README),
and execute:

./build

Flashing Devices
================

If you wish, you may run the tegra-uboot-flasher script directly from the
source tree. The script will automatically find the build results generated
in the previous step. For details on running this script, please see
README-user.txt in this directory.

Packaging the Build Results
===========================

The build script generates the directory tree ../_out. this contains all data
required by the tegra-uboot-flasher script. The content of this directory
should be installed into /usr/share/tegra_uboot_flasher.

The tegra-uboot-flasher script itself should be installed somewhere in $PATH.

The Python module tegraboardconfigs.py should be installed somewhere that
Python can locate it.
