#!/usr/bin/env python 3


#Author ID: sdaweng

import subprocess


def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'",
                            shell = True,
                            capture_output=True,
                            text=True)
    return result.stdout.strip()

if __name__ == "__main__":
    print(free_space())
