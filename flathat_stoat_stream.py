from microprediction.config_private import FLATHAT_STOAT
from microprediction import MicroCrawler
import numpy as np

class FlathatStoatStream(MicroCrawler):

    def __init__(self,write_key):
        super().__init__(stop_loss=2,min_lags=5,sleep_time=20*60,write_key=write_key,quietude=1,verbose=False)

    def candidate_streams(self):
        streams = [name for name, sponsor in self.get_sponsors().items() if "z1" not in name and "z2" not in name and "z3" not in name and "three_body" not in name]
        return streams

    def sample(self, lagged_values, lagged_times=None, **ignored ):
        # weighted average of the last five values
        center = 0.40 * lagged_values[0] \
               + 0.30 * lagged_values[1] \
               + 0.15 * lagged_values[2] \
               + 0.10 * lagged_values[3] \
               + 0.05 * lagged_values[4]
        spread = max(lagged_values[:5]) - min(lagged_values[:5])
        values = [center + 0.2 * spread * s for s in np.random.randn(self.num_predictions) ] 
        return sorted(values)

if __name__=="__main__":
    mw = FlathatStoatStream(write_key=FLATHAT_STOAT)
    mw.run()

