import re
import torch
from torch.nn import functional as F
import string




# lexical items
def lexical(text, tags):

    # father tags
    if "tayta" in text:
        tags.append("<TAG_tayta>")
    if "tata" in text:  
        tags.append("<TAG_tata>")
    if "yaya" in text:
        tags.append("<TAG_yaya>")
    if "papä" in text:
        tags.append("<TAG_papä>")
    if "papa" in text:
        tags.append("<TAG_papa>")
    if "jahua" in text:
        tags.append("<TAG_jahua>")
    if "papá" in text:
        tags.append("<TAG_papá>")
    if "taita" in text:
        tags.append("<TAG_taita>")

    # land tags
    if "allpu" in text:
        tags.append("<TAG_allpu>")
    if "patsa" in text:
        tags.append("<TAG_patsa>")
    if "pacha" in text:
        tags.append("<TAG_pacha>")
    if "alpa" in text:
        tags.append("<TAG_alpa>")
    if "hallp'a" in text:
        tags.append("<TAG_hallp'a>")
    if "allpa" in text:
        tags.append("<TAG_allpa>")
    
    # water tags
    if "yacu" in text:
        tags.append("<TAG_yacu>")
    if "yaku" in text:
        tags.append("<TAG_yaku>")
    if "unu" in text:
        tags.append("<TAG_unu>")
    
    # sun tags
    if "inti" in text:
        tags.append("<TAG_inti>")
    if "indi" in text:
        tags.append("<TAG_indi>")
    if "rupay" in text:
        tags.append("<TAG_rupay>")

    if "quilla" in text:
        tags.append("<TAG_quilla>")
    if "killa" in text:
        tags.append("<TAG_killa>")
    if "kuilla" in text:
        tags.append("<TAG_kuilla>")
    
    # man tags
    if "runa" in text:
        tags.append("<TAG_runa>")
    if "qhari" in text:
        tags.append("<TAG_qhari>")
    if "kari" in text:
        tags.append("<TAG_kari>")
    if "nuna" in text:
        tags.append("<TAG_nuna>")
    if "ollgo" in text:
        tags.append("<TAG_ollgo>")
    if "ullku" in text:
        tags.append("<TAG_ullku>")
    if "qari" in text:
        tags.append("<TAG_qari>")

    return tags  # Return all tags as a single string to be appended to each chunk


def poly(text, tags):

    # list of endings from your data (unique, no repeats)
    endings = [
        "manqui", "masha", "manchi", "chimasha", "shunqui", "shcanqui", "mushcä",
        "mashcanqui", "manquitsu", "mushga", "manga", "munki", "manki", "man",
        "huanqui", "huarca", "cuśhunqui", "chwanpis", "wanki", "wan", "wankichik",
        "wanku", "wankiku", "ki", "sunki", "ykichik", "sunkichik", "wanchej", "yki",
        "ykichej", "wankichis", "ykichis", "ykiku", "sunkiku", "sunkichis", "wankikú",
        "wangi", "washpapis", "wananqa", "wangilla", "shushqa", "ykillapas", "shushpa",
        "shaykillapa", "gangui", "kiga", "huangi", "jun", "chingui", "jpipash",
        "wankungi", "wanka", "rkangi", "murka", "iki", "ikichita", "wankichi", "shkanki",
        "ptiypas", "huaca", "jpis", "rishcami", "canchi", "hua", "huanaun", "cpiga",
        "washka", "ptinika"
    ]
    
    # # Sort endings by length (longest first) to ensure we match the most specific suffix first
    # endings_sorted = sorted(endings, key=len, reverse=True)

    # # Convert text to lowercase if matching should be case-insensitive
    # check_text = text.lower()

    # for ending in endings_sorted:
    #     # We'll also do a case-insensitive check for the suffix
    #     e = ending.lower()
    #     if check_text.endswith(e) and len(check_text) >= (len(e) + 2):
    #         # Tag using the original ending or its lowercase version, whichever you prefer
    #         tags.append(f"<VERB_{ending}>")
    #         print("Flagged word: ", text, " + ", e)
    #         break  # Stop after the first (longest) match

    # return tags
    # Sort endings by length (longest first) for "longest match wins"
    endings_sorted = sorted(endings, key=len, reverse=True)

    # We'll collect all <VERB_> tags from this chunk in a set (to avoid duplicates)
    verb_tags = set()

    # Split the chunk text by whitespace
    words = text.split()

    # For each word in the chunk, strip punctuation from its ends and do suffix matching
    for w in words:
        # Lowercase for case-insensitive matching (adjust if you need exact case)
        lw = w.lower().strip(string.punctuation)

        # Now check if lw ends with any known suffix
        for ending in endings_sorted:
            e = ending.lower()
            # Check: ends with 'e' and is at least 2 chars longer
            if lw.endswith(e) and (len(lw) >= len(e) + 2):
                # If matched, add a tag and break (so we don't also tag shorter suffixes)
                verb_tags.add(f"<VERB_{ending}>")
                # Print for debugging
                # print("Flagged word:", w, "=>", f"<VERB_{ending}>")
                break  # longest match wins for this *one* word

    # Extend the main 'tags' list with all <VERB_> tags found in this chunk
    tags.extend(verb_tags)

    return tags


def preprocess_texts(text):
    text = text.lower()
    # text = strip_punctuation_from_word_ends(text)
    tags = []
    # tags = lexical(text, tags) # no lexical in this version
    tags = poly(text, tags)
    return " ".join(tags)

def strip_punctuation_from_word_ends(text):
    """
    Splits 'text' into words, strips punctuation from
    *both ends* of each word (e.g., commas, periods, semicolons, etc.).
    Joins them back into a single string.
    """
    words = text.split()
    clean_words = []
    for w in words:
        # Strip punctuation on left/right edges only
        clean_w = w.strip(string.punctuation)
        clean_words.append(clean_w)
    return " ".join(clean_words)


def custom_loss(outputs, labels, augmented_features, alpha=0.5):

    # Standard cross-entropy loss for classification
    loss = F.cross_entropy(outputs, labels)
    
    # Additional rule-based penalty
    for idx, features in enumerate(augmented_features):
        if features['has_tata'] and labels[idx] not in [label_dict['quh'], label_dict['qul']]:
            loss += alpha  # Increase loss by a factor when rule is ignored
    return loss


