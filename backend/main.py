from fastapi import FastAPI
from controllers.customerController import router as customerRouter
from controllers.accountController import router as accountRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Bank API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bank-app-nine-wheat.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customerRouter)
app.include_router(accountRouter)


@app.get("/")
def root():
    return {"message": "Bank API is running"}