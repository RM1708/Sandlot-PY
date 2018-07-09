import resource
print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
import tensorflow as tf
print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
session = tf.InteractiveSession()
x = tf.constant(list(range(10)))
print(x.eval())
print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
session.close()
print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))

#import sys
#The above was run from the  Python3 command line from the ~ directory
#
#Commands below were used to save the command line interaction
#import readline
#readline.write_history_file('./Sandlot/history')
