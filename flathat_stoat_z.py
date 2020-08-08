from microprediction.config_private import FLATHAT_STOAT
from microprediction import MicroCrawler
import numpy as np

class FlathatStoatZ(MicroCrawler):

    def __init__(self,write_key):
        super().__init__(stop_loss=2,sleep_time=20*60,write_key=write_key,quietude=1,verbose=False)

    def candidate_streams(self):
        streams = [name for name, sponsor in self.get_sponsors().items() if name[:2] in ['z1','z2','z3'] and "three_body" not in name]
        return streams

    def sample(self, lagged_values, lagged_times=None, **ignored ):
        """ Fat tails """
        values = [s*(1+0.05*abs(s)) for s in np.random.randn(self.num_predictions - 5) ] 
        for _ in range(5):
            values.append(0)
        return sorted(values)

if __name__=="__main__":
    mw = FlathatStoatZ(write_key=FLATHAT_STOAT)
    mw.run()

