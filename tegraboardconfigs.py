# Copyright (c) 2013, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import os

debug = False

socs = {}
boards = {}
configs = {}

def _load_something(path, filetype, name, saveindict):
    fn = os.path.join(path, name + '.' + filetype)
    d = {}
    execfile(fn, globals(), d)
    saveindict[name] = d[filetype]

def _load_soc(path, socname):
    if socs.has_key(socname):
        return
    if debug: print 'load soc', socname
    _load_something(path, 'soc', socname, socs)

def _load_board(path, boardname):
    if boards.has_key(boardname):
        return
    if debug: print 'load board', boardname
    _load_something(path, 'board', boardname, boards)
    _load_soc(path, boards[boardname]['soc'])

def _load_config(path, configname):
    if configs.has_key(configname):
        return
    if debug: print 'load config', configname
    _load_something(path, 'config', configname, configs)
    _load_board(path, configs[configname]['board'])

def load_configs(path):
    fns = os.listdir(path)
    for fn in fns:
        if not fn.endswith('.config'):
            continue
        cfgname = fn[:-7]
        _load_config(path, cfgname)

if __name__ == '__main__':
    debug = True
    load_configs('configs')
    print
    print socs
    print
    print boards
    print
    print configs
