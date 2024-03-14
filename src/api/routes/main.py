from fastapi import APIRouter

from src.api.routes.interaction import router as interactions_router

router = APIRouter()
router.include_router(interactions_router) 