Introduction
============

This project provides scripts and data that provide a simple way of using
tegrarcm and U-Boot to write U-Boot (or an alternative image) to the boot
flash of a Tegra device.

The flash images handled by this tool include just the bootloader and any
other data necessary for the bootloader to execute (i.e. the BCT). Creating or
flashing a root filesystem, either on the Tegra device's built-in flash, or on
external storage media, is a separate step unrelated to this tool.

Pre-requisites
==============

This document assumes that the instructions in README-developer.txt have
already been followed. Those instructions generate various files that the
flashing process uses. These include host-based utilities such as tegrarcm,
U-Boot binaries that run on the Tegra target device, and the flash images to
write to the Tegra device. 

If you are using a distribution package of this tool, the development steps
have likely already been followed, and you need only follow the instructions
in this file.

If you are working with the source code to this tool, you almost certainly
need to follow the instructions in README-developer.txt first.

Board Configurations
====================

Every Tegra board design has a name. Examples are Harmony or Cardhu.

Each board may exist in a number of different configurations; perhaps the
RAM size or speed varies, or a different type of boot flash is supported.
Each of these configurations is also given a name. tegra-uboot-flasher's
user-interface uses these configuration names exclusively. Examples are
harmony, cardhu-a02-1gb, cardhu-a04-1gb.

You may find a list of valid values for configname by executing:

tegra-uboot-flasher list-configs

Simple Usage - Flashing
=======================

To flash a board, connect a USB cable from your host PC to the Tegra device,
place that board into USB recovery mode, and execute the following as root
on the host machine:

tegra-uboot-flasher flash CONFIG

This will download code and data to the Tegra device and execute a flashing
routine. Once this is complete, the system will reboot into the freshly
flashed boot image, and the system will proceed to boot normally. Depending
on the board and U-Boot support, the flashing process may be observed via the
debug serial port, or on a built-in LCD panel.

Simple Usage - Testing U-Boot
=============================

If you simply want to download an unmodified U-Boot to the Tegra device and
execute it, execute the following as root on the host machine:

tegra-uboot-flasher exec CONFIG

This can be useful for quickly testing changes to U-Boot without writing it
to flash every time. This mode of operation is a very simple wrapper around
tegrarcm, which eliminates the need to remember which BCT to use for each
board configuration.

Advanced Options
================

A number of command-line options exist to control tegra-uboot-flasher's
behaviour. For example, you may specify an alternate image to be written
to boot flash, load configuration data from an alternate location, save
the temporary files created during execution for later analysis, etc.
Execute tegra-uboot-flasher with the --help option to see a description
of these options.
