from aiogram import Router

from app.handlers.admin import admin_router
from app.handlers.other import other_router
from app.handlers.user import user_router

router = Router()
router.include_routers(admin_router, user_router, other_router)
