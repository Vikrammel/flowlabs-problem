import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

from typer import Typer

from .solution import change_me

app = Typer()


@app.command()
def main():
    log.info("Thank you for interviewing with Flow Labs!")
    log.info("If you have not already done so, please check out the README.")
    try:
        log.info(f"Solution: {change_me()}")
    except NotImplementedError:
        log.error(("Solution not yet implemented"))
