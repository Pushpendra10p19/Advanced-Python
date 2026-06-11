import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")

# Output:
DEBUG:root:Debug Message
INFO:root:Info Message
WARNING:root:Warning Message
ERROR:root:Error Message
CRITICAL:root:Critical Message

# Explaination:
# All log levels outputs are printed using basicConfig() method
# In logging.basicConfig(level=logging.DEBUG)  DEBUG is used because DEBUG is the lowest log by which all upper logs will work 
