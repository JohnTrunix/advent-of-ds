from typing import Annotated

import httpx
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.config import Settings, get_settings
from app.db import crud, schema
from app.dependencies import get_db

router: APIRouter = APIRouter(prefix="/login")


@router.get("/github-auth")
async def github_auth(settings: Annotated[Settings, Depends(get_settings)]):
    return RedirectResponse(
        f"{settings.OAUTH_AUTHORIZE_URL}?client_id={settings.OAUTH_CLIENT_ID}&scope={settings.OAUTH_SCOPE}",
        status_code=302,
    )


@router.get("/github-code")
async def github_code(
    code: str,
    settings: Annotated[Settings, Depends(get_settings)],
    db: Session = Depends(get_db),
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
    token_response = response.json()
    access_token = token_response["access_token"]

    # get scope read:user from github
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://api.github.com/user",
            headers={"Authorization": f"token {access_token}"},
        )
    user_response = response.json()

    # get scope user:email from github
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://api.github.com/user/emails",
            headers={"Authorization": f"token {access_token}"},
        )
    email_response = response.json()

    data = {
        "github_id": str(user_response["id"]),
        "username": user_response["login"],
        "email": email_response[0]["email"],
        "avatar_url": user_response["avatar_url"],
        "profile_url": user_response["html_url"],
        "oauth_token": access_token,
    }

    crud.create_update_user(db, schema.UserCreate(**data))
    return RedirectResponse(settings.OAUTH_REDIRECT_URL, status_code=302)
