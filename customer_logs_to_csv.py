from datetime import datetime
import logging
import posixpath
import sys

from pyspark.sql import SparkSession
import typer

import input_checks
from pyspark import SparkConf
