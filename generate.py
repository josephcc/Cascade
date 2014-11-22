import sys
from random import shuffle

from utils import *

question_id = int(sys.argv[1])
batch_size = 8
init_set_size = 32

#cid, source_id, option_id, text, created_at, updated_at, worker_id, begin, end, creator_id, html, dimension_id, answer_id, answer_used, conductor_sent, question_id, img, video, video_id, vbegin, vend, clip_tag, vote_count, overlap, turker_option_id
data = []
form = ''
for line in dataset(question_id):
    fields = line.strip().split('\t')
    cid, text = fields[0], fields[3]
    data.append((cid, text))

for _ in range(5):
    shuffle(data)

data = data[:init_set_size]

for batch_id, batch in enumerate(batches(data, batch_size)):
    form = ''
    for cid, text in batch:
        form += render('_generate_form', {'clip_id': cid, 'text': text})
    fp = open('render/generate/generate.%s.%s.html' % (question_id, batch_id), 'w')
    print >> fp, render('generate', {'question': question(102), 'form': form})
    fp.close()
    

