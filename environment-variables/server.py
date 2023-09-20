from dotenv import load_dotenv, find_dotenv


# load_dotenv("find_dotenv()")
load_dotenv(
    dotenv_path=find_dotenv(), # Absolute or relative path to .env file.
    stream=None, # Text stream (such as io.StringIO) with .env content, used if dotenv_path is None.
    verbose=None, # Whether to output a warning the .env file is missing.
    override=None,
    interpolate=True,
    encoding="utf-8", # Encoding to be used to read the file.
) # Returns Bool: True if at least one environment variable is set else False;
# Ps: If both dotenv_path and stream are None, find_dotenv() is used to find the .env file
load_dotenv()

# NOW ACCESS THE ENVIRONMENT VARIABLE MY_ENVIRONMENT_VARIABLE SETTED ON .env file

import os

os.environ.get()