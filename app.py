import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman
st.set_page_config(page_title="Special Message", page_icon="💖", layout="centered")

# CSS untuk menaikkan posisi konten Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body { background-color: #fff5f5; }

    /* Menghilangkan padding bawaan Streamlit agar bisa lebih mentok ke atas */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Komponen Utama
romantic_html = """
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<div id="main-frame">
    <h1 class="question">Malem minggu jatah ga?</h1>

    <div id="container">
        <div id="button-wrapper">
            <button id="yesBtn" class="btn-style" onclick="celebrate()">Mau!</button>
            <button id="noBtn" class="btn-style" onmouseover="moveButton()" onclick="moveButton()">Gak</button>
        </div>
    </div>
</div>

<style>
    :root {
        --pink-gradient: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
        --rose-red: #ff4b4b;
        --gray-btn: #757575;
    }

    #main-frame {
        text-align: center;
        padding: 50px 20px;
        background: var(--pink-gradient);
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        font-family: 'Quicksand', sans-serif;
        min-height: 450px;
        margin-top: 10px; /* Jarak dari tepi atas */
    }

    .question {
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        color: #880e4f;
        margin-bottom: 20px;
        transition: all 0.5s ease;
    }

    #container {
        height: 300px;
        width: 100%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center; /* Tombol tetap di tengah area container */
    }

    #button-wrapper {
        display: flex;
        gap: 20px;
        justify-content: center;
        align-items: center;
        width: 100%;
    }

    .btn-style {
        width: 120px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-family: 'Quicksand', sans-serif;
    }

    #yesBtn {
        background-color: var(--rose-red);
        color: white;
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
        z-index: 10;
    }

    #noBtn {
        background-color: var(--gray-btn);
        color: white;
        position: relative;
        z-index: 10;
    }
</style>

<script>
    const btnNo = document.getElementById('noBtn');
    const container = document.getElementById('container');
    let isMoved = false;

    function moveButton() {
        if (!isMoved) {
            btnNo.style.position = 'absolute';
            isMoved = true;
        }

        const maxX = container.clientWidth - btnNo.clientWidth;
        const maxY = container.clientHeight - btnNo.clientHeight;

        const randomX = Math.floor(Math.random() * maxX);
        const randomY = Math.floor(Math.random() * maxY);

        btnNo.style.left = randomX + 'px';
        btnNo.style.top = randomY + 'px';
    }

    function celebrate() {
        var end = Date.now() + (5 * 1000);
        var colors = ['#ff4b4b', '#ffb6c1', '#ffffff'];

        (function frame() {
          confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: colors });
          confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: colors });
          if (Date.now() < end) { requestAnimationFrame(frame); }
        }());

        document.querySelector('.question').innerHTML = "Ga Sabar Pulang Nih ❤️";
        btnNo.style.display = 'none';
        document.getElementById('yesBtn').style.transform = 'scale(1.5)';
        document.getElementById('yesBtn').innerHTML = "❤️";
    }
</script>
"""

components.html(romantic_html, height=650)
