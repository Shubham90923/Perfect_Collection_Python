import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import (
    init_db,
    get_all_products,
    get_product_by_id,
    update_stock,
    create_order,
    get_all_orders
)

# Initialize SQLite database
init_db()

app = Flask(__name__)

# Storefront Home Page
@app.route("/")
def home():
    category = request.args.get("category")
    search = request.args.get("search")
    max_price = request.args.get("max_price")
    products = get_all_products(category=category, search=search, max_price=max_price)
    return render_template("index.html",
                           products=products,
                           current_category=category,
                           current_search=search)

# Product Detail Page
@app.route("/product/<product_id>")
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return redirect(url_for("home"))
    return render_template("product_detail.html", product=product)

# Video Reels / TikTok Showcase
@app.route("/reels")
def reels_view():
    products = get_all_products()
    return render_template("reels.html", products=products)

# Staff & Admin Inventory Portal
@app.route("/admin")
def admin_portal():
    products = get_all_products()
    orders = get_all_orders()
    return render_template("admin.html", products=products, orders=orders)

# Stock Status Update Action
@app.route("/admin/update-stock", methods=["POST"])
def update_product_stock():
    product_id = request.form.get("product_id")
    status = request.form.get("status")
    count = int(request.form.get("count", 0))
    update_stock(product_id, status, count)
    return redirect(url_for("admin_portal"))

# JSON API for Products
@app.route("/api/products")
def api_products():
    category = request.args.get("category")
    return jsonify(get_all_products(category=category))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Run locally on 127.0.0.1:5000
    app.run(host="127.0.0.1", port=port, debug=True)
