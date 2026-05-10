import streamlit as st
import time
from pipeline import run_research_pipeline

def extract_text(content):

    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, dict):
                text_parts.append(item.get("text", str(item)))

            else:
                text_parts.append(str(item))

        return "\n".join(text_parts)

    return str(content)

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchOS — Multi-Agent System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS (dark research-lab aesthetic) ───────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}
.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #111118 !important;
    border-right: 1px solid #2a2a3a;
}
[data-testid="stSidebar"] * { color: #7070a0 !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem; }

/* ── Logo ── */
.logo-wrap {
    display: flex; align-items: center; gap: 12px;
    padding-bottom: 20px; border-bottom: 1px solid #2a2a3a; margin-bottom: 24px;
}
.logo-icon {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, #7c6af7, #a855f7);
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
}
.logo-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px; color: #e8e8f0 !important; letter-spacing: -0.3px;
}
.logo-sub {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #7070a0 !important;
    letter-spacing: 1.5px; text-transform: uppercase;
}

/* ── Page heading ── */
.page-heading {
    font-family: 'DM Serif Display', serif;
    font-size: 28px; color: #e8e8f0;
    letter-spacing: -0.5px; margin-bottom: 4px;
}
.page-sub {
    font-size: 13px; color: #7070a0;
    font-family: 'DM Mono', monospace; margin-bottom: 28px;
}

/* ── Input area ── */
.input-label {
    font-size: 11px; color: #7070a0;
    letter-spacing: 1.5px; text-transform: uppercase;
    font-family: 'DM Mono', monospace; margin-bottom: 8px;
}
[data-testid="stTextArea"] textarea {
    background: #1a1a24 !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 15px !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #7c6af7 !important;
    box-shadow: 0 0 0 2px rgba(124,106,247,0.15) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: #7c6af7 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 10px 24px !important;
    transition: all 0.15s !important;
}
.stButton > button:hover {
    background: #a855f7 !important;
    transform: translateY(-1px);
}

