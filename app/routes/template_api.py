from fastapi import APIRouter,Depends, Path
import json
from app.schemas import TemplateSubmit
from app.auth import get_current_user # type: ignore

router=APIRouter()

# Return the template.json content
@router.get("/template")
def get_template():
    from pathlib import Path
    template_path = Path(__file__).parent.parent / "app" / "template.json"
    with open(template_path, "r") as f:
        return json.load(f)

# Save submitted template data per user
@router.post("/template")
def submit_template(template_data: TemplateSubmit, user=Depends(get_current_user)):
        submission_path = Path(__file__).parent.parent / "app" / f"submitted_data_{user.username}.json"
        with open(submission_path, "w") as f:
           json.dump(template_data.data, f, indent=4)
           return {"message": "Form submitted", "user": user.username}
