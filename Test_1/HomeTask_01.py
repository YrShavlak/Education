norway_text = 'Automatisering akselererer %syeblikket da roboter vil' \
              ' erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)
# 1
s1 = 'ø'
s2 = 'å'
s3 = 'Æ'
norway_text = f'Automatisering akselererer {s1}yeblikket da roboter vil' \
              f' erobre planeten v{s2}r. ({s3})'
print(norway_text)
# 2
norway_text = 'Automatisering akselererer {}yeblikket da roboter vil' \
              ' erobre planeten v{}r. ({})'
t1 = 'ø'
t2 = 'å'
t3 = 'Æ'
print(norway_text.format(t1, t2, t3))
