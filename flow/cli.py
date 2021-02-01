"""
package: flow

file: cli.py

Defines the cli through which the user can interact with the solution functions
"""

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

from typer import Typer

from .solution import find_solution, InvalidInputException

app = Typer()


@app.command()
def main():
    log.info("Thank you for reviewing my solution!")
    log.info("If you have not already done so, please check out the README.")
    try:
        log.info(f"Solution (max_ticket_uid, missing_ticket_uid): {find_solution('input.txt')}")
    except InvalidInputException:
        log.error(("Invalid characters in input file. Please double check data/input.txt and re-run."))
