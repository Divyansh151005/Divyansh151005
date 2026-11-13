# Hey, I'm Divyansh 👋

<img align="right" src="./assets/temporal-desk.gif" width="340" alt="Pixel desk: a monitor shows hyperedges appearing and expiring along a timeline"/>

### Building time-aware memory for LLMs.

<p><em>
  Creator of <a href="https://github.com/Divyansh151005/Temporal-Hypergraph-Engine"><b>Temporal Hypergraph Engine</b></a>
</em></p>

### ⚡ Flagship — Temporal Hypergraph Engine

A lock-free, SIMD-accelerated **temporal hypergraph** database in Rust that stores facts as time-bounded hyperedges, so LLM retrieval only follows facts that were true at the moment asked — with a zero-copy **vLLM KV-cache** block store alongside.

<br clear="right"/>

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

### ⚛️ Aether-Decoders

Real-time **quantum error correction** decoding for fault-tolerant quantum computers — an integer **Union-Find** decoder for surface codes and **Relay-BP** for qLDPC codes in Rust, rebuilt as **SystemVerilog** processing-element grids that match the Rust model bit for bit.

**🔌 RTL ≡ Rust Co-Simulation** <sub>(bit-identical decodes)</sub>

```text
Blueprint graphs         8 / 8 match         █████████████████████████   100.00 % 
Stim phenom d=5          4 / 4 match         █████████████████████████   100.00 % 
Circuit-level V=392      2 / 2 match         █████████████████████████   100.00 % 
Helios-n schedule RTL    16 / 16 match       █████████████████████████   100.00 % 
Helios-n circuit map     16 / 16 match       █████████████████████████   100.00 % 
```

**📐 FPGA Footprint** <sub>(Yosys LUT estimates, lower is better)</sub>

```text
Flat PE mesh, N=16       138,502 LUT         █████████████████████████
Flat PE mesh, N≥24       synthesis timeout   — the flat-mesh cliff
Helios-n lattice, 7 PEs  12,576 LUT          ██░░░░░░░░░░░░░░░░░░░░░░░
```

**⚙️ Under the Hood**

```text
🧮 Surface codes  Integer Union-Find — grow, merge, peel over F2, benchmarked vs PyMatching
🔗 qLDPC          Relay-BP on IBM gross [[144,12,12]] circuits vs BP+OSD, matched shots
🔁 Multiplexing   Helios-n time-multiplexed PE lattice past the flat-mesh synthesis cliff
🧪 Toolchain      Stim · Sinter · Verilator DPI · Icarus · Yosys
📊 Evidence       76 milestones · 28 Rust tests · 46 result CSVs · 29 RTL modules
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
**🌍 18 Merged Pull Requests Across 6 Upstream Projects**

```text
meta/pyrefly                          5 merged    ████████████████████
vercel/turborepo                      5 merged    ████████████████████
apple/foundationdb                    2 merged    ████████░░░░░░░░░░░░
lballabio/QuantLib                    2 merged    ████████░░░░░░░░░░░░
anthropics/buffa                      2 merged    ████████░░░░░░░░░░░░
K-Dense-AI/scientific-agent-skills    2 merged    ████████░░░░░░░░░░░░
```
<!--END_SECTION:oss-->


---

<p align="center"><em>I love connecting with people working on hard systems problems — say <b>hi</b> on <a href="https://www.linkedin.com/in/divyansh-barodiya/">LinkedIn</a>.</em></p>
