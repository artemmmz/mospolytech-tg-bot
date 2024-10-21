from aiogram import Router

from .basic_commands import router as basic_command_router

router = Router()

router.include_routers(basic_command_router)
