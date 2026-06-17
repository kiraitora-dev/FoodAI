from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Depends

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.user import Token, UserCreate, UserRead
from app.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=201)
async def register(payload: UserCreate, session: DbSession) -> UserRead:
    return await AuthService(session).register(payload)


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: DbSession,
) -> Token:
    service = AuthService(session)
    user = await service.authenticate(form_data.username, form_data.password)
    return service.issue_tokens(user)


@router.get("/me", response_model=UserRead)
async def read_me(current_user: CurrentUser) -> UserRead:
    return current_user
