import os
from litellm import completion
import pandas as pd
from pydantic import BaseModel

class FaithfulnessVerdict(BaseModel):
    reasoning: str
    verdict: Literal["Faithful", "Hallucinated"]
    score: int #1 to 5

def judge_faithfulness(question: str, answer: str) -> FaithfulnessVerdict:
    prompt = f"""
    You are a helpful assistant that judges the faithfulness of an answer to a question.
    You will be given a question and an answer.
    You need to judge the faithfulness of the answer to the question.
    The answer is faithful if it is a direct answer to the question.
    The answer is hallucinated if it is not a direct answer to the question.
    The score is a number between 1 and 5, where 1 is the lowest and 5 is the highest.
    """


