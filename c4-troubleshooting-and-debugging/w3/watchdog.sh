#!/bin/bash

watch_dog(){
  while true;
    do found=$(ps ax -o exe | grep /usr/bin/top);
    if [ -z "$found" ]; then 
      gnome-terminal -- top;
    fi;
    sleep 2;
    done 2>>/dev/null
}

watch_dog 

