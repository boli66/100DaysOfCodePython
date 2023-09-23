import fileMaker
import path
names = "hitler bob chans"

fileMaker.saveFile(f"{path.IN}names.txt", ''.join([f"{s.title()}\n"for s in names.split(" ")]))