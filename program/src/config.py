'''The Config class is responsible for loading and storing the configuration settings for the program.'''
import os
import sys

# Days for looking back for member joins
DAYS_OF_DATA = int(input("INPUT (MAIN) - Days to analyse?: "))

# Milestone amount for each election
MILESTONE_AMOUNT = 250000

# SEA's group ID
SEA_GROUP_ID = 2648601

if __name__ == "__main__":
    sys.call_tracing(sys.exit, ("\nERROR (CONFIG) - This file is not meant to be run directly. Please run SMED.py instead.",))