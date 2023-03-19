#!/usr/bin/env python3

import os
import sys
import argparse
import binwalk


def logo():
    print("   ___                             __  _     ")
    print("  / __\__  _ __ ___ _ __  ___   _ / / | | __ ")
    print(" / _\/ _ \| '__/ _ \ '_ \/ __| (_) |  | |/ / ")
    print("/ / | (_) | | |  __/ | | \__ \  _| |  |   <  ")
    print("\/   \___/|_|  \___|_| |_|___/ ( ) |  |_|\_\\")
    print("                                  \_\       ")
    print("                                             ")


##########GET INFO##########
def parse_file_types(l):
    types = ["PDF","Zlib"]
    occ = [0,0]
    res = []
    for e in l:
        if "PDF" in e:
            occ[0]+=1
        if "Zlib" in e:
            occ[1]+=1
    for i in range(len(occ)):
        res.append((types[i],occ[i]))
    return res


#Getting info on embedded files
def get_info(path):
    try:
        for x in binwalk.scan(path,signature=True,quiet=True):
            print("[+] Infos")
            types = []
            for result in x.results:
                #print(result.description)
                types.append(result.description)
        parsed = parse_file_types(types)
        for tp in parsed:
            print("    "+"¤ "+tp[0]+": "+str(tp[1]))
    except binwalk.ModuleException as e:
        print ("Critical failure:", e)

    #new_dir = path + "_extracted"
    #zipped.extractall(os.mkdir(path))

############################

###########EXTRACT##########
#TODO
############################


#def parse_args():
#    parser = argparse.ArgumentParser(
#        description="A Forensic tool to help gathering info before analysis",
#        format_class=argparse.ArgumentDefaultsHelpFormatter,)
#    subparsers = parser.add_subparser(dest='mode', title="Mode")
#    subparsers.required = True
#    #continue, inspire from: https://github.com/aress31/jwtcat/blob/master/jwtcat.py


def main():
    logo()
    if(len(sys.argv) != 2):
        sys.exit("Invalid arguments :(")
    logo()
    get_info(sys.argv[1])


if __name__ == "__main__":
    main()