/* ── Pipeline step cards ── */
.step-card {
    background: #111118;
    border: 1px solid #2a2a3a;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 0;
    position: relative;
    overflow: hidden;
}
.step-card-active {
    background: rgba(124,106,247,0.08);
    border-color: #7c6af7;
}
.step-card-done {
    border-color: #2dd4bf;
}
.step-bar {
    height: 2px; background: #2a2a3a;
    border-radius: 2px; margin-bottom: 12px;
}
.step-bar-active { background: linear-gradient(90deg, #7c6af7, #a855f7); }
.step-bar-done   { background: #2dd4bf; }
.step-num  { font-family:'DM Mono',monospace; font-size:10px; color:#7070a0; letter-spacing:1px; margin-bottom:6px; }
.step-name { font-size:14px; font-weight:500; color:#e8e8f0; margin-bottom:4px; }
.step-desc { font-size:11px; color:#7070a0; line-height:1.5; }
.step-status-idle    { color:#7070a0; }
.step-status-running { color:#f59e0b; }
.step-status-done    { color:#2dd4bf; }
.dot { display:inline-block; width:6px; height:6px; border-radius:50%; margin-right:5px; vertical-align:middle; }
.dot-idle    { background:#2a2a3a; }
.dot-running { background:#f59e0b; }
.dot-done    { background:#2dd4bf; }

/* ── Console log ── */
.console-wrap {
    background: #111118;
    border: 1px solid #2a2a3a;
    border-radius: 14px;
    overflow: hidden;
    margin-top: 8px;
}
.console-header {
    display:flex; align-items:center; gap:8px;
    padding: 12px 16px;
    border-bottom: 1px solid #2a2a3a;
    font-family:'DM Mono',monospace; font-size:12px; color:#7070a0;
}
.console-body {
    padding: 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 1.8;
    min-height: 120px;
    max-height: 260px;
    overflow-y: auto;
    color: #7070a0;
}

/* ── Result cards ── */
.result-card {
    background: #111118;
    border: 1px solid #2a2a3a;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 16px;
}
.result-header {
    padding: 12px 16px;
    border-bottom: 1px solid #2a2a3a;
    font-size: 12px; color:#7070a0;
    display:flex; align-items:center; gap:8px;
}
.result-body {
    padding: 16px;
    font-size: 13px; color:#a0a0c0; line-height:1.8;
}
.result-body-report {
    padding: 20px;
    font-size: 14px; color:#c8c8e0; line-height:1.9;
    white-space: pre-wrap;
}

/* ── Metric chips ── */
.metric-chip {
    display:inline-block;
    background:#1a1a24; border:1px solid #2a2a3a;
    border-radius:8px; padding:4px 12px;
    font-family:'DM Mono',monospace; font-size:11px; color:#7070a0;
    margin-right:8px;
}
.metric-chip span { color:#e8e8f0; font-size:15px; font-weight:500; display:block; }

/* ── Feedback stars ── */
.stars { font-size: 18px; color: #f59e0b; letter-spacing: 2px; margin-bottom:8px; }

/* ── Suggestion tags ── */
.tag-row { display:flex; gap:8px; flex-wrap:wrap; margin-top:12px; }
.tag {
    padding:5px 14px;
    background:#1a1a24; border:1px solid #2a2a3a;
    border-radius:20px; font-size:11px; color:#7070a0;
    font-family:'DM Mono',monospace; cursor:pointer;
    transition:all 0.15s;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="logo-wrap">
      <div class="logo-icon">🔬</div>
      <div>
        <div class="logo-title">Quantum</div>
        <div class="logo-sub">Multi-Agent System</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Workspace**", help="Navigation")
    st.markdown("🔭 &nbsp; New Research")
    st.markdown("📄 &nbsp; Reports")
    st.markdown("⚙️ &nbsp; Settings")
    st.divider()

    st.markdown("**Agents**")
    search_status  = st.empty()
    reader_status  = st.empty()
    writer_status  = st.empty()
    critic_status  = st.empty()

    def set_sidebar(s, r, w, c):
        def badge(label, state):
            color = {"idle":"#7070a0","running":"#f59e0b","done":"#2dd4bf"}[state]
            symbol = {"idle":"○","running":"●","done":"✓"}[state]
            return f'<span style="color:{color};font-size:12px;font-family:DM Mono,monospace">{symbol} {label}</span>'
        search_status.markdown(badge("Search Agent", s),  unsafe_allow_html=True)
        reader_status.markdown(badge("Reader Agent", r),  unsafe_allow_html=True)
        writer_status.markdown(badge("Writer Chain", w),  unsafe_allow_html=True)
        critic_status.markdown(badge("Critic Chain", c),  unsafe_allow_html=True)

    set_sidebar("idle","idle","idle","idle")

# ── Main content ───────────────────────────────────────────────────────────────
st.markdown('<div class="page-heading">Research Pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">4-agent autonomous research system</div>', unsafe_allow_html=True)

# ── Topic input ────────────────────────────────────────────────────────────────
st.markdown('<div class="input-label">🔍 Research Topic</div>', unsafe_allow_html=True)
topic = st.text_area(
    label="topic",
    label_visibility="collapsed",
    placeholder="e.g. Impact of large language models on scientific research in 2024...",
    height=80,
    key="topic_input",
)

st.markdown("""
<div class="tag-row">
  <span class="tag">⚛ Quantum computing</span>
  <span class="tag">🏥 AI in healthcare</span>
  <span class="tag">🌿 Climate tech</span>
  <span class="tag">🤖 Future of work</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
run_col, _ = st.columns([1, 5])
with run_col:
    run_clicked = st.button("▶  Run Pipeline", use_container_width=True)

st.divider()

# ── Pipeline step cards ────────────────────────────────────────────────────────
STEPS = [
    ("01/04", "🔍", "Search Agent",  "Finds recent, reliable information across the web"),
    ("02/04", "📡", "Reader Agent",  "Scrapes and extracts deep content from top URLs"),
    ("03/04", "✍️", "Writer Chain",  "Drafts a structured, comprehensive report"),
    ("04/04", "🧐", "Critic Chain",  "Reviews, scores and refines the final report"),
]

def render_step(col, num, icon, name, desc, state="idle"):
    bar_cls    = {"idle":"step-bar","running":"step-bar step-bar-active","done":"step-bar step-bar-done"}[state]
    card_cls   = {"idle":"step-card","running":"step-card step-card-active","done":"step-card step-card-done"}[state]
    stat_cls   = f"step-status-{state}"
    dot_cls    = f"dot dot-{state}"
    stat_label = {"idle":"idle","running":"running…","done":"completed"}[state]
    col.markdown(f"""
    <div class="{card_cls}">
      <div class="{bar_cls}"></div>
      <div class="step-num">{num}</div>
      <div style="font-size:22px;margin-bottom:6px">{icon}</div>
      <div class="step-name">{name}</div>
      <div class="step-desc">{desc}</div>
      <div class="{stat_cls}" style="margin-top:10px;font-size:11px;font-family:'DM Mono',monospace">
        <span class="{dot_cls}"></span>{stat_label}
      </div>
    </div>""", unsafe_allow_html=True)

cols = st.columns(4)
step_placeholders = [c.empty() for c in cols]

def update_steps(states):
    for i, (ph, (num, icon, name, desc)) in enumerate(zip(step_placeholders, STEPS)):
        with ph:
            render_step(ph, num, icon, name, desc, states[i])

update_steps(["idle","idle","idle","idle"])

# ── Console log ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="console-wrap">
  <div class="console-header">⬛ Pipeline Console</div>
</div>""", unsafe_allow_html=True)

log_placeholder = st.empty()
log_lines = []

def render_log():
    colors = {"info":"#7c6af7","agent":"#2dd4bf","success":"#34d399","warn":"#f59e0b","plain":"#7070a0"}
    html = '<div class="console-body">'
    if not log_lines:
        html += '<span style="color:#3a3a50">Pipeline output will appear here...</span>'
    for ts, msg, kind in log_lines:
        c = colors.get(kind, colors["plain"])
        html += f'<div><span style="color:#3a3a50">{ts}</span>&nbsp;&nbsp;<span style="color:{c}">{msg}</span></div>'
    html += "</div>"
    log_placeholder.markdown(html, unsafe_allow_html=True)

render_log()

def log(msg, kind="plain"):
    ts = time.strftime("%H:%M:%S")
    log_lines.append((ts, msg, kind))
    render_log()

# ── Result placeholders ────────────────────────────────────────────────────────
results_placeholder = st.empty()

def render_results(state):
    search  = state.get("search_results","")
    scrape  = state.get("scraped_content","")
    report  = state.get("report","")
    feedback= state.get("feedback","")

    words   = len(report.split()) if report else 0
    read_m  = max(1, round(words/200))

    stars   = "★★★★☆"

    html = f"""
    <div class="result-card">
      <div class="result-header">🔍 &nbsp; Search Results</div>
      <div class="result-body">{search[:600]}{'…' if len(search)>600 else ''}</div>
    </div>
    <div class="result-card">
      <div class="result-header">📡 &nbsp; Scraped Content</div>
      <div class="result-body">{scrape[:600]}{'…' if len(scrape)>600 else ''}</div>
    </div>
    <div class="result-card">
      <div class="result-header" style="justify-content:space-between">
        <span>📄 &nbsp; Final Report</span>
        <span>
          <span class="metric-chip"><span>{words}</span>words</span>
          <span class="metric-chip"><span>{read_m} min</span>read</span>
        </span>
      </div>
      <div class="result-body-report">{report}</div>
    </div>
    <div class="result-card">
      <div class="result-header">🧐 &nbsp; Critic Feedback</div>
      <div class="result-body">
        <div class="stars">{stars}</div>
        {feedback}
      </div>
    </div>
    """
    results_placeholder.markdown(html, unsafe_allow_html=True)

# ── Pipeline execution ─────────────────────────────────────────────────────────
if run_clicked:

    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    log_lines.clear()
    results_placeholder.empty()

    start = time.time()

    try:

        # Step 1
        update_steps(["running", "idle", "idle", "idle"])
        set_sidebar("running", "idle", "idle", "idle")

        log("▶ Search Agent started", "info")
        log(f'  Querying: "{topic}"', "agent")

        time.sleep(0.5)

        # Step 2
        update_steps(["done", "running", "idle", "idle"])
        set_sidebar("done", "running", "idle", "idle")

        log("✓ Search Agent complete", "success")
        log("▶ Reader Agent started", "info")
        log("  Scraping top resources...", "agent")

        time.sleep(0.5)

        # Step 3
        update_steps(["done", "done", "running", "idle"])
        set_sidebar("done", "done", "running", "idle")

        log("✓ Reader Agent complete", "success")
        log("▶ Writer Chain started", "info")
        log("  Drafting research report...", "agent")

        time.sleep(0.5)

        # Step 4
        update_steps(["done", "done", "done", "running"])
        set_sidebar("done", "done", "done", "running")

        log("✓ Writer Chain complete", "success")
        log("▶ Critic Chain started", "info")
        log("  Reviewing final report...", "agent")

        # ── SINGLE PIPELINE CALL ──
        state = run_research_pipeline(topic)

        # Extract results
        search_results = state["search_results"]
        scraped_content = state["scraped_content"]
        report = state["report"]
        feedback = state["feedback"]

        # Final UI updates
        update_steps(["done", "done", "done", "done"])
        set_sidebar("done", "done", "done", "done")

        log("✓ Critic Chain complete", "success")

        elapsed = round(time.time() - start, 1)

        log(f"Pipeline finished in {elapsed}s ✓", "success")

        # ── Render Results ──
        st.divider()

        st.markdown("### Results")

        render_results({
            "search_results": search_results,
            "scraped_content": scraped_content,
            "report": report,
            "feedback": feedback,
        })

    except Exception as e:

        st.error(f"Pipeline Failed: {str(e)}")

        update_steps(["idle", "idle", "idle", "idle"])

        set_sidebar("idle", "idle", "idle", "idle")