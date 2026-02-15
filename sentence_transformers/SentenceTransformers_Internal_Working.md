# SentenceTransformers -- Internal Working Explained

## 1. Model Initialization

When running:

``` python
model = SentenceTransformer('all-MiniLM-L6-v2')
```

The library checks whether the model exists locally inside:

    C:\Users\<username>\.cache\huggingface\hub\

If not found, it downloads the model from Hugging Face Hub.

Downloaded files include: - modules.json - config.json -
model.safetensors (model weights) - tokenizer files (vocab.txt,
tokenizer.json)

------------------------------------------------------------------------

## 2. Windows Symlink Warning

Hugging Face uses symbolic links (symlinks) to save disk space.

On Windows, symlinks require: - Developer Mode enabled, OR - Running
Python as Administrator

If not enabled, caching still works but may use more disk space.

This is only a warning, not an error.

------------------------------------------------------------------------

## 3. Model Weights Loading

File:

    model.safetensors (about 90MB)

This contains neural network parameters.

The model used (`all-MiniLM-L6-v2`) is: - MiniLM transformer - 6
transformer layers - Outputs 384-dimensional embeddings

After downloading, weights are loaded into memory.

------------------------------------------------------------------------

## 4. Tokenizer Loading

Files: - vocab.txt - tokenizer.json - special_tokens_map.json

Before text enters the model:

1.  Text is split into tokens
2.  Tokens are converted to token IDs
3.  IDs are passed to the transformer

------------------------------------------------------------------------

## 5. Embedding Generation Pipeline

When calling:

``` python
embeddings = model.encode(sentences)
```

Internally:

Text\
↓\
Tokenizer\
↓\
Token IDs\
↓\
MiniLM Transformer\
↓\
Mean Pooling\
↓\
384-Dimensional Sentence Vector

Each sentence becomes a vector of size:

    (384,)

For 3 sentences:

    (3, 384)

------------------------------------------------------------------------

## 6. Similarity Calculation

You computed similarity using:

``` python
np.dot(embeddings[0], embeddings[1])
```

Since SentenceTransformers normalizes embeddings by default, dot product
≈ cosine similarity.

That is why the output makes semantic sense:

-   Dogs vs Pets → High similarity (\~62%)
-   Dogs vs Remote → Low similarity (\~33%)
-   Pets vs Remote → Low similarity (\~29%)

The model understands meaning, not just matching words.

------------------------------------------------------------------------

## 7. What Happens on Second Run

After first download: - Model loads from local cache - No re-download -
Faster execution

------------------------------------------------------------------------

## 8. Recommended Similarity Method

Instead of using `np.dot`, better practice:

``` python
from sentence_transformers import util
util.cos_sim(embeddings[0], embeddings[1])
```

This ensures correct cosine similarity computation.

------------------------------------------------------------------------

# Final Summary

Your pipeline:

Text → Tokenizer → Transformer → Mean Pooling → 384D Vector → Similarity
Score

This is the foundation of: - Semantic Search - Chatbots - Document
Retrieval - Vector Databases - RAG Systems

You now understand what happens internally when generating sentence
embeddings.
