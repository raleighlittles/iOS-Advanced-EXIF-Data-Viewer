import argparse
import os

# Local imports
import exif_reader
import accelerometer_visualizer
import subject_area


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument(
        "-i", "--input-file", type=str, help="iPhone image filename")

    argparse_args = argparse_parser.parse_args()

    image_filepath = argparse_args.input_file
    print("[DEBUG] Analyzing file ", image_filepath)
    image_basename = os.path.splitext(os.path.basename(image_filepath))[0]

    exif_data = exif_reader.get_exif_data(image_filepath)
    img_width, img_height = int(exif_data['ImageWidth'][0]), int(
        exif_data['ImageHeight'][0])
    print("[DEBUG] Image dimensions - Width=",
          img_width, " Height=", img_height)

    try:
        accel_data = exif_reader.get_acceleration_vector(exif_data)
        print("[DEBUG] Accelerometer data for image: ", accel_data)
        accel_plot_filename = accelerometer_visualizer.create_accelerometer_plot(
            image_basename, accel_data)

    except KeyError:
        print(
            "[ERROR] Image is missing accelerometer data. Make sure image is a native iOS photo.")

    try:
        subject_region = exif_reader.get_focus_area(exif_data)
        print("[DEBUG] Focus region for image ", subject_region)
        subject_area.draw_subject_highlight(
            image_filepath, subject_region, img_width, img_height)

    except KeyError:
        print("[WARN] No subject area found for image")
