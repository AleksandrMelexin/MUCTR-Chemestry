#!/bin/bash
mount | grep "tmpfs" | sed /"mode="/d | awk {'print $3'} > memmntdir_t.txt
rm memmntdir.txt
cat memmntdir_t.txt | grep tmp >> memmntdir.txt
cat memmntdir_t.txt | grep shm >> memmntdir.txt
cat memmntdir_t.txt  >> memmntdir.txt


