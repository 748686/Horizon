"""Shared CLI argument helpers for Horizon entrypoints."""

import argparse


def add_log_level_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-l", "--log-level",
        default="WARNING",
        type=str.upper,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        metavar="LEVEL",
        help="Logging level (default: WARNING)",
    )
