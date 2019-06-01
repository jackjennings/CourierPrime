from hellbox import Hellbox
from hellbox.jobs.fontmake import GenerateOtf, GenerateTtf

with Hellbox("build") as task:
    ufo = task.read("ufo/*")
    otf = ufo >> GenerateOtf()
    ttf = ufo >> GenerateTtf()

    otf >> task.write("build/otf")
    ttf >> task.write("build/ttf")
