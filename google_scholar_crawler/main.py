from scholarly import scholarly
import json
from datetime import datetime, timezone
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = datetime.now(timezone.utc).isoformat()
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
results_dir = os.environ.get('RESULTS_DIR', 'results')
os.makedirs(results_dir, exist_ok=True)
with open(os.path.join(results_dir, 'gs_data.json'), 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(os.path.join(results_dir, 'gs_data_shieldsio.json'), 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print(json.dumps({
    'scholar_id': author['scholar_id'],
    'name': name,
    'citedby': author['citedby'],
    'updated': author['updated'],
}, indent=2))
