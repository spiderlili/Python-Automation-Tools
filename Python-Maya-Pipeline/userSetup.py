import inspect
import os

user_setup_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("Reading userSetup.py from {0}".format(user_setup_path))