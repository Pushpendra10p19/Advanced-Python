import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")

# Explaination:
# To save all activity of program we create a app.log file
# The activity of program will save in app.log 
