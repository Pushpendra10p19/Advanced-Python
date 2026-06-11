import logging

logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")

#Output:
WARNING:root:Warning Message
ERROR:root:Error Message
CRITICAL:root:Critical Message

# Explaination:
# debug & info boths output not print because they hai come at low level in logging and the default level is warning and high level logs will print
# without basicConfig() debug & info logs will not work
