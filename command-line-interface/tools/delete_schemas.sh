#!/bin/bash
for i in <schema-name-value> <schema-name-key>
do
    echo $i
    curl -X DELETE http://<host:port>/subjects/$i
done
