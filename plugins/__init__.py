from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import operators
from operators import *
import helpers
from helpers import *

# Defining the plugin class
class CapstonePlugin(AirflowPlugin):
    name = "capstone_plugin"
    operators = [
        operators.AddConnectionOperator,
    ]
    helpers = [
    ]
