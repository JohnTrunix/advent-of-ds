from typing import Annotated

import httpx
from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from app.config import Settings
from app.dependencies import get_settings

router: APIRouter = APIRouter(prefix="/login")


@router.get("/github-auth")
async def github_auth(settings: Annotated[Settings, Depends(get_settings)]):
    return RedirectResponse(
        f"{settings.OAUTH_AUTHORIZE_URL}?client_id={settings.OAUTH_CLIENT_ID}&scope={settings.OAUTH_SCOPE}",
        status_code=302,
    )


@router.get("/github-code")
async def github_code(
    code: str, settings: Annotated[Settings, Depends(get_settings)]
):
    params: dict[str, str] = {
        "client_id": settings.OAUTH_CLIENT_ID,
        "client_secret": settings.OAUTH_CLIENT_SECRET,
        "code": code,
    }
    headers: dict[str, str] = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=settings.OAUTH_TOKEN_URL, params=params, headers=headers
        )
    response = response.json()
    return RedirectResponse(settings.OAUTH_REDIRECT_URL, status_code=302)
