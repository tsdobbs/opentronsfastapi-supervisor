import asyncio
import threading
from typing import List
from functools import wraps
import requests

from fastapi import APIRouter
test_routes = APIRouter()

#temp config file that should be changed to a database
import config


# https://gist.github.com/amirasaran/e91c7253c03518b8f7b7955df0e954bbhsh
class BaseThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.args = args
        self.kwargs = args

    def target_with_callback(self, *args, **kwargs):
        self.method(*args, **kwargs)
        if self.callback is not None:
            self.callback()



def request_robot_endpoint(robot, endpoint):
    response = requests.get(robot + endpoint)
    return response

def robot_generator():
    for robot in config.robots:
        yield robot, config.robots[robot]
get_robot = robot_generator()

### Test funcs ####

@test_routes.get("/")
def read_root():
    return {"Message": "Hello World"}

@test_routes.post("/test/connection")
def test_connection(targets=None):
    if targets is None:
        targets = config.robots.keys()

    responses = dict()
    for robot in targets:
        robot_ip = targets[robot]
        responses[robot] = request_robot_endpoint(robot_ip, "/")

    return responses

#Home the first available robot
@test_routes.get("/test/home")
def test_home_func():
    response = None
    
    while response.status_code != 200:
        try:
            robot, robot_ip = next(get_robot)
            response = request_robot_endpoint(robot_ip, "/test/home")
        except StopIteration:
            return {"Message": "No robots available"}

    #TODO Log job completions somewhere
    return {"Message": f"Success! ROBOT {robot} completed job"}