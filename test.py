import unittest

from astropy.coordinates import SkyCoord, EarthLocation
from astropy.coordinates import Angle
from astropy import units as u

import astropy_coordinates as ac
import datetime

def std(s): # returns a numpy.float64, not a u.degree
    return Angle(s).degree

class TestTrackedObject(unittest.TestCase):
    def test_tracked_object(self):
        psh = EarthLocation(lat=40.20412 * u.deg, lon=-76.74238 * u.deg)
        paris = EarthLocation(lat=48.85350 * u.deg, lon=2.34839 * u.deg)
        TO = ac.TrackedObject
        dt = datetime.datetime
        SC = SkyCoord
        object_samples = [
            ('sirius', 1, TO(name='sirius', location=psh), [
                (dt(2023, 11, 3, 20, 0, 0), (std('-62d58m20.9s'), std('325d45m24.2s'))),
                (dt(2023,  5, 3, 10, 0, 0), (std('-64d04m13.3s'), std('028d54m54.4s'))),
                (dt(2017, 11, 3, 20, 0, 0), (std('-63d11m38.7s'), std('326d45m28.5s'))),
                (dt(2017,  5, 3, 15, 0, 0), (std('-11d50m48.7s'), std('102d00m55.0s'))),
                (dt(1975, 11, 3, 10, 0, 0), ( std('31d36m14.6s'), std('196d05m49.3s'))),
                (dt(1975,  6, 3, 19, 0, 0), ( std('33d07m15.0s'), std('178d41m27.1s'))),
            ]),
        ]
        for name, places, tracked_object, samples in object_samples:
            print('Checking {} object'.format(name))
            for time, expected_alt_az in samples:
                print(' at {}'.format(time))
                alt_az = tracked_object.get_alt_az(time)
                alt, az = alt_az.alt.value, alt_az.az.value
                expected_alt, expected_az = expected_alt_az
                self.assertAlmostEqual(alt, expected_alt, places=places)
                self.assertAlmostEqual(az, expected_az, places=places)


if __name__ == '__main__':
    unittest.main()
    
