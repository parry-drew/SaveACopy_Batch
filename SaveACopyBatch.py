#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# SaveACopyBatch.py
# This script is a batch processing tool for copying MXDs into a format that can be
# used by older versions of ArcMap.
#
# C:\Python27\ArcGIS10.4\python.exe SaveAsCopyBatch.py
#
# ---------------------------------------------------------------------------
import os, datetime, timeit, shutil, zipfile, arcpy

root = os.path.abspath(os.path.curdir)

def manage_directories(d):
    for i in d:
        if os.path.exists(root + "\\" + i):
            shutil.rmtree(root + "\\" + i)
            os.makedirs(root + "\\" + i)
        else:
            os.makedirs(root + "\\" + i)

def save_as_copy_loop(d, versions):
    for mxd in os.listdir(d):
        if mxd.endswith(".mxd"):
            for version in versions:
                print("\n    saveACopy output : " + root +"\\"+ version +"\\"+ mxd)
                arcpy.mapping.MapDocument(mxd).saveACopy(root +"\\"+ version +"\\"+ mxd , version)

def main():
    print('    What earlier version of ArcGIS do need to make? ')
    raw_dir = raw_input('    Leave a space between value like this : 10.0 10.1 10.3 --> ')
    directory = raw_dir.split()

    print('\n    Where is the directory containing your mxds?  ')
    raw_mxds = raw_input('    Drag the folder containing your mxd here and hit enter. --> ')

    start = timeit.default_timer()
    print('\n    PROCESSING ...')
    manage_directories(directory)
    save_as_copy_loop(raw_mxds , directory)
    stop = timeit.default_timer()
    print("\n    COMPLETED! Total Run Time: " +  str(stop - start) + " seconds")

if __name__ == '__main__':
    main()
