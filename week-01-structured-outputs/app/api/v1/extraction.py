from fastapi import APIRouter, HTTPException
from app.schemas.tech_profile import TechProfile, ExtractionRequest
from app.services.ai_service import extract_tech_profile

# Define the router
router = APIRouter()

@router.post("/profile", response_model=TechProfile)
async def get_profile(request: ExtractionRequest):
    """
    Endpoint to transform unstructured text into a validated TechProfile.
    """
    try:
        profile = extract_tech_profile(request.raw_text)
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI Extraction failed. Please check logs.")