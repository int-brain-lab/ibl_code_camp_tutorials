print('Hello World!')
print("Here's something interesting:\n")
# Add lines here, let's make this script do something ineterting!! 

import numpy as np
import time

answer = 0
while answer != 42:
    answer = np.random.choice(100)
    print('The answer to life the universe and everything is %d' % answer)
    time.sleep(0.1)
