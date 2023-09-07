import fileMaker
import path
names = "Kitty John Jonathan Andrew"

fileMaker.saveFile(f"{path.IN}names.txt", ''.join([f"{s}\n"for s in names.split(" ")]))