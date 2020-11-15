#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
   
if __name__ == '__main__':
    path = input("If you want to delete empty folders,Please Enter Path:")

    for root, dirs, files in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)
                print("Delete:" + dir)
            except Exception as e:
                continue

    input("\nComplete!")