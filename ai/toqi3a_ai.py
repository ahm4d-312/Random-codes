# ==========================================
# Minimal Character-Level Text Model (No OOP)
# ==========================================
# Requirements:
# pip install torch tqdm

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

# ==========================================
# 1. Load data
# ==========================================
with open("problem_solving.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Get vocabulary
chars = sorted(list(set(text)))
vocab_size = len(chars)

# Create lookup tables
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}


def encode(s):  # string -> list of ints
    return [stoi[c] for c in s]


def decode(indices):  # list of ints -> string
    return "".join([itos[i] for i in indices])


data = torch.tensor(encode(text), dtype=torch.long)

# Train/validation split
n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]

# ==========================================
# 2. Make batch function
# ==========================================
block_size = 64
batch_size = 32


def get_batch(split):
    source = train_data if split == "train" else val_data
    ix = torch.randint(len(source) - block_size, (batch_size,))
    x = torch.stack([source[i : i + block_size] for i in ix])
    y = torch.stack([source[i + 1 : i + block_size + 1] for i in ix])
    return x, y


# ==========================================
# 3. Initialize parameters manually
# ==========================================
hidden_size = 128

# Layers
embedding = nn.Embedding(vocab_size, hidden_size)
lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
linear = nn.Linear(hidden_size, vocab_size)

# Send to device (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
embedding, lstm, linear = embedding.to(device), lstm.to(device), linear.to(device)

# Optimizer
optimizer = optim.AdamW(
    list(embedding.parameters()) + list(lstm.parameters()) + list(linear.parameters()),
    lr=1e-3,
)


# ==========================================
# 4. Forward pass (no class)
# ==========================================
def forward(x, targets=None):
    x = embedding(x)
    out, _ = lstm(x)
    logits = linear(out)
    loss = None
    if targets is not None:
        loss = nn.functional.cross_entropy(
            logits.view(-1, vocab_size), targets.view(-1)
        )
    return logits, loss


# ==========================================
# 5. Training loop
# ==========================================
for epoch in range(10):
    total_loss = 0
    for _ in tqdm(range(300)):
        xb, yb = get_batch("train")
        xb, yb = xb.to(device), yb.to(device)

        optimizer.zero_grad()
        _, loss = forward(xb, yb)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/300:.4f}")


# ==========================================
# 6. Text generation (manual)
# ==========================================
def generate(start_char=" ", length=400):
    context = torch.tensor([[stoi[start_char]]], dtype=torch.long, device=device)
    generated = [stoi[start_char]]
    hidden = None

    for _ in range(length):
        x = embedding(context)
        out, hidden = lstm(x, hidden)
        logits = linear(out[:, -1, :])
        probs = torch.softmax(logits, dim=-1)
        next_id = torch.multinomial(probs, num_samples=1)
        generated.append(next_id.item())
        context = next_id.unsqueeze(0)

    return decode(generated)


# ==========================================
# 7. Generate text
# ==========================================
print("\n--- Generated Text ---")
print(generate("t", 400))
