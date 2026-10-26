from fastapi import APIRouter
from app.routers.redirect import router as redirect_router
from app.routers.v1.data import router as data_router

router = APIRouter()
router.include_router(data_router)
router.include_router(redirect_router)
