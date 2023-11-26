from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database.connector import engine
from app import schemas
from app.api.endpoints import organization_endpoint, user_endpoint, role_endpoint, action_endpoint, rule_endpoint, user_role_organization_endpoint

app = FastAPI(encoding="utf-8")
app.include_router(organization_endpoint.router)
app.include_router(user_endpoint.router)
app.include_router(role_endpoint.router)
app.include_router(action_endpoint.router)
app.include_router(rule_endpoint.router)
app.include_router(user_role_organization_endpoint.router)

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

[base.metadata.create_all(bind=engine) for base in schemas.Base]

@app.get("/")
def root():
  return {"message": "Server is running..."}