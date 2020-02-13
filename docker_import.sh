#!/bin/bash
docker import --change 'CMD ["/bin/bash"]' server.tar naihai:0.5
