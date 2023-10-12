import numpy as np
from scipy.special import softmax
from googletrans import Translator
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class SentimentModel:
    def __init__(self) -> None:
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.config = AutoConfig.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.translator = Translator()

    def _token_resize(self, encoded_input):
        if encoded_input["input_ids"].shape[1] > 512:
            for key, value in encoded_input.items():
                value = value[:, :512]
                encoded_input[key] = value
            return encoded_input
        else:
            return encoded_input

    def _text_to_token(self, text):
        return self.tokenizer(text, return_tensors="pt")

    def _preprocessing(self, text: str):
        text = self._translate(text=text)
        encoded_input = self._text_to_token(text=text)
        encoded_input = self._token_resize(encoded_input=encoded_input)
        return encoded_input

    def _translate(self, text):
        return self.translator.translate(text).text

    def _compute_scores(self, model_output):
        scores = model_output[0][0].detach().numpy()
        return softmax(scores)

    def _get_all_scores(self, scores):
        score_dict = {}
        for i, score in enumerate(scores):
            score_dict[self.config.id2label[i]] = score

        return score_dict

    def _get_best_score(self, scores):
        ranking = np.argsort(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        sentiment = self.config.id2label[ranking[0]]
        return {"sentiment": sentiment, "score": scores[ranking[0]]}

    def get_sentiment_prediction(self, text, best_score: bool = False):
        encoded_input = self._preprocessing(text=text)
        output = self.model(**encoded_input)
        scores = self._compute_scores(model_output=output)

        if best_score:
            return self._get_best_score(scores=scores)
        else:
            return self._get_all_scores(scores=scores)
