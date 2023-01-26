import argparse
import matplotlib.pyplot
import os
import pandas


# https://exiftool.org/TagNames/Apple.html

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-i", "--input-file", type=str, help="Image")

    argparse_args = argparse_parser.parse_args()

    image_filename = argparse_args.input_file


