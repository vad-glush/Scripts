#!/bin/sh

if [[ -z "$1" ]]
then

  echo "Usage: ${0} <stack name>"

else
 
  filedir="/tmp/fromswarm/logs-$(date +%Y%m%d_%H%M%S)"
  mkdir $filedir
  for item in $(docker service ls --format "{{.Name}}" --filter "NAME=${1}"); do echo $item; docker service logs ${2} $item > $filedir/$item.log 2>&1; done
  find $filedir -size 0 -delete
#  tar -czvf $filedir.tar.gz $filedir/*.log
#  rm -rf $filedir
  
fi
