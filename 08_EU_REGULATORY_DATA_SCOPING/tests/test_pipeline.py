import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('cli',ROOT/'scripts'/'cli.py')
cli=importlib.util.module_from_spec(spec)
spec.loader.exec_module(cli)

class ProjectTests(unittest.TestCase):
 def test_seed_inventory_count(self):
  with (ROOT/'inputs'/'seed_inventory_v0_1.csv').open(encoding='utf-8-sig',newline='') as f:records=list(csv.DictReader(f))
  self.assertEqual(len(records),41)
  self.assertEqual(len({r['source_seed_id'] for r in records}),41)
  self.assertTrue(all(r['source_url'] for r in records))
 def test_data_headers(self):
  for table,expected in cli.SCHEMA.items():
   with (ROOT/'data'/table).open(encoding='utf-8-sig',newline='') as f:
    self.assertEqual(next(csv.reader(f)),expected)
 def test_cohen_kappa(self):
  records=[{'record_id':'1','reviewer':'A','decision':'include'},{'record_id':'1','reviewer':'B','decision':'include'},
           {'record_id':'2','reviewer':'A','decision':'exclude'},{'record_id':'2','reviewer':'B','decision':'exclude'}]
  k=cli.kappa_or_na(records)
  self.assertEqual(k['n'],2)
  self.assertEqual(k['kappa'],1.0)
 def test_canonical_dataset_ids_are_unique(self):
  ids=[r['dataset_id'] for r in cli.read_table('datasets.csv')]
  self.assertEqual(len(ids),len(set(ids)))

if __name__=='__main__':unittest.main()
