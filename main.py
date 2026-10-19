import os
from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from database import (
    init_db,
    get_all_products,
    get_product_by_id,
    update_stock,
    create_order,
    get_all_orders
)

# Initialize database
init_db()

app = FastAPI(title="Perfect Collection API & Storefront", description="Devdaha -1, Rupandehi Women's Ethnic Boutique")

BASE_DIR = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Storefront Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, category: str = Query(None), search: str = Query(None), max_price: int = Query(None)):
    products = get_all_products(category=category, search=search, max_price=max_price)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products,
        "current_category": category,
        "current_search": search
    })

# Product Detail Page
@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: str):
    product = get_product_by_id(product_id)
    if not product:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("product_detail.html", {
        "request": request,
        "product": product
    })

# Video Reels / TikTok Showcase
@app.get("/reels", response_class=HTMLResponse)
async def reels_view(request: Request):
    products = get_all_products()
    return templates.TemplateResponse("reels.html", {
        "request": request,
        "products": products
    })

# Staff & Admin Inventory Portal
@app.get("/admin", response_class=HTMLResponse)
async def admin_portal(request: Request):
    products = get_all_products()
    orders = get_all_orders()
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "products": products,
        "orders": orders
    })

# Stock Status Update Action
@app.post("/admin/update-stock")
async def update_product_stock(product_id: str = Form(...), status: str = Form(...), count: int = Form(...)):
    update_stock(product_id, status, count)
    return RedirectResponse(url="/admin", status_code=303)

# JSON API for Products
@app.get("/api/products")
async def api_products(category: str = None):
    return get_all_products(category=category)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
