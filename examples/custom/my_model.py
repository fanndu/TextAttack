import transformers

import textattack

model_path = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = transformers.DistilBertTokenizer.from_pretrained(model_path)
model = transformers.DistilBertForSequenceClassification.from_pretrained(model_path)

model = textattack.models.wrappers.HuggingFaceModelWrapper(model, tokenizer)

# you can move dataset to new file and use it as a custom dataset
dataset = textattack.datasets.HuggingFaceDataset(
    "glue", subset="sst2", split="train", shuffle=False
)

