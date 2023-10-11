# DMG Mori Sentiment Analysis

## Introduction
This project is a part of DMG Mori's Project. The goal of this project is to understand 
the extent to which the crisis has affected the brand reputation. 

## Installation
Requirements:

- Python 3.9+

Setup:
**MacOS**

1. Initialize the virtualEnv
```{bash}
$ pip install virtualenv
$ python3 -m venv .env
```

2. Activate the environment
```{bash}
$ source .env/bin/activate
```

3. Install required libraries
```{bash}
$ pip install --no-cache-dir -r requirements.txt
```

**Windows**

1. Initialize the virtualEnv
```{bash}
$ python3 -m venv .env
```

2. Activate the environment
```{bash}
$ .\.env\Scripts\activate
```

3. Install required libraries
```{bash}
$ pip install --no-cache-dir -r requirements.txt
```

## Details

### Data

The data was collected with respect to the comments that were provided by the public on posts by DMG Mori or posts that mention DMB Mori. 
Channels:
- Facebook
- LinkedIn
- instagram

### Analysis and Prediction
The comment data was used to classify its sentiments and topics. 

The model used(2023): 
- sentiment analysis:  [twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) 
- topic analysis: [cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all)
