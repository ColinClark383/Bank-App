from fastapi import FastAPI

from controllers.customerController import router as customerRouter
from controllers.accountController import router as accountRouter

app = FastAPI(
    title="Bank API",
    version="1.0.0"
)

app.include_router(customerRouter)
app.include_router(accountRouter)


@app.get("/")
def root():
    return {"message": "Bank API is running"}