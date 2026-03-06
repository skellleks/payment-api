from app.routers.plans import router as plans_router
from app.routers.providers import router as providers_router
from app.routers.payments import router as payments_router

all_routers = [plans_router, providers_router, payments_router]
