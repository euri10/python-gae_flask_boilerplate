import os

# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
# vendor.add('lib')

# from https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#installing_a_library
# The appengine_config.py file above assumes that the current working directory is
# where the lib folder is located. In some cases, such as unit tests, the current
# working directory can be different. To avoid errors, you can explicitly pass
# in the full path to the lib folder using:
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
