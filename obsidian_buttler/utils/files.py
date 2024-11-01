import glob


def find_files_by_extension(directory, extension):
    return glob.glob(f"{directory}/**/*{extension}", recursive=True)
