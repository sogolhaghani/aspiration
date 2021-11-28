import pandas as pd
import torch
from torch.utils.data import DataLoader
from _bookdataset import CustomTextDataset
from transformers import DistilBertTokenizerFast


_read_directory = './out/'
_doc = ['Thinking fast and Slow',
'Theories of Personality',
'WHY MEN LOVE Bitches']

_raw_data = pd.read_csv(_read_directory + _doc[0] + '.txt', delimiter = "\t", header=None)
dataset = CustomTextDataset(_raw_data)
train_dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
train_encodings = tokenizer(train_dataloader, truncation=True, padding=True)
