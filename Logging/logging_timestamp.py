import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("Low memory")
logging.error("An error occurred")

# output:
2026-06-11 16:55:20,123 - INFO - Program started
2026-06-11 16:55:20,124 - WARNING - Low memory
2026-06-11 16:55:20,125 - ERROR - An error occurred

# Explaination:
# To displey the time of activity we use timestamp formate
# Where : %(asctime)s is used for yy/mm/dd , %(levelname)s is used for displey the log levels and %(message)s id used for activity message
