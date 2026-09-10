from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.media_fact_checker_verifier.schemas import AgenticMediaFactCheckerVerifierSessionCreate, AgenticMediaFactCheckerVerifierSessionResponse
from app.domain.media_fact_checker_verifier.service import AgenticMediaFactCheckerVerifierService

router = APIRouter(prefix="/api/v1/media_fact_checker_verifier", tags=["Agentic Media Fact Checker Verifier Domain"])

@router.post("/sessions", response_model=AgenticMediaFactCheckerVerifierSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticMediaFactCheckerVerifierSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Media Fact Checker Verifier.
    """
    return AgenticMediaFactCheckerVerifierService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticMediaFactCheckerVerifierSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticMediaFactCheckerVerifierService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
