<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Ishtiaq Ahmed: AI Systems Engineer and Full-Stack Developer. Machine learning, deep learning, neural networks and LLMs." src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://ishtiaqahmed-portfolio.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-ishtiaqahmed--portfolio-2a78d6?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio"></a>
  <a href="https://linkedin.com/in/ishtiaq-ahmed-90a70b35a"><img src="https://img.shields.io/badge/LinkedIn-Ishtiaq%20Ahmed-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:iashtiaqkhattak@gmail.com"><img src="https://img.shields.io/badge/Email-iashtiaqkhattak%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://wa.me/923354317471?text=Hi%20Ishtiaq%2C%20I%20saw%20your%20GitHub%20and%20would%20like%20to%20discuss%20a%20project."><img src="https://img.shields.io/badge/WhatsApp-Message-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="WhatsApp"></a>
  <img src="https://img.shields.io/badge/Open%20to-remote%20roles%20%26%20contracts-1baf7a?style=flat-square" alt="Open to remote roles and contracts">
</p>

## About me

I build AI systems that hold up outside the notebook: models that are measured honestly, and software around them that runs in production.

- **Neural control:** trained a neural network that flies an entire Falcon 9-class launch and booster landing, every command from liftoff to touchdown, across 10,056 randomised test missions.
- **Biomedical AI:** first author of **CardioFusion-SSL**, a self-supervised model that fuses ECG and heart-sound signals for cardiac screening (AUROC 0.985 under subject-disjoint validation).
- **Production software:** client portals and automations for international clients: multi-tenant React and FastAPI portals, self-hosted n8n WhatsApp workflows, real-time voice AI backends on Azure.
- **Agents and voice:** local-first assistants on Ollama with ChromaDB retrieval and tool use; speaker verification and anti-spoofing face recognition.
- Studying for a **BS in Artificial Intelligence** at IMSciences, Peshawar.

## Featured project

<table>
<tr>
<td width="56%">
<a href="https://github.com/ishtiaq-ahmed-dev/rocket-mission-lab"><img src="https://raw.githubusercontent.com/ishtiaq-ahmed-dev/rocket-mission-lab/master/docs/assets/demo.gif" alt="Rocket Mission Lab: liftoff, stage separation, boostback, entry burn and touchdown" width="100%"></a>
</td>
<td>

### [Rocket Mission Lab](https://github.com/ishtiaq-ahmed-dev/rocket-mission-lab)

A Falcon 9-class launch and return-to-launch-site landing, **flown end to end by a neural network** in the browser. Physics, network and renderer run in one page, with no scripted guidance.

- **1,300 / 1,300** held-out missions completed
- Recovers from forced engine faults in **399 / 400** flights
- Trained by imitation of a predictive teacher with DAgger

`Three.js` `PyTorch` `Node.js` `Imitation learning`

</td>
</tr>
</table>

## More projects

<table>
<tr>
<td width="50%" valign="top">

### [CardioFusion-SSL](https://github.com/ishtiaq-ahmed-dev/CardioFusion-SSL)
Cross-modal self-supervised pretraining and hierarchical fusion of 12-lead ECG and heart-sound (PCG) signals for cardiac screening. Accepts paired, ECG-only or PCG-only input; validated subject-disjoint and on ten external datasets.

**AUROC 0.985 · sensitivity 0.953** (10-fold, subject-disjoint)

`PyTorch` `Contrastive learning` `Biomedical signals`

</td>
<td width="50%" valign="top">

### [FaceGuard AI](https://github.com/ishtiaq-ahmed-dev/faceguard-ai)
Face verification that checks the person is present, not just that the face matches: three independent liveness signals (motion, texture, depth) over a face recogniser, refusing rather than degrading when a check cannot run.

**Anti-spoofing against photo and screen replay attacks**

`Python` `Computer vision` `Security`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Robust Voice Recognition](https://github.com/ishtiaq-ahmed-dev/robust-voice-recognition)
Speaker enrolment, identification and verification on GE2E voice embeddings, with voice-activity detection, calibrated confidence, speaker-disjoint evaluation, a FastAPI service and a live dashboard.

**Noise-robust inference with confidence-scored predictions**

`Python` `FastAPI` `Speech`

</td>
<td width="50%" valign="top">

### ISHTI (private)
A personal, local-first AI assistant: voice in and out, retrieval over personal notes with ChromaDB, and tool-driven agents running on local models through Ollama.

**Runs locally, no cloud dependency**

`Python` `Ollama` `RAG` `Agents`

</td>
</tr>
</table>

Also: C++ data structures and object-oriented programming practice in [DATA_STRUCTURES](https://github.com/ishtiaq-ahmed-dev/DATA_STRUCTURES) and [Cpp-Library](https://github.com/ishtiaq-ahmed-dev/Cpp-Library).

## Professional work

| Project | What I built | Link |
| --- | --- | --- |
| **Startup Consultancy client portal** | Multi-tenant compliance portal for international entrepreneurs (React, FastAPI) | [portal.startupconsultancyofficial.com](https://portal.startupconsultancyofficial.com/) |
| **WhatsApp automation CRM** | Self-hosted n8n workflows for client messaging and follow-up | [startupconsultancyofficial.com](https://startupconsultancyofficial.com/) |
| **JQ AI Solutions** | Company platform and AI services website | [jqaisolutions.com](https://jqaisolutions.com/) |
| **Muslim 360** | Android app, published on Google Play | [Google Play](https://play.google.com/store/apps/details?id=com.foxentech.muslim) |

## Tech stack

| Area | Tools |
| --- | --- |
| **AI and ML** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) ![Deepgram](https://img.shields.io/badge/Deepgram-13EF93?style=flat-square&logo=deepgram&logoColor=black) ![ElevenLabs](https://img.shields.io/badge/ElevenLabs-000000?style=flat-square&logo=elevenlabs&logoColor=white) |
| **Backend and cloud** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black) ![Telnyx](https://img.shields.io/badge/Telnyx-00E599?style=flat-square&logo=telnyx&logoColor=black) ![Sentry](https://img.shields.io/badge/Sentry-362D59?style=flat-square&logo=sentry&logoColor=white) |
| **Frontend** | ![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38BDF8?style=flat-square&logo=tailwindcss&logoColor=white) ![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white) |
| **Automation and tools** | ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white) ![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) |

## GitHub at a glance

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <img alt="GitHub activity over the last 12 months: contributions, commits, public repositories, stars and followers" src="assets/stats-light.svg" width="100%">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/activity-dark.svg">
  <img alt="Contributions per week over the last 12 months" src="assets/activity-light.svg" width="100%">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/languages-dark.svg">
  <img alt="Share of code by language across public repositories" src="assets/languages-light.svg" width="100%">
</picture>

<sub>Generated from the GitHub API by <a href="scripts/profile_stats.py">scripts/profile_stats.py</a> and refreshed daily.</sub>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=ishtiaq-ahmed-dev&color=2a78d6&style=flat-square&label=Profile%20views" alt="Profile views"><br>
  <sub>© 2026 Ishtiaq Ahmed</sub>
</p>
