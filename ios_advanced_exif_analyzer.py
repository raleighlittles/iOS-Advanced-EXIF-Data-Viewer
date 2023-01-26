import argparse
import matplotlib.pyplot
import os
import pandas


import exif_reader
import accelerometer_visualizer
import subject_area

# https://exiftool.org/TagNames/Apple.html

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-i", "--input-file", type=str, help="Image")

    argparse_args = argparse_parser.parse_args()

    image_filename = argparse_args.input_file
    print("[DEBUG] Analyzing file ", image_filename)

    # Get EXIF data

    exif_data = exif_reader.get_exif_data(image_filename)

    accel_data = exif_reader.get_acceleration_vector(exif_data)
    print("[DEBUG] Accelerometer data for image: ", accel_data)

    subject_region = exif_reader.get_focus_area(exif_data)
    print("[DEBUG] Focus region for image ", subject_region)

    img_width, img_height = int(exif_data['ImageWidth'][0]), int(exif_data['ImageHeight'][0])
    print("[DEBUG] Image dimensions - Width=", img_width, " Height=", img_height)

    accel_plot_filename = accelerometer_visualizer.create_accelerometer_plot(accel_data)
    subject_area.draw_subject_highlight(image_filename, subject_region, img_width, img_height)
    







