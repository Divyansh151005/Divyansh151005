<div align="center">

# Divyansh Barodiya

**Building [Temporal Hypergraph Engine](#-flagship-temporal-hypergraph-engine)** · CSE @ IIT Ropar · SWE Intern @ **Arista Networks**  
*Pune, Maharashtra, India*

[![Live demo](https://img.shields.io/badge/demo-temporal--hypergraph--web.onrender.com-0ea5e9?style=for-the-badge)](https://temporal-hypergraph-web.onrender.com/)
[![Temporal Hypergraph Engine](https://img.shields.io/badge/repo-Temporal--Hypergraph--Engine-f97316?style=for-the-badge&logo=github)](https://github.com/Divyansh151005/Temporal-Hypergraph-Engine)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-divyansh--barodiya-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/divyansh-barodiya/)
[![Email](https://img.shields.io/badge/Email-2023csb1119@iitrpr.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:2023csb1119@iitrpr.ac.in)
[![IEEE DualCare](https://img.shields.io/badge/IEEE-DualCare-00629B?style=for-the-badge&logo=ieee&logoColor=white)](https://ieeexplore.ieee.org/document/11575533)

</div>

---

## ⚡ Flagship — Temporal Hypergraph Engine

**Time-aware memory for LLMs that never serves a stale fact.**

I built [**Temporal Hypergraph Engine**](https://github.com/Divyansh151005/Temporal-Hypergraph-Engine) — a lock-free, SIMD-accelerated **temporal hypergraph** database in Rust, with Python/TypeScript SDKs and a zero-copy KV-cache block store for vLLM. Facts are stored as **time-bounded N-ary hyperedges**; every retrieval hop is filtered by validity windows so superseded facts are not returned or expanded.

| | |
|---|---|
| **Live site** | [temporal-hypergraph-web.onrender.com](https://temporal-hypergraph-web.onrender.com/) — product overview, docs, and benchmarks |
| **Packages** | [`hypergraph-client`](https://pypi.org/project/hypergraph-client/) · [`hypergraph-engine-native`](https://pypi.org/project/hypergraph-engine-native/) · [`@temporal-hypergraph/sdk`](https://www.npmjs.com/package/@temporal-hypergraph/sdk) |
| **Highlights** | **0%** stale facts in multi-hop evals vs ~45–52% for vector/graph RAG · **7.8×** faster p50 than temporal property graphs · **375 ns** p99 snapshot under concurrent writers |

Rust core · async ingestion · temporal traversal API · vLLM KV restore path. [Read the engine README →](https://github.com/Divyansh151005/Temporal-Hypergraph-Engine#-why-temporal-hypergraphs)

---

## About

Software engineer working across **AI systems, backends, distributed systems, and cryptography**. I ship production AI stacks, contribute upstream to infrastructure and tooling, and publish research on **blockchain-backed healthcare data sharing**.

- 🔭 **Now:** Arista Networks internship · scaling **Temporal Hypergraph** · OSS in systems & developer tooling
- 🎓 **B.Tech CSE** @ IIT Ropar
- 📄 **Research:** *DualCare* — dual-consent, cross-chain medical data sharing on Hyperledger Fabric ([IEEE Xplore](https://ieeexplore.ieee.org/document/11575533))

---

## Pinned work

These four repos are what I’m building and maintaining right now (see pins on my profile):

| Project | One line |
|---------|----------|
| [**Temporal-Hypergraph-Engine**](https://github.com/Divyansh151005/Temporal-Hypergraph-Engine) | Temporal hypergraph DB + LLM memory / vLLM KV cache |
| [**Aether-Decoders**](https://github.com/Divyansh151005/Aether-Decoders) | FTQC quantum error correction — Union-Find + Relay-BP decoders in Rust/SystemVerilog |
| [**ZK-Coprocessor**](https://github.com/Divyansh151005/ZK-Coprocessor) | Trustless off-chain compute & historical state for smart contracts, ZK-verified on-chain |
| [**alpha-engine**](https://github.com/Divyansh151005/alpha-engine) | Event-driven crypto multi-alpha engine (Binance, PostgreSQL) |

---

## Open source (merged upstream)

I contribute fixes and docs where I use the tools daily — **merged PRs only** across **[Vercel Turborepo](https://github.com/vercel/turborepo)**, **[Apple FoundationDB](https://github.com/apple/foundationdb)**, **[Anthropic Buffa](https://github.com/anthropics/buffa)**, **[QuantLib](https://github.com/lballabio/QuantLib)**, and **[K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** — spanning CLI/docs, distributed-database safety, protobuf tooling, quantitative finance numerics, and agent skill corrections.

<div align="center">

[![Merged upstream PRs](https://img.shields.io/badge/merged_upstream-13+-22c55e?style=flat-square&logo=github)](https://github.com/pulls?q=is%3Apr+author%3ADivyansh151005+is%3Amerged+-repo%3ADivyansh151005%2FOurGuide_test+-repo%3ADivyansh151005%2FSOL_Wallet)
[![Contributions this year](https://img.shields.io/badge/GitHub_contributions-600+-181717?style=flat-square&logo=github)](https://github.com/Divyansh151005)

</div>

---

## Hackathons

| Event | Place | Focus |
|-------|-------|--------|
| MedinosXAdvitya | 🥇 1st | Multimodal medical chatbot |
| Ideathon | 🥇 1st | NFC smart entry + backend verification |
| Sustainovate | 🥈 2nd | Geospatial land analysis & 3D segmentation |
| Edify | 🥈 2nd | Drone imagery preprocessing pipeline |

---

## Stack

**Languages:** Rust · Python · TypeScript · Java · C/C++  
**Domains:** LLM/RAG memory · async APIs · ZK & smart contracts · quant/backtesting · Fabric/Solana

---

<div align="center">

<sub>Open to internships, collaborations, and hard systems problems — reach out via LinkedIn or email.</sub>

</div>
