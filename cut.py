import json
import os
import subprocess
from vsatcloud.scene import ProcessingScene


class CutProcess(ProcessingScene):
    def __init__(self, params):
        if params['geometry_json'] is None or params['geometry_json'] == "":
            self.geometry_json = None
        else:
            self.geometry_json = params['geometry_json']

    def process(self, input_file_path):
        """
        :param self:
        :param input_file_path: 待裁剪raster路径
        :return: 输出文件的绝对路径
        """
        geometry_path = self.write_geometry()
        output_path = os.path.join(os.getcwd(), "cut_target.tif")
        args = [
            "gdalwarp", "-cutline", geometry_path, "-t_srs", "EPSG:4326",
            "-dstnodata", "0", "-crop_to_cutline", "-dstalpha", "-of", "GTiff",
            input_file_path, output_path
        ]
        try:
            obj = subprocess.Popen(args)
            obj.wait()
        except BaseException as e:
            print(str(e))
            raise Exception("cut failed")
        return output_path

    def write_geometry(self):
        with open("vector.json", 'w+') as geom:
            geom.write(json.dumps(self.geometry_json))
        return os.path.join(os.getcwd(), "vector.json")


if __name__ == '__main__':
    CutProcess.run()
