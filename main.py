"""
MoviePy
Install: pip install moviepy
"""

"""
Pillow
Install: pip install Pillow
"""

"""
pySimpleGUI
Install: pip install PySimpleGUI
        pip install PySimpleGUIQt
"""

"""
pySimpleGUI deploy into .exe:
Install: pip install pysimplegui-exemaker
Run: python -m pysimplegui-exemaker.pysimplegui-exemaker
"""

import os
import io
import PySimpleGUI as sg
import PySimpleGUIQt as sq
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image
from PIL import ImageTk
import tkinter
# import moviepy
import re


def blank_frame(size=(0, 0)):
    image = Image.open(rootPath + "\\img\\" + 'background.GIF')
    # image.thumbnail((4000, 4000))
    bio = io.BytesIO()
    image.save(bio, format="GIF")
    # print(bio.getvalue())
    return [
        # [sg.Window('Everything bagel', layout=[[]], finalize=True, keep_on_top=True, grab_anywhere=False,
        #            transparent_color=sg.theme_background_color(), no_titlebar=True)],
        [sg.Image(data=bio.getvalue(), expand_x=True, expand_y=True)],
        [sg.Frame("", layout=[[]], expand_x=True, expand_y=True, border_width=0, vertical_alignment='top')],
    ]


def set_column_size(element, size):
    # Only work for sg.Column when `scrollable=True` or `size not (None, None)`
    options = {'width': size[0], 'height': size[1]}
    if element.Scrollable or element.Size != (None, None):
        element.Widget.canvas.configure(**options)
    else:
        element.Widget.pack_propagate(0)
        element.set_size(size)


def title_bar(title, text_color, background_color):
    """
    Creates a "row" that can be added to a layout. This row looks like a titlebar
    :param title: The "title" to show in the titlebar
    :type title: str
    :param text_color: Text color for titlebar
    :type text_color: str
    :param background_color: Background color for titlebar
    :type background_color: str
    :return: A list of elements (i.e. a "row" for a layout)
    :rtype: List[sg.Element]
    """
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [[sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0),
                    background_color=bc)],
            [sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),
                      sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]],
                    element_justification='r', key='-C-', grab=True,
                    pad=(0, 0), background_color=bc)]]


def get_videofiles(directory, type):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # get file extension by using regex
            filename_extension = re.search('\.([^.])+$', filename).group(0)

            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            try:
                video = VideoFileClip(os.path.join("path", "to", filepath))
                if not video.audio:
                    print("not a movie but an image! " + filename_extension)
                    continue
            except:
                continue
            print(filename_extension)
            if type == "filepath":
                file_paths.append(filepath)
            elif type == "filename":
                file_paths.append(
                    [filename, filename_extension])
            elif type == "extension":
                file_paths.append(filename_extension)
            else:
                break

    return file_paths  # Self-explanatory.


rootPath = os.path.abspath(os.curdir)
rootPathConvFolder = rootPath + "\\convert folder\\"
print(rootPathConvFolder)
# get all file paths
file_names = []

sg.theme('DarkBrown4')
# sg.theme_previewer()


col1 = blank_frame()
print(col1[1])
column1 = [[col1[0][0]],
           [col1[1][0].layout([
               # [col1[0][0]],
               [sg.Text('Choose video file to convert:', justification='center')],
               [
                   sg.Table(headings=["1", "2"],
                            values=[["sdassda", "sdfsdfsdf", "Sdfsdfdf"],
                                    ["sdassda", "sdfsdfsdf", "Sdfsdfdf"],
                                    ["sdassda", "sdfsdfsdf", "Sdfsdfdf"],
                                    ], col_widths=10, enable_events=True, key="file_names",
                            row_height=25, num_rows=20, auto_size_columns=True, justification='center',
                            expand_x=True, expand_y=True),
                   sg.Frame("", layout=[
                       [sg.Checkbox("", default=True, key="checkboxConv_", expand_x=True, expand_y=True)]
                   ], expand_y=True, size=(50, 0), key="checkboxConvTable", background_color="#000000"),
               ]
           ])
           ]
           ]

col2 = blank_frame()
column2 = [
    [col2[1][0].layout([
        [sg.Text('Change into audio file:', justification='center')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]
    ])
    ]
]

layout = [
    [
        sg.Frame("column1", column1, key="column1", expand_x=True, expand_y=True),
        sg.Frame("column2", column2, key="column2", expand_x=True, expand_y=True),
    ],
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
    [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
    [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
    [sg.Submit(), sg.Cancel()],
]
# main window
window = sg.Window('Window Title', layout, finalize=True, )
# sg.theme_background_color('#999999')

# full_file_paths = get_videofiles(rootPathConvFolder, "filepath")
launched = False

while True:
    # layout[2](values=file_names)
    while True:
        event, values = window.read(timeout=500)
        # print('You entered 1', values)
        break
    while True:
        # event, values = window.read()
        # print('You entered 2')
        break
    if not launched:
        launched = True
        file_names = get_videofiles(rootPathConvFolder, "filename")
        print(30 * len(file_names) + 50)
        checkboxList = []
        for key, filename in enumerate(file_names):
            checkboxList.append(
                [sg.Checkbox("", default=True, key="checkboxConv_" + filename[0], expand_x=True, expand_y=True)])

        window["file_names"].update(file_names)
        print("----------")
        # sg.Column.Update()
        print(layout["checkboxConvTable"][0])
        print(checkboxList)
        # print(window["checkboxConvTable"].layout([]))
        # window["file_names"].set_size(size=(400, 3 * len(file_names)))
        # window['column1'].set_size(size=(500, 30 * len(file_names) + 500))
        # window['column2'].set_size(size=(500, 30 * len(file_names) + 50))
        # set_column_size(window['column1'], (500, 30 * len(file_names) + 50))
        # set_column_size(window['column2'], (500, 30 * len(file_names) + 50))
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        print("close window!")
        break

window.close()
# print(button, values[0], values[1], values[2])

# for id in range (2, 3, 1):
#     video = VideoFileClip(os.path.join("path","to", rootPathConvFolder + str(id) + ".mp4" ))
#     video.audio.write_audiofile(os.path.join("path","to", rootPathConvFolder + str(id) + ".mp3" ))
