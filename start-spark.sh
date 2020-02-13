#!/bin/bash
# 启动spark任务

# 1. 自动添加jar包依赖
sparkExtraLibDir=/home/hadoop/Runs/libs
for jar in $( ls $sparkExtraLibDir | grep "jar" )
do
    if [ -z "$jars" ];then
        jars=${sparkExtraLibDir}"/"${jar}
    else
        jars=${sparkExtraLibDir}"/"${jar}":"${jars}
    fi
done
#echo $jars
spark-submit \
    --master spark://219.223.174.21:7077 \
    --executor-memory 6G \
    --executor-cores 4 \
    --driver-memory 4G \
    --driver-class-path $jars \
    --class com.naihai.jobs.OfflineJob Runs/Recommend.jar
