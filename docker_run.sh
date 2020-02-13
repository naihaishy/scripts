#!/bin/bash
docker run -d \
--name naihai_space \
--hostname future \
--device /dev/fuse \
--privileged \
-p 80:80 \
-p 443:443 \
-p 3306:3306 \
-p 6264:22 \
-i -t naihai:0.5
