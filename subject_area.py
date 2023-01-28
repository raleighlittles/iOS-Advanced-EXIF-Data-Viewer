import os
import sys
import typing
import subprocess


def draw_subject_highlight(img_name: str, subject_area_exif: typing.List, img_width, img_height):

    subject_area_count = len(subject_area_exif)

    if (subject_area_count == 2):
        # The focus "area" in this case was a single point.
        # To show the point, draw 2 lines onto the image, where the two lines intersect is the focus point.
        focus_point_x, focus_point_y = subject_area_exif

        draw_horizontal_line_cmd = "convert -size 100x100 {} -draw \"line 0, {} {}, {}\" {}".format(
            img_name, focus_point_y, img_width, focus_point_y, img_name)

        if subprocess.run(draw_horizontal_line_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error running convert to draw X-line")
            sys.exit(2)

        draw_vertical_line_cmd = "convert -size 100x100 {} -draw \"line {}, 0, {}, {}\" {}".format(
            img_name, focus_point_x, focus_point_x, img_height, img_name)

        if subprocess.run(draw_vertical_line_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error running convert to draw Y-line")
            sys.exit(2)

    elif (subject_area_count == 3):
        focus_point_x, focus_point_y, circle_diam = subject_area_exif

        draw_focal_radius_cmd = "convert {} -fill none -stroke red -draw \'circle {}, {} {}, {}\' {}".format(
            img_name, focus_point_x, focus_point_y, focus_point_x, focus_point_y + (circle_diam / 2))

        if subprocess.run(draw_focal_radius_cmd.split(), stdout=subprocess.PIPE).returncode != 0:
            print("Error drawing circle")
            sys.exit(2)

    elif (subject_area_count == 4):
        x_center, y_center, rect_width, rect_height = subject_area_exif

        draw_rectangle_cmd = "convert -verbose {} -fill none -stroke red -draw \"rectangle {},{} {},{}\" {}".format(img_name,
                                                                                                                    x_center -
                                                                                                                    int(
                                                                                                                        0.5 * rect_width),
                                                                                                                    y_center -
                                                                                                                    int(
                                                                                                                        0.5 * rect_height),
                                                                                                                    x_center +
                                                                                                                    int(
                                                                                                                        0.5 * rect_width),
                                                                                                                    y_center +
                                                                                                                    int(
                                                                                                                        0.5 * rect_height),
                                                                                                                    img_name)

        print("[DEBUG] Executing command: ", draw_rectangle_cmd)

        # Doesn't work unless shell=True is set. Why??
        if subprocess.run(draw_rectangle_cmd, stdout=subprocess.PIPE, shell=True).returncode != 0:
            print("Error drawing rectangle")
            sys.exit(2)

    else:
        print("Unsupported subject area count: ", subject_area_count)
        sys.exit(3)
