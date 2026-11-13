# Hey, I'm Divyansh 👋

<img align="right" src="./assets/temporal-desk.gif" width="340" alt="Pixel desk: a monitor shows hyperedges appearing and expiring along a timeline"/>

### Building time-aware memory for LLMs.

<p><em>
  Creator of <a href="https://github.com/Divyansh151005/Temporal-Hypergraph-Engine"><b>Temporal Hypergraph Engine</b></a>
</em></p>

[![Live demo](https://img.shields.io/badge/Live_demo-Temporal_Hypergraph-1e293b?style=flat-square&logo=render&logoColor=white)](https://temporal-hypergraph-web.onrender.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-divyansh--barodiya-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/divyansh-barodiya/)
[![Email](https://img.shields.io/badge/Email-2023csb1119@iitrpr.ac.in-475569?style=flat-square&logo=gmail&logoColor=white)](mailto:2023csb1119@iitrpr.ac.in)
[![IEEE](https://img.shields.io/badge/IEEE-DualCare-00629B?style=flat-square&logo=ieee&logoColor=white)](https://ieeexplore.ieee.org/document/11575533)

<br clear="right"/>

---

### ⚡ Flagship — Temporal Hypergraph Engine

A lock-free, SIMD-accelerated **temporal hypergraph** database in Rust that stores facts as time-bounded hyperedges, so LLM retrieval only follows facts that were true at the moment asked — with a zero-copy **vLLM KV-cache** block store alongside.
[Live site](https://temporal-hypergraph-web.onrender.com/) · [Repository](https://github.com/Divyansh151005/Temporal-Hypergraph-Engine) · [PyPI](https://pypi.org/project/hypergraph-client/) · [npm](https://www.npmjs.com/package/@temporal-hypergraph/sdk)

**🎯 Stale Facts Served in Multi-Hop Retrieval** <sub>(lower is better)</sub>

```text
Temporal Hypergraph      0.0 %               ░░░░░░░░░░░░░░░░░░░░░░░░░   00.00 % 
Graph RAG                45.1 %              ███████████░░░░░░░░░░░░░░   45.10 % 
Vector RAG               52.5 %              █████████████░░░░░░░░░░░░   52.50 % 
```

**🧠 Facts Recalled at a Matched Token Budget** <sub>(higher is better)</sub>

```text
Temporal Hypergraph      62.2 %              ████████████████░░░░░░░░░   62.20 % 
Vector RAG               8.6 %               ██░░░░░░░░░░░░░░░░░░░░░░░   08.60 % 
```

**⚙️ Under the Hood**

```text
🚀 Latency        0.53 ms p50 — 7.8× faster than a temporal property graph
🔒 Snapshots      375 ns p99 acquire under a heavy writer (vs 48.9 ms RwLock)
📈 Scale          10M hyperedges ingested in 85.6 s — 117K/s sustained, 227K/s peak
🧩 vLLM           1,600 KV blocks restored bit-exact, 0 mismatches, +0 B VRAM
📦 SDKs           Rust core · Python (PyPI) · TypeScript (npm) · Docker (GHCR)
```

---

### 🎓 Education & Experience

```text
🎓 B.Tech, Computer Science & Engineering       IIT Ropar
💼 Software Engineering Intern                  Arista Networks
📍 Based in                                     Pune, Maharashtra, India
```

### 🔬 Research

```text
📄 DualCare: A Blockchain Framework for Secure Medical Data Sharing with Dual Consent
   Published in IEEE Xplore

   Cross-chain consortium blockchain · dual consent across Hyperledger Fabric networks
   Relay service for consent propagation · MinIO off-chain storage · on-chain integrity
   AES-256 · RSA-2048 · time-limited key revocation
```

<sub>Read the paper on <a href="https://ieeexplore.ieee.org/document/11575533">IEEE Xplore</a>.</sub>

### 🏆 Hackathons

```text
🥇 MedinosXAdvitya       1st place     Multimodal medical chatbot — NLP + image analysis
🥇 Ideathon              1st place     NFC smart entry with backend ID verification
🥈 Sustainovate          2nd place     Land image analysis — 3D segmentation, geospatial maps
🥈 Edify                 2nd place     Drone imagery pipeline with automated preprocessing
```

---

### 🌍 Open Source

<!--START_SECTION:oss-->
**🌍 13 Merged Pull Requests Across 5 Upstream Projects**

```text
vercel/turborepo                      5 merged      ████████████████████
apple/foundationdb                    2 merged      ████████░░░░░░░░░░░░
lballabio/QuantLib                    2 merged      ████████░░░░░░░░░░░░
anthropics/buffa                      2 merged      ████████░░░░░░░░░░░░
K-Dense-AI/scientific-agent-skills    2 merged      ████████░░░░░░░░░░░░
google/guava                          3 in review   ████████████░░░░░░░░
meta/pyrefly                          1 in review   ████░░░░░░░░░░░░░░░░
```

<sub>[vercel/turborepo](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3ADivyansh151005+repo%3Avercel%2Fturborepo) · [apple/foundationdb](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3ADivyansh151005+repo%3Aapple%2Ffoundationdb) · [lballabio/QuantLib](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3ADivyansh151005+repo%3Alballabio%2FQuantLib) · [anthropics/buffa](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3ADivyansh151005+repo%3Aanthropics%2Fbuffa) · [K-Dense-AI/scientific-agent-skills](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3ADivyansh151005+repo%3AK-Dense-AI%2Fscientific-agent-skills) · [meta/pyrefly](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3ADivyansh151005+repo%3Ameta%2Fpyrefly) · [google/guava](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3ADivyansh151005+repo%3Agoogle%2Fguava)</sub>
<!--END_SECTION:oss-->


---

<p align="center"><em>I love connecting with people working on hard systems problems — say <b>hi</b> on <a href="https://www.linkedin.com/in/divyansh-barodiya/">LinkedIn</a>.</em></p>
