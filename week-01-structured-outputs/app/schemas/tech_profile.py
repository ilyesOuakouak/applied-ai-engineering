from pydantic import BaseModel, Field
from typing import List, Optional

class ExtractionRequest(BaseModel):
    raw_text: str = Field(..., min_length=10, description="The unstructured text to be parsed.")

class TechProfile(BaseModel):
    """Encapsulates a software engineer's extracted professional identity."""
    full_name: str = Field(..., description="The candidate's full legal name.")
    programming_languages: List[str] = Field(
        default_factory=list,
        description="Core coding languages (e.g., Python, Go, Rust)."
    )
    years_of_experience: Optional[int] = Field(
        None,
        description="Total years in software industry. Must be an integer."
    )
    current_role: Optional[str] = Field(None, description="Current job title.")
    summary: str = Field(..., description="A concise one-sentence professional summary.")