#!/bin/bash
output_dir=/home/hadoop/Applications/
for file in $( ls | grep tar.gz )
do
    tar -zxvf $file -C $output_dir
done

for file in $( ls $output_dir )
do
    mv "$output_dir/$file" "$output_dir/${file%%-*}"
done

typeset -u home
for file in $( ls $output_dir )
do
    home="${file}_HOME"
    echo "export $home=$output_dir$file" >> ~/.bashrc
    echo "export PATH=\$$home/bin:\$PATH" >> ~/.bashrc
done

source ~/.bashrc

