from transformers import BertTokenizer, BertForSequenceClassification

# Load pre-trained model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Example text to classify
text = "I really enjoyed the movie!"

# Tokenize input text
tokens = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# Make a prediction
outputs = model(**tokens)
logits = outputs.logits
predicted_class = logits.argmax().item()

# Print the predicted class
print("Predicted Class:", predicted_class)
