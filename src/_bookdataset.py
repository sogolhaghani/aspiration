
from torch.utils.data import Dataset

class CustomTextDataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df
        self.transform = transform

    def __len__(self):
        return len(self.df)
        
    def __getitem__(self, idx):
        text = self.df.loc[[idx]]
        sample = {"text": text, "label": 0}
        return sample