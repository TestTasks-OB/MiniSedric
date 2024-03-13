from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.core.config import get_app_settings 
from src.api.routes.main import router as api_router 
from src.core.settings.env import ENV_PATH
from dotenv import load_dotenv
from loguru import logger 
 
def get_application() -> FastAPI:

    load_dotenv(ENV_PATH)

    settings = get_app_settings()

    settings.configure_logging()    
    settings.configure_env() 
    logger.info(settings.app_env)
    application = FastAPI(**settings.fastapi_kwargs)
 
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )   
    application.include_router(api_router)

    return application


app = get_application() 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)