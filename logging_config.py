import logging as log # Import package and rename it

# Call the basic setting
# format = display date&time - level - message
# datefmt = 12/12/2010 11:46:36 AM

#DEBUG
#log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d7%Y %I:%M:%S %p')

#INFO
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d7%Y %I:%M:%S %p')


# Test code
if (__name__ == "__main__"):
    log.debug("Message ...")