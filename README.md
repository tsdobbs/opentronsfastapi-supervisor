# opentronsfastapi-supervisor

opentronsfastapi-supervisor is a library that compliments opentronsfastapi, focusing on managing job at the system level.

For example, a biofoundry might have the following components for successfully executing a protocol:
1. A job queue that lists the tasks to be done
2. A system-level execution manager that decides what job to do next and passes the job to an appropriate robot
3. A client on the robot that receives job requests and, if accepted, initiates execution on the robot
4. A low-level layer that converts job instructions to the acutation of motors

opentronsfastapi-supervisor specifically helps with #2, assuming you haave opentronsfastapi handling #3.

## Features
- Allows configuring of robots in its purview and their capabilities
- Given a job, decides a capable robot for that job and passes it to the executor on that robot
- If the robot refuses the job, finds the next capable robot for execution
- If no capable robot can be found to execute the job, logs job as failed

## Limitations


## Todo
