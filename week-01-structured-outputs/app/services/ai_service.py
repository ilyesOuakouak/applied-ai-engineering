import os
from openai import OpenAI
from app.schemas.tech_profile import TechProfile
from app.core.config import settings

clien = OpenAI(api_key=settings.openai_api_key)

def extract_tech_profile(raw_text: str):
    completion = clien.beta.chat.completions.parse(
        model=settings.model_name,
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical recruiter. Extract professional data accurately."
            },
            {"role": "user", "content": raw_text},
        ],

        response_format=TechProfile,
        #temperature=0.0 #Deterministic output is mandatory for extraction
    )

    return completion.choices[0].message.parsed
