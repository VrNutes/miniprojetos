"""
importation of python-dotenv library that loads the environment variables into
python environment variables
"""
from dotenv import load_dotenv, find_dotenv

# search for .env file that must contains the environment variables preset
if not find_dotenv():
    print("Please use the command 'cp .env.example .env' and rerun the command'") # write message on stdout
    exit() # exit application

load_dotenv(
    dotenv_path=find_dotenv(), # Absolute or relative path to .env file.
    stream=None, # Text stream (such as io.StringIO) with .env content, used if dotenv_path is None.
    verbose=None, # Whether to output a warning the .env file is missing.
    override=None, # If already loaded environment variable, override the value of variable with .env content.
    interpolate=True,
    encoding="utf-8", # Encoding to be used to read the file.
) # Returns Bool: True if at least one environment variable is set else False;
# Ps: If both dotenv_path and stream are None, find_dotenv() is used to find the .env file

# NOW ACCESS THE ENVIRONMENT VARIABLE MY_ENVIRONMENT_VARIABLE SETTED ON .env file

import os

MY_ENVIRONMENT_VARIABLE = os.environ.get("MY_ENVIRONMENT_VARIABLE")
print(f"environment variable:\n MY_ENVIRONMENT_VARIABLE has value = {MY_ENVIRONMENT_VARIABLE}")

default_value = "default_value"
MY_ENVIRONMENT_VARIABLE_NOT_SETTED = os.environ.get("MY_ENVIRONMENT_VARIABLE_NOT_SETTED", default_value)
print(f"environment variable not setted, but has a default value:\nMY_ENVIRONMENT_VARIABLE_NOT_SETTED has value = {MY_ENVIRONMENT_VARIABLE_NOT_SETTED} == {default_value}")


MY_ENVIRONMENT_VARIABLE_NOT_SETTED_WITHOUT_DEFAULT = os.environ.get("MY_ENVIRONMENT_VARIABLE_NOT_SETTED_WITHOUT_DEFAULT")
print(f"environment variable:\n MY_ENVIRONMENT_VARIABLE_NOT_SETTED_WITHOUT_DEFAULT has value = {MY_ENVIRONMENT_VARIABLE_NOT_SETTED_WITHOUT_DEFAULT}")