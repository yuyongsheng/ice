#!/usr/bin/env python

import os, sys, FixUtil

def usage():
    print "Usage: " + sys.argv[0] + " [options]"
    print
    print "Options:"
    print "-h    Show this message."
    print

for x in sys.argv[1:]:
    if x == "-h":
        usage()
        sys.exit(0)
    elif x.startswith("-"):
        print sys.argv[0] + ": unknown option `" + x + "'"
        print
        usage()
        sys.exit(1)

ice_dir = os.path.normpath(os.path.join(os.path.dirname(__file__)))

FixUtil.replaceAllCopyrights(ice_dir, "Ice", "ICE_LICENSE", False)
for dir in ["slice", "cpp", "java", "cs", "vb", "php", "py", "rb", "demoscript", "distribution", "config", "certs",\
            "scripts"]:
    home = os.path.join(ice_dir, dir)
    if home:
       FixUtil.replaceAllCopyrights(home, "Ice", "ICE_LICENSE", True)

# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
cpatMatch = "20[0-9][0-9]-(20[0-9][0-9]) ZeroC"
copyright = "2009"

files = FixUtil.find(ice_dir, "*.rc")
files += FixUtil.find(ice_dir, "*LICENSE")
files += FixUtil.find(os.path.join(ice_dir, "cpp", "src"), "Gen.cpp")
files += FixUtil.find(os.path.join(ice_dir, "cpp", "src"), "Parser.cpp")
files += FixUtil.find(os.path.join(ice_dir, "cpp", "src", "Slice"), "*Util.cpp")
files += [os.path.join(ice_dir, "cpp", "src", "ca", "iceca")]
files += [os.path.join(ice_dir, "cpp", "doc", "symboltree.js")]
files += [os.path.join(ice_dir, "cpp", "demo", "Freeze", "backup", "backup")]
files += FixUtil.find(os.path.join(ice_dir, "cpp"), "*.bat")
files += [os.path.join(ice_dir, "cpp", "test", "IceSSL", "certs", "makecerts")]
files += [os.path.join(ice_dir, "java", "bin", "icegridgui.rpm")]
files += [os.path.join(ice_dir, "java", "src", "IceGridGUI", "Coordinator.java")]
files += FixUtil.find(os.path.join(ice_dir, "java", "resources", "IceGridAdmin"), "icegridadmin_content_*.html")
files += [os.path.join(ice_dir, "config", "makeprops.py")]
files += FixUtil.find(os.path.join(ice_dir), "AssemblyInfo.cs")
files += FixUtil.find(os.path.join(ice_dir, "distribution", "src", "rpm"), "*")
files += FixUtil.find(os.path.join(ice_dir, "php"), "*.php")
files += [os.path.join(ice_dir, "cpp", "test", "Slice", "errorDetection", "IllegalIdentifier.ice")]
files += [os.path.join(ice_dir, "distribution", "src", "rpm", "mcpp-devel.spec")]

for f in files:
    FixUtil.fileMatchAndReplace(f, [(cpatMatch, copyright)])
