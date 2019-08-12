"""Handle the top-level command-line arguments provided to GatorGrader."""

from gator import constants
from gator import files

import argparse


def parse(args):
    """Parse the arguments provided on the command-line."""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Optional Arguments {{{

    # CHECKERDIR: the directory of user-provided checkers
    # REQUIRED? No
    # CORRECT WHEN: it is a valid directory
    parser.add_argument(
        constants.commandlines.Checker_Dir,
        metavar=constants.metavars.Dir,
        help=constants.help.Checker_Dir,
        type=str,
    )

    # JSON: output reports in JSON?
    # REQUIRED? No
    # CORRECT WHEN: always, only changes report output
    parser.add_argument(
        constants.commandlines.Json, help=constants.help.Json, action="store_true"
    )

    # NOWELCOME: do not display the welcome message?
    # REQUIRED? No
    # CORRECT WHEN: always, only changes output on screen
    parser.add_argument(
        constants.commandlines.No_Welcome,
        help=constants.help.No_Welcome,
        action="store_true",
    )

    # }}}

    # Positional Arguments {{{

    # CHECK: the name of the check
    # REQUIRED? Yes
    # CORRECT WHEN: always, selects a check and asks it to verify its own arguments
    parser.add_argument(
        constants.commandlines.Check,
        metavar=constants.metavars.Check,
        help=constants.help.Check,
        type=str,
    )

    # }}}

    # call argparse's parse_args function and return result
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args):
    """Check if the arguments are correct."""
    # assume the arguments are valid, then prove otherwise
    verified_arguments = True
    # CHECKERDIR: an external directory of checks was specified
    # ENSURE: this directory is a valid directory
    if args.checkerdir is not None:
        # assume that it is not a valid directory, then prove otherwise
        verified_arguments = False
        checkerdir_path = files.create_path(file="", home=args.checkerdir)
        # the directory does exist, so this argument is verified
        if checkerdir_path.is_dir():
            verified_arguments = True
    return verified_arguments
