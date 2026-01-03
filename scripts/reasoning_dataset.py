# data/reasoning_dataset.py

import re
from datasets import Dataset


def create_dataset(
    path: str = "../data/reasoning_debug_100.txt",
):
    """
    Creates a HuggingFace Dataset from a reasoning .txt file
    structured with <doc>...</doc> blocks.

    Each <doc> block becomes ONE training sample.
    """

    
    with open(path, "r", encoding="utf-8") as f:
        full_text = f.read()

    raw_docs = re.split(r"<doc>\s*|\s*</doc>", full_text)

    # Remove empty blocks
    raw_docs = [d.strip() for d in raw_docs if d.strip()]

    samples = []

    
    for idx, doc in enumerate(raw_docs):

      
        sample = {
            "prompt": doc
        }

        samples.append(sample)

       
        if idx == 0:
            print("RAW PARSED DOC SAMPLE:")
            print(sample["prompt"][:300])
            print("=" * 60)

    
    dataset = Dataset.from_list(samples)

    return dataset
