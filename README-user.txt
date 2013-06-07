Introduction
============

This project provides scripts and data that provide a simple way of using
tegrarcm and U-Boot to write U-Boot (or an alternative image) to the boot
flash of a Tegra device.

Board Configurations
====================

Every Tegra board design has a name. Examples are Harmony or Cardhu.

Each board may exist in a number of different configurations; perhaps the
RAM size or speed varies, or a different type of boot flash is supported.
Each of these configurations is also given a name. tegra-uboot-flasher's
user-interface uses these configuration names exclusively. Examples are
harmony, cardhu-a02-1gb.config, cardhu-a04-1gb.config.

You may find a list of valid values for configname by executing:

tegra-uboot-flasher --list-confignames

Simple Usage
============

To flash a board, connect a USB cable from your host PC to the Tegra device,
place that board into USB recovery mode, and execute the following as root
on the host machine:

tegra-uboot-flasher configname

This will download code and data to the Tegra device and execute a flashing
routine. Once this is complete, the system will reboot into the freshly
flashed boot image, and the system will proceed to boot normally. Depending
on the board and U-Boot support, the flashing process may be observed via the
debug serial port, or on a built-in LCD panel.

Advanced Options
================

A number of command-line options exist to control tegra-uboot-flasher's
behaviour. For example, you may specify an alternate image to be written
to boot flash, load configuration data from an alternate location, save
the temporary files created during execution for later analysis, etc.
Execute tegra-uboot-flasher with the --help option to see a description
of these options.
