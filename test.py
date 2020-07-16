import os
from pathlib import Path

from cut import CutProcess

if __name__ == "__main__":
    params = {
        "geometry_json": {
            "type":
            "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type":
                    "Polygon",
                    "coordinates": [[[102.12874733238306, 27.92533465949343],
                                     [102.13112659321388, 27.917406009549182],
                                     [102.13765256577517, 27.916024442881607],
                                     [102.13636096703829, 27.922031126012186],
                                     [102.12874733238306, 27.92533465949343]]]
                }
            }]
        }
    }
    cut = CutProcess(params)
    cut.process(os.getcwd() + "/test.tif")
