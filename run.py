from src.bitmap import Bitmap

bitmap = Bitmap()

cmd = input('Entre command \n ')
# while not os.path.isfile(cmd):
#   cmd = input('command ? => ')

cmd_list = cmd.split()
cmd_name = cmd_list[0]
bitmap.set_options(cmd_name, cmd_list[1:])
