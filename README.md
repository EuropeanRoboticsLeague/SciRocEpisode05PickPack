# SciRocEpisode05PickPack
Logging capability for SciRoc Episode 05


The file 'sciroc_episode05_logging.py' will provide helper function to log the robot status to
an online sheet.

## Logging functions available

1. `log_run_started`
2. `log_object_picked`
3. `log_object_placed`
4. `log_run_stopped` 

## Pre-requisite library
```
pip3 install requests
```

## Usage
1. copy 'sciroc_episode05_logging.py' file to your folder with functionality code.
2. import file 
3. Instantiate `LogStatusSciRoc` class
4. use the functions

## Demo

```
import sciroc_episode05_logging

#Initialize the logger with team name 
sciroc_log = sciroc_episode05_logging.LogStatusSciRoc(team_name='AutonOHM')

#Logging start of run
sciroc_log.log_run_started()

#Logging object picked
sciroc_log.log_object_picked(object_name='Ocado Toasted Sesame Oil')

#Logging object placed
sciroc_log.log_object_placed(object_name='Ocado Toasted Sesame Oil')

#logging object dropped
sciroc_log.log_object_placed(object_name='DROPPED')

#logging run stopped
sciroc_log.log_run_stopped()

```

