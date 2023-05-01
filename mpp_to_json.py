import jpype
import mpxj

jpype.startJVM()
from net.sf.mpxj.reader import UniversalProjectReader
from net.sf.mpxj.json import JsonWriter

FileOutputStream = jpype.JClass("java.io.FileOutputStream")

project = UniversalProjectReader().read('Microsoft-Project-Example.mpp')

fileStream = FileOutputStream('out.json')

JsonWriter().write(project, fileStream)

jpype.shutdownJVM()