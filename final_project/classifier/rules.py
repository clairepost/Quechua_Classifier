import re
import torch
from torch.nn import functional as F

# def preprocess_texts(texts):
#     processed_texts = []
#     for text in texts:
#         text_lower = text.lower()
#         if "tata" in text_lower and not "tayta" in text_lower:
#             text += " <TAG_ECUADORIAN>"  # Append a special tag
#         processed_texts.append(text)
#     return processed_texts


def preprocess_texts(text):
    tags = []
    text = text.lower() 

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


    return " ".join(tags)  # Return all tags as a single string to be appended to each chunk




def augment_features(texts):
    augmented_features = []
    for text in texts:
        features = {}
        text_lower = text.lower()
        features['has_tata'] = 1 if "tata" in text_lower and not "tayta" in text_lower else 0
        augmented_features.append(features)
    return augmented_features

def custom_loss(outputs, labels, augmented_features, alpha=0.5):

    # Standard cross-entropy loss for classification
    loss = F.cross_entropy(outputs, labels)
    
    # Additional rule-based penalty
    for idx, features in enumerate(augmented_features):
        if features['has_tata'] and labels[idx] not in [label_dict['quh'], label_dict['qul']]:
            loss += alpha  # Increase loss by a factor when rule is ignored
    return loss


