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


def add_data_dir_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-d", "--data-dir",
        default="data",
        metavar="PATH",
        help="Path to the data directory (default: 'data')",
    )
    parser.add_argument(
        "-c", "--config",
        default=None,
        metavar="PATH",
        help="Path to config file (default: <data-dir>/config.json)",
    )
