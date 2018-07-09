import sys

print("Pl Enter Input Data. Terminate with <CNTRL-D>")
print("Example Input from stdin:\n123\n456\nABCD\n")
print("NOTE: To terminate input, Enter <CNTRL-D>, on a new line")

data = sys.stdin.readlines()

print ("Counted", len(data), "lines.")
#Output: Counted 4 lines.

print(data)
#Output: ['123\n', '456\n', 'EOF\n', '\n']
#
##Used to write the session to file
#import readline
#readline.write_history_file('ReadLinesFromStdIn')
