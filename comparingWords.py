#http://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python

with open('wordlist.txt', 'r') as file1:
    with open('wordlist2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('wordlistcombined.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
