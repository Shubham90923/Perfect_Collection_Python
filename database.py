import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "boutique.db")

INITIAL_PRODUCTS = [
    {
        "id": "pc-suit-101",
        "code": "PC-ST-101",
        "name": "Gulabi Zardozi Chanderi Silk Suit Set",
        "category": "suits",
        "sub_category": "Heavy Work Suits",
        "price": 6850,
        "original_price": 8500,
        "fabric": "Pure Chanderi Silk with Santoon Lining & Organza Dupatta",
        "work_type": "Handcrafted Zardozi, Golden Gota Patti & Moti Work",
        "neckline_detail": "Regal Sweetheart Neckline framed with intricate dabka & pearl embroidery",
        "stock_status": "in_stock",
        "stock_count": 5,
        "is_featured": 1,
        "colors": json.dumps([
            {"colorName": "Gulabi Rose Pink", "colorHex": "#e06b88"},
            {"colorName": "Champagne Gold", "colorHex": "#e2ba7d"},
            {"colorName": "Emerald Green", "colorHex": "#1b4d3e"}
        ]),
        "sizes": json.dumps(["Unstitched", "S", "M", "L", "XL", "XXL"]),
        "images": json.dumps([
            "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=1000&q=80"
        ]),
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-fashion-model-in-an-ethnic-dress-41399-large.mp4",
        "description": "A masterpiece created for festive occasions and wedding celebrations. Features an ornate neckline with genuine dabka and pearls.",
        "included_pieces": "Full Embroidered Kurti (3m), Trouser Fabric (2.5m), Organza Dupatta (2.4m)"
    },
    {
        "id": "pc-suit-102",
        "code": "PC-ST-102",
        "name": "Noor Emerald Velvet Winter Suit",
        "category": "suits",
        "sub_category": "Heavy Work Suits",
        "price": 9200,
        "original_price": 11500,
        "fabric": "Micro 9000 Royal Velvet with Embroidered Silk Dupatta",
        "work_type": "Tilla Kashmiri Embroidery & Antique Zari Border",
        "neckline_detail": "Band Collar V-Slit with dense antique gold Kashmiri tilla handwork",
        "stock_status": "in_stock",
        "stock_count": 3,
        "is_featured": 1,
        "colors": json.dumps([
            {"colorName": "Royal Emerald", "colorHex": "#084c38"},
            {"colorName": "Wine Burgundy", "colorHex": "#58111a"}
        ]),
        "sizes": json.dumps(["Unstitched", "M", "L", "XL"]),
        "images": json.dumps([
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=1000&q=80"
        ]),
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-young-woman-in-a-luxurious-gown-41395-large.mp4",
        "description": "Rich, plush Micro 9000 Velvet tailored to perfection. Shimmers under Rupandehi evening receptions.",
        "included_pieces": "Velvet Top, Velvet Bottom, Heavy Silk Dupatta"
    },
    {
        "id": "pc-lehenga-201",
        "code": "PC-LH-201",
        "name": "Shahi Dulhan Crimson Bridal Lehenga",
        "category": "lehengas",
        "sub_category": "Bridal Lehengas",
        "price": 32500,
        "original_price": 38000,
        "fabric": "Raw Silk with Double Can-Can Layering & Dual Dupattas",
        "work_type": "Heavy Cutwork Border, Zardozi, Kundan Stone & Marodi",
        "neckline_detail": "Deep Royal Cut Blouse with Embroidered Latkan Back Dori",
        "stock_status": "in_stock",
        "stock_count": 2,
        "is_featured": 1,
        "colors": json.dumps([
            {"colorName": "Sindoor Crimson", "colorHex": "#9f1239"}
        ]),
        "sizes": json.dumps(["Semi-Stitched", "Custom Tailored"]),
        "images": json.dumps([
            "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=1000&q=80"
        ]),
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-young-woman-in-a-luxurious-gown-41395-large.mp4",
        "description": "Quintessential Nepali wedding bridal set with over 160 hours of artisanal handwork on raw silk.",
        "included_pieces": "Semi-Stitched Lehenga (5m Flare), Blouse Piece, Dual Heavy Dupattas"
    },
    {
        "id": "pc-saree-301",
        "code": "PC-SR-301",
        "name": "Devdaha Heritage Katan Banarasi Silk Saree",
        "category": "sarees",
        "sub_category": "Silk Sarees",
        "price": 11800,
        "original_price": 14500,
        "fabric": "Pure Katan Weave Silk with Pure Gold Zari Pallu",
        "work_type": "Traditional Kadwa Weave with Floral Jaal & Royal Minakari",
        "neckline_detail": "Includes unstitched heavy brocade blouse fabric for custom neckline tailoring",
        "stock_status": "in_stock",
        "stock_count": 6,
        "is_featured": 1,
        "colors": json.dumps([
            {"colorName": "Royal Vermillion Red", "colorHex": "#be123c"},
            {"colorName": "Peacock Blue", "colorHex": "#0e7490"}
        ]),
        "sizes": json.dumps(["Free Size (6.3m with Blouse Piece)"]),
        "images": json.dumps([
            "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=1000&q=80"
        ]),
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-woman-modeling-a-traditional-indian-dress-41396-large.mp4",
        "description": "Timeless heirloom piece woven with pure gold zari. Perfect for Dashain, Tihar, and wedding rituals.",
        "included_pieces": "5.5m Pure Katan Silk Saree + 0.8m Brocade Blouse Piece"
    },
    {
        "id": "pc-anarkali-401",
        "code": "PC-AK-401",
        "name": "Mumtaz Floor-Length Royal Angrakha Anarkali",
        "category": "anarkalis",
        "sub_category": "Royal Floor Length",
        "price": 13500,
        "original_price": 16200,
        "fabric": "Heavy Chinon Silk with Shantoon Lining & Net Dupatta",
        "work_type": "Antique Dabka, Pearl Motifs & 28-Kali Kalidar Flare",
        "neckline_detail": "Crossover Angrakha Neckline adorned with handmade silk dori tassels",
        "stock_status": "in_stock",
        "stock_count": 3,
        "is_featured": 1,
        "colors": json.dumps([
            {"colorName": "Rani Pink & Gold", "colorHex": "#be185d"},
            {"colorName": "Mor-Pankhi Teal", "colorHex": "#0f766e"}
        ]),
        "sizes": json.dumps(["Unstitched", "S", "M", "L", "XL"]),
        "images": json.dumps([
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=1000&q=80"
        ]),
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-fashion-model-in-an-ethnic-dress-41399-large.mp4",
        "description": "28-kali sweep that flows majestically. Angrakha overlap neckline decorated with rich antique dabka.",
        "included_pieces": "Anarkali Gown, Churidar Bottom, 2.5m Heavy Dupatta"
    }
]

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY,
        code TEXT UNIQUE,
        name TEXT,
        category TEXT,
        sub_category TEXT,
        price INTEGER,
        original_price INTEGER,
        fabric TEXT,
        work_type TEXT,
        neckline_detail TEXT,
        stock_status TEXT,
        stock_count INTEGER,
        is_featured INTEGER,
        colors TEXT,
        sizes TEXT,
        images TEXT,
        video_url TEXT,
        description TEXT,
        included_pieces TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id TEXT PRIMARY KEY,
        order_number TEXT UNIQUE,
        customer_name TEXT,
        phone TEXT,
        city TEXT,
        address TEXT,
        stitching_notes TEXT,
        payment_method TEXT,
        subtotal INTEGER,
        delivery_fee INTEGER,
        total INTEGER,
        items_json TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

    # Populate initial products if empty
    cursor.execute("SELECT COUNT(*) as count FROM products")
    if cursor.fetchone()["count"] == 0:
        for p in INITIAL_PRODUCTS:
            cursor.execute("""
            INSERT INTO products (
                id, code, name, category, sub_category, price, original_price,
                fabric, work_type, neckline_detail, stock_status, stock_count,
                is_featured, colors, sizes, images, video_url, description, included_pieces
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                p["id"], p["code"], p["name"], p["category"], p["sub_category"],
                p["price"], p["original_price"], p["fabric"], p["work_type"],
                p["neckline_detail"], p["stock_status"], p["stock_count"],
                p["is_featured"], p["colors"], p["sizes"], p["images"],
                p["video_url"], p["description"], p["included_pieces"]
            ))
        conn.commit()
    conn.close()

def get_all_products(category=None, search=None, max_price=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if category and category != 'all':
        query += " AND category = ?"
        params.append(category)

    if search:
        query += " AND (name LIKE ? OR code LIKE ? OR neckline_detail LIKE ? OR fabric LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term, term])

    if max_price:
        query += " AND price <= ?"
        params.append(int(max_price))

    query += " ORDER BY is_featured DESC, price ASC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    result = []
    for r in rows:
        d = dict(r)
        d["colors"] = json.loads(d["colors"])
        d["sizes"] = json.loads(d["sizes"])
        d["images"] = json.loads(d["images"])
        result.append(d)
    conn.close()
    return result

def get_product_by_id(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    d = dict(row)
    d["colors"] = json.loads(d["colors"])
    d["sizes"] = json.loads(d["sizes"])
    d["images"] = json.loads(d["images"])
    return d

def update_stock(product_id, status, count):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock_status = ?, stock_count = ? WHERE id = ?", (status, count, product_id))
    conn.commit()
    conn.close()

def create_order(customer_name, phone, city, address, stitching_notes, payment_method, subtotal, delivery_fee, total, items):
    import random
    order_number = f"PC-{random.randint(100000, 999999)}"
    order_id = f"ord-{order_number}"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO orders (
        id, order_number, customer_name, phone, city, address,
        stitching_notes, payment_method, subtotal, delivery_fee,
        total, items_json, status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id, order_number, customer_name, phone, city, address,
        stitching_notes, payment_method, subtotal, delivery_fee,
        total, json.dumps(items), "confirmed" if payment_method == 'cod' else "pending_whatsapp"
    ))
    conn.commit()
    conn.close()
    return order_number

def get_all_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    rows = cursor.fetchall()
    result = []
    for r in rows:
        d = dict(r)
        d["items"] = json.loads(d["items_json"])
        result.append(d)
    conn.close()
    return result
