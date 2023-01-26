import os
import pandas
import subprocess
import typing

def get_exif_data(filename: str) -> dict:
    exiftool_cmd_get_all_metadata_csv = "exiftool -a -U -csv {}".format(filename)
    exiftool_csv_string = subprocess.run(exiftool_cmd_get_all_metadata_csv.split(), stdout=subprocess.PIPE).stdout.decode('utf-8', 'ignore').strip()
    exif_dict = pandas.read_csv(io.StringIO(exiftool_csv_string)).to_dict()
    return exif_dict

def get_acceleration_vector(exif_data : dict) -> typing.List:
    return [float(component) for component in str(exif_data["AccelerationVector"][0]).split(" ")]


def get_focus_area(exif_data : dict) -> typing.List:
    return [int(point) for point in str(exif_data["SubjectArea"][0]).split(" ")]