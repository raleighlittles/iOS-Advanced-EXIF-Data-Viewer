import os
import sys
import typing
import subprocess

# https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/subjectarea.html

def draw_subject_highlight(image_name : str, subject_area_exif : typing.List, exif_data : dict):

    if len(subject_area_exif) == 2:
        # The focus "area" in this case was a single point.
        # To show the point, draw 2 lines onto the image, where the two lines intersect is the focus point.
        focus_point_x, focus_point_y = subject_area_exif
        img_width, img_height = str(exif_data["ImageWidth"][0]), str(exif_data["ImageHeight"][0])

        draw_horizontal_line_cmd = "convert -size 100x100 {} -draw \"line 0, {} {}, {}\" {}".format(image_name, focus_point_y, img_width, focus_point_y, image_name)

        if subprocess.run(draw_horizontal_line_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error running convert to draw X-line")
            sys.exit(2)

        draw_vertical_line_cmd = "convert -size 100x100 {} -draw \"line {}, 0, {}, {}\" {}".format(image_name, focus_point_x, focus_point_x, img_height, image_name)
        
        if subprocess.run(draw_vertical_line_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error running convert to draw Y-line")
            sys.exit(2)

        
    elif (len(subject_area_exif) == 3):
        focus_point_x, focus_point_y, circle_diam = subject_area_exif

        draw_focal_radius_cmd = "convert {} -fill none -stroke black -draw \'circle {}, {} {}, {}\' {}".format(image_name, focus_point_x, focus_point_y, focus_point_x, focus_point_y + (circle_diam / 2))

        if subprocess.run(draw_focal_radius_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error drawing circle")
            sys.exit(2)


    else:
        # Draw rectangle using 
        x, y, width, area = subject_area_exif

