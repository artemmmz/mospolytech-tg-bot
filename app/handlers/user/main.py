from aiogram import Router

from app.handlers.user.schedule import router as schedule_router

router = Router()
router.include_routers(schedule_router)
