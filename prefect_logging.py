"""
Logging example
	* write >=INFO logs to a file
	* visualize with graphviz: 
		1. download and install graphviz executable
"""
import logging
import os

logging.basicConfig(
	level=logging.DEBUG,
	format='{asctime} {levelname:<8} {message}',
	style='{',
	filename='esg_radar.log', 
	filemode='w'
)

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

# logging with the standard loggin module
logging.debug("Debug msg")
logging.info("Info msg")
logging.warning("Warning msg")
logging.error("Error msg")
logging.critical("Critical msg")

print(*os.environ['PATH'].split(";"), sep='\n')

"""
This is a simple flow that takes in a required parameter `value` and determines if it is even or odd.

This utilizes one of the control flow tasks from the Prefect task library for evaluating
the conditional returned from the `check_if_even` task.
"""
from prefect import Flow, Parameter, task
from prefect.tasks.control_flow import ifelse


@task
def check_if_even(value):
    return value % 2 == 0


@task
def print_odd(value):
    print("{} is odd!".format(value))


@task
def print_even(value):
    print("{} is even!".format(value))


with Flow("Check Even/Odd") as f:
    value = Parameter("value")
    is_even = check_if_even(value)

    even = print_even(value)
    odd = print_odd(value)

    ifelse(is_even, even, odd)


# Prints '2 is even!'
f.run(value=2)


# Prints '1 is odd!'
f.run(value=1)

f.visualize()