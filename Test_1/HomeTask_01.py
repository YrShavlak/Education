"""HomeTask_01.

# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string
# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# try to run code from pycharm/command line
"""
norway_text = ('Automatisering akselererer %syeblikket da roboter vil'
               ' erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ'))
print(norway_text)
# 1
s1 = 'ø'
s2 = 'å'
s3 = 'Æ'
norway_text = (f'Automatisering akselererer {s1}yeblikket da roboter vil'
               f' erobre planeten v{s2}r. ({s3})')
print(norway_text)
# 2
t1 = 'ø'
t2 = 'å'
t3 = 'Æ'
norway_text = ('Automatisering akselererer {0}yeblikket da roboter vil'
               ' erobre planeten v{1}r. ({2})')
print(norway_text.format(t1, t2, t3))
