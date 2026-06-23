from flask import Flask
import time

app = Flask(__name__)

# Simulasi database
database = {
    "produk": "Laptop Asus AsusVivoBook"
}

# Simulasi cache
cache = {}

@app.route("/produk")
def get_produk():

    # Cek cache terlebih dahulu
    if "produk" in cache:
        return f"""
        <div style="font-family:Arial; text-align:center; margin-top:50px;">
            <h1 style="color:green;">✅ CACHE HIT</h1>
            <h2>{cache['produk']}</h2>
            <p>Data diambil dari cache</p>
            <p><b>Waktu akses:</b> Sangat Cepat</p>
        </div>
        """

    # Simulasi akses database
    time.sleep(3)

    data = database["produk"]

    # Simpan ke cache
    cache["produk"] = data

    return f"""
    <div style="font-family:Arial; text-align:center; margin-top:50px;">
        <h1 style="color:orange;">⚠️ CACHE MISS</h1>
        <h2>{data}</h2>
        <p>Data diambil dari database</p>
        <p>Data kemudian disimpan ke cache</p>
    </div>
    """

@app.route("/clear-cache")
def clear_cache():
    cache.clear()
    return """
    <div style="font-family:Arial; text-align:center; margin-top:50px;">
        <h1 style="color:red;">🗑️ Cache Berhasil Dihapus</h1>
        <p>Silakan akses kembali <b>/produk</b> untuk melihat Cache Miss.</p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)