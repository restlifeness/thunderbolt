import core
import uvicorn

from fastapi import FastAPI

from thunderbolt.users import auth_router, user_router


settings = core.settings.get_settings()


app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
)

app.include_router(auth_router)
app.include_router(user_router)


def main():
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == '__main__':
    main()
