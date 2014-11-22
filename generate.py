import sys
from operator import *
from random import shuffle

from utils import *

question_id = int(sys.argv[1])
batch_size = 8
inset_size = 32

#cid, source_id, option_id, text, created_at, updated_at, worker_id, begin, end, creator_id, html, dimension_id, answer_id, answer_used, conductor_sent, question_id, img, video, video_id, vbegin, vend, clip_tag, vote_count, overlap, turker_option_id
data = []
form = ''
for line in dataset(question_id):
    fields = line.strip().split('\t')
    cid, text = fields[0], fields[3]
    data.append((cid, text))

for _ in range(5):
    shuffle(data)

inset, outset = data[:inset_size], data[inset_size:]

for batch_id, batch in enumerate(batches(inset, batch_size)):
    form = ''
    for cid, text in batch:
        form += render('_generate_form', {'clip_id': cid, 'text': text})
    fp = open('render/generate/generate.%s.%s.html' % (question_id, batch_id), 'w')
    print >> fp, render('generate', {'question': question(question_id), 'form': form})
    fp.close()
    
inset = map(itemgetter(0), inset)
outset = map(itemgetter(0), outset)

fp = open('dataset/%s.metadata' % question_id, 'w')
print >> fp, {'inset': inset, 'outset': outset}
fp.close()

