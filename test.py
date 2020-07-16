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
                    "coordinates": [[[102.12903600072963, 27.92310224920098],
                                     [102.12679898877627, 27.915435273652164],
                                     [102.12896821248904, 27.91130206913732],
                                     [102.13039176555009, 27.902316297042447],
                                     [102.14157682531652, 27.900998321042593],
                                     [102.14286480189452, 27.905431449223826],
                                     [102.14381383726982, 27.912500115688403],
                                     [102.1416446135571, 27.919987605951988],
                                     [102.12903600072963, 27.92310224920098]]]
                }
            }]
        }
    }
    cut = CutProcess(params)
    cut.process(os.getcwd() + "/test.tif")
