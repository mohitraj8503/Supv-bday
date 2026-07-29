<div align="center">

# 🎈 Happy Birthday Jiya | Widescreen & Mobile Experience

### A Premier 16:9 Widescreen & Mobile Birthday Celebration Web Application

[![HTML5: Valid](https://img.shields.io/badge/HTML5-Semantic-orange?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3: Premium](https://img.shields.io/badge/Styling-Premium%20Vanilla%20CSS-blue?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript: ES6+](https://img.shields.io/badge/Logic-Vanilla%20JS-yellow?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Deployment: GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages-brightgreen?style=for-the-badge&logo=githubpages&logoColor=white)](https://mohitraj8503.github.io/Supv-bday/)

**Happy Birthday Jiya** is a custom, high-fidelity 16:9 widescreen and mobile-optimized birthday web application built with AI background matting, glassmorphism UI, interactive audio synthesis, direct WhatsApp wish routing, and real-time confetti physics.

[Live Demo](https://mohitraj8503.github.io/Supv-bday/) • [Key Features](#-key-features) • [Tech Architecture](#-technology-stack) • [GitHub Pages Deployment](#-github-pages-deployment)

---

</div>

## ✨ End-to-End Experience Architecture

The application combines high-performance frontend animations with deep AI background extraction for a seamless experience across desktop monitors and mobile smartphones.

```mermaid
graph TD
    A[Original Subject Photo] --> B[ISNet Deep AI Matting]
    B --> C[Zero-Edge Cosine Alpha Decay]
    C --> D[16:9 Widescreen & Mobile Responsive Canvas]
    D --> E[Interactive Floating Orbs & Light Halo]
    D --> F[Direct WhatsApp Wish Integration]
    D --> G[Web Audio Melody & Confetti Physics]
```

---

## 🚀 Key Features

* 🖼️ **AI Deep Background Matting**: Uses the ISNet neural segmentation model with zero-edge cosine alpha decay to cleanly extract the portrait with zero white halos or hair artifacts.
* 📺 **16:9 Full-Bleed Widescreen**: Designed to fill 100% of desktop viewports in standard 16:9 ratio (`100vw x 100vh`) with soft ambient light halos and glassmorphism cards.
* 📱 **Mobile Smartphone First**: Fully responsive layout tailored for phone users (`< 768px`) with smooth touch scrolling, centered subject showcase, and full-width touch targets.
* 🎈 **Festive Asset Integration**: Includes interactive 3D birthday cake (`cake.svg`), hanging bunting garland (`banner.png`), and balloon border overlay (`Balloon-Border.png`).
* 📲 **Direct WhatsApp Wish Routing**: Visitors can write custom wishes in the "Send a Wish" modal, which directly opens WhatsApp pre-filled for `+91 86769 92907`.
* 🎵 **Audio Synthesis & Confetti**: Integrates background music playback (`music.mp3`) with Web Audio API fallback synthesizer and real-time canvas confetti explosions.

---

## 🛠️ Technology Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend Core** | HTML5 / JavaScript (ES6+) | Semantic layout and modular interactive event handlers |
| **Styling & Motion** | Vanilla CSS3 / Glassmorphism | Custom CSS tokens, fluid typography (`clamp()`), and GPU-accelerated keyframe animations |
| **Image AI Processing** | Python 3 / `rembg` (ISNet) / PIL | Deep neural net matting with cosine alpha edge blending |
| **Audio Engine** | Web Audio API / HTML5 Audio | Dual background music player with live equalizer bar animation |
| **Effects & Physics** | `canvas-confetti` Library | Particle explosion physics on page load, cake clicks, and wish submissions |

---

## 🌐 GitHub Pages Deployment

To deploy this project to GitHub Pages:

1. **Set Up Remote Repository**:
   ```bash
   git remote add origin https://github.com/mohitraj8503/Supv-bday.git
   git branch -M main
   git push -u origin main --force
   ```

2. **Enable GitHub Pages**:
   - Go to [mohitraj8503/Supv-bday Settings](https://github.com/mohitraj8503/Supv-bday/settings/pages).
   - Under **Build and deployment** -> **Source**, select **Deploy from a branch**.
   - Choose Branch: `main` and Folder: `/ (root)`.
   - Click **Save**.

Your birthday website will be live at: **[https://mohitraj8503.github.io/Supv-bday/](https://mohitraj8503.github.io/Supv-bday/)** 🎉
