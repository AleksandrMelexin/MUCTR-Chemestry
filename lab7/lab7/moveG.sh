#!/bin/bash
mkdir -p Gbest
cp G-$1-$2-*.inp Gbest/
cp temp/$1-best-$2conv-$1-$2.csv Gbest/
