/* デザイン全史 / Web Edition — interactions
   Vanilla, no dependencies. Every interactive element has a no-JS baseline
   except the timeline preview, which is progressive enhancement. */

(function () {
  "use strict";

  const root = document.documentElement;
  const body = document.body;

  /* ---------- Theme ---------- */
  const themeButtons = document.querySelectorAll("[data-theme-toggle]");

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function paintThemeButton() {
    const dark = currentTheme() === "dark";
    themeButtons.forEach((btn) => {
      btn.setAttribute("aria-pressed", String(dark));
      btn.setAttribute("aria-label", dark ? "照明を明るくする" : "照明を暗くする");
      btn.setAttribute("title", dark ? "照明を明るくする" : "照明を暗くする");
    });
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", dark ? "#0d0f0e" : "#e7e8e0");
  }

  themeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try {
        localStorage.setItem("dh-theme", next);
      } catch (e) {
        /* private mode */
      }
      paintThemeButton();
    });
  });
  paintThemeButton();

  /* ---------- Mobile navigation ---------- */
  const navToggle = document.querySelector("[data-nav-toggle]");
  const nav = document.getElementById("site-nav");
  const scrim = document.querySelector("[data-nav-scrim]");

  const navLabel = navToggle ? navToggle.querySelector(".nav-toggle__label") : null;

  function setNav(open) {
    body.classList.toggle("nav-open", open);
    if (navToggle) navToggle.setAttribute("aria-expanded", String(open));
    if (navLabel) navLabel.textContent = open ? "閉じる" : "メニュー";
    if (open && nav) {
      const first = nav.querySelector("a");
      if (first) first.focus({ preventScroll: true });
    }
  }

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      setNav(!body.classList.contains("nav-open"));
    });
  }

  if (scrim) {
    scrim.addEventListener("click", () => setNav(false));
  }

  if (nav) {
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) setNav(false);
    });
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && body.classList.contains("nav-open")) {
      setNav(false);
      if (navToggle) navToggle.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 760 && body.classList.contains("nav-open")) {
      setNav(false);
    }
  });

  /* ---------- Reveal on scroll ---------- */
  const revealItems = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealItems.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.04 }
    );
    revealItems.forEach((el) => io.observe(el));
  } else {
    revealItems.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------- Back to top ---------- */
  const toTop = document.createElement("button");
  toTop.type = "button";
  toTop.className = "to-top";
  toTop.setAttribute("aria-label", "ページ上部へ");
  toTop.textContent = "↑";
  document.body.appendChild(toTop);

  let footerVisible = false;
  const toggleToTop = () => {
    toTop.classList.toggle("is-visible", window.scrollY > 900 && !footerVisible);
  };
  const footerEl = document.querySelector(".footer");
  if (footerEl && "IntersectionObserver" in window) {
    const footerObserver = new IntersectionObserver(
      (entries) => {
        footerVisible = entries[0].isIntersecting;
        toggleToTop();
      },
      { rootMargin: "0px 0px 0px 0px" }
    );
    footerObserver.observe(footerEl);
  }
  window.addEventListener("scroll", toggleToTop, { passive: true });
  toggleToTop();
  toTop.addEventListener("click", () => {
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
  });

  /* ---------- Definition equation ---------- */
  const TERMS = {
    intent: {
      title: "意図",
      body:
        "何をしたいのか。誰に何を渡したいのか。デザインは自己表現ではなく、意図の翻訳から始まります。ただし、意図は最初から明確とは限りません。作りながら、意図そのものが発見されます。",
    },
    constraint: {
      title: "制約",
      body:
        "素材、技術、予算、法律、文化、身体、時間。制約は敵ではありません。制約があるから形は決まり、制約を読み替えるところに発明が生まれます。問題は、どの制約を受け入れ、どれを変えるかです。",
    },
    other: {
      title: "他者",
      body:
        "使う人、使えない人、未来の世代、非人間。デザインは、他者の時間と身体に介入します。だから「誰のためか」を問わずに形を決めることはできません。他者は、答えではなく、制約であり、目的です。",
    },
    form: {
      title: "かたち",
      body:
        "モノ、システム、サービス、体験、制度。形は、可能性と不可能性を配ります。椅子は座ることを可能にし、立ち続けることを難しくします。形は中立ではありません。",
    },
  };

  const termButtons = document.querySelectorAll("[data-term]");
  const termDetail = document.querySelector("[data-term-detail]");

  if (termButtons.length && termDetail) {
    const defaultHTML =
      "<strong>四つの項は、どれか一つが欠けても成立しません。</strong> 意図だけでは妄想になり、制約だけでは諦めになり、他者だけでは配慮になり、かたちだけでは装飾になります。四つが交わるところに、デザインがあります。";
    termDetail.innerHTML = defaultHTML;

    termButtons.forEach((btn) => {
      btn.setAttribute("aria-pressed", "false");
      btn.addEventListener("click", () => {
        const key = btn.getAttribute("data-term");
        const data = TERMS[key];
        if (!data) return;
        const isOpen = btn.getAttribute("aria-pressed") === "true";
        termButtons.forEach((b) => b.setAttribute("aria-pressed", "false"));
        if (isOpen) {
          termDetail.innerHTML = defaultHTML;
          return;
        }
        btn.setAttribute("aria-pressed", "true");
        termDetail.innerHTML = `<strong>${data.title}。</strong> ${data.body}`;
      });
    });
  }

  /* ---------- Timeline preview ---------- */
  const PREVIEW = {
    prehistory: {
      name: "先史",
      years: "約5万年前 – 紀元前3000年",
      question: "最初のデザインは、美しさのためだったのか、生き延びるためだったのか。",
      events: [
        { y: "約176万年前", t: "アシューリアン握斧", m: "左右対称の石器。機能と、見せるための形。" },
        { y: "約2万年前", t: "土器", m: "粘土を焼いて、初めて「容器」を人工的に作る。" },
        { y: "約5000年前", t: "ウルクの都市", m: "道路、神殿、市場。都市という巨大なシステム。" },
      ],
    },
    ancient: {
      name: "古代",
      years: "紀元前3000年 – 紀元前500年",
      question: "文字は、誰の記憶を保存し、誰の記憶を消したのか。",
      events: [
        { y: "約3200年前", t: "楔形文字", m: "会計のトークンから、行政と文学の文字へ。" },
        { y: "約4500年前", t: "モヘンジョ・ダロ", m: "格子状の街路、下水道、標準化されたレンガ。" },
        { y: "約2000年前", t: "ローマの水道橋", m: "公共インフラという、見えないデザイン。" },
      ],
    },
    medieval: {
      name: "古典・中世",
      years: "紀元前500年 – 1400年",
      question: "職人の身体知は、どこで生まれ、どこで失われたのか。",
      events: [
        { y: "537年", t: "ハギア・ソフィア", m: "ドームと光。ビザンツの宇宙観。" },
        { y: "1140年ごろ", t: "ゴシック建築", m: "尖頭アーチ、リブ、フライング・バットレス。" },
        { y: "1200年ごろ", t: "禅宗の伝来", m: "建築、庭園、茶、書。日本の美意識の一層。" },
      ],
    },
    print: {
      name: "印刷・ルネサンス",
      years: "1400 – 1750",
      question: "複製は、知識を民主化したのか、それとも新しい管理を生んだのか。",
      events: [
        { y: "1440年ごろ", t: "グーテンベルクの活版印刷", m: "活字、油性インク、ブドウ絞り機。" },
        { y: "1501年", t: "アルドゥスのイタリック体", m: "持ち運べる本。読書のスタイルが変わる。" },
        { y: "1682年", t: "ヴェルサイユ宮殿", m: "権力を空間で演出するバロック。" },
      ],
    },
    industrial: {
      name: "産業革命",
      years: "1750 – 1900",
      question: "機械は、美しさを殺したのか、それとも新しい美しさを生んだのか。",
      events: [
        { y: "1759年", t: "ウェッジウッド創業", m: "デザインを市場・生産・ブランドのシステムに組む。" },
        { y: "1851年", t: "ロンドン万国博覧会", m: "クリスタル・パレス。機械の勝利と醜さ。" },
        { y: "1861年", t: "モリス商会", m: "アーツ・アンド・クラフツ。美と労働の統一。" },
      ],
    },
    modern: {
      name: "モダニズム",
      years: "1900 – 1945",
      question: "普遍の名の下で、何が地方の特殊として切り捨てられたのか。",
      events: [
        { y: "1919年", t: "バウハウス設立", m: "芸術と技術の統合。学校が世界を変える。" },
        { y: "1917年", t: "デ・ステイル", m: "直線、矩形、原色。抽象の宇宙。" },
        { y: "1930年代", t: "流線型", m: "速度と未来を、冷蔵庫にまでまとわせる。" },
      ],
    },
    postwar: {
      name: "戦後",
      years: "1945 – 1970",
      question: "豊かさのデザインは、誰の労働の上に建っていたのか。",
      events: [
        { y: "1956年", t: "イームズ・ラウンジチェア", m: "合板、革、アルミ。快適さの工学。" },
        { y: "1956年", t: "ブラウン SK4", m: "「白雪姫の棺」。機能主義の黄金期。" },
        { y: "1964年", t: "東京オリンピック", m: "ピクトグラム。言語を越える情報デザイン。" },
      ],
    },
    postmodern: {
      name: "ポストモダン",
      years: "1970 – 1990",
      question: "装飾の復権は、自由の回復か、消費の加速か。",
      events: [
        { y: "1981年", t: "メンフィス初展", m: "色、模様、引用。機能主義への反逆。" },
        { y: "1984年", t: "マッキントッシュ", m: "GUIの大衆化。画面が世界になる。" },
        { y: "1980年", t: "無印良品", m: "「これでいい」。引き算のデザイン。" },
      ],
    },
    digital: {
      name: "デジタル",
      years: "1990 – 2010",
      question: "使いやすさは、民主化か、依存か。",
      events: [
        { y: "1989年", t: "ワールドワイドウェブ", m: "誰でも発信できる。誰でも監視される。" },
        { y: "2007年", t: "iPhone", m: "マルチタッチ。体験の再設計。" },
        { y: "2014年", t: "Material Design", m: "デザインをスケールさせる言語。" },
      ],
    },
    now: {
      name: "現在",
      years: "2010 – 2026",
      question: "AIが形を作るとき、誰が「良い」を決めるのか。",
      events: [
        { y: "2022年", t: "生成AIの普及", m: "画像、文章、コード。制作の再配置。" },
        { y: "2024年", t: "EU AI Act 発効", m: "リスクベースの規制。責任の所在。" },
        { y: "2024年", t: "WCAG 2.2 勧告", m: "アクセシビリティは、任意から基準へ。" },
      ],
    },
  };

  const previewRuler = document.querySelector("[data-tp-ruler]");
  const previewPanel = document.querySelector("[data-tp-panel]");

  if (previewRuler && previewPanel) {
    function renderPreview(key) {
      const era = PREVIEW[key];
      if (!era) return;
      previewPanel.innerHTML = `
        <div class="tp__head">
          <span class="tp__years">${era.years}</span>
          <h3 class="tp__title">${era.name}</h3>
          <p class="tp__question">${era.question}</p>
        </div>
        <div class="tp__events">
          ${era.events
            .map(
              (e) => `
            <div class="tp-event">
              <span class="tp-event__year">${e.y}</span>
              <div>
                <span class="tp-event__title">${e.t}</span>
                <span class="tp-event__meaning">${e.m}</span>
              </div>
            </div>`
            )
            .join("")}
        </div>`;
      previewRuler.querySelectorAll("[data-era]").forEach((btn) => {
        btn.setAttribute("aria-pressed", String(btn.getAttribute("data-era") === key));
      });
    }

    previewRuler.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-era]");
      if (btn) renderPreview(btn.getAttribute("data-era"));
    });

    renderPreview("prehistory");
  }

  /* ---------- Full timeline page ---------- */
  const timelineDataEl = document.getElementById("timeline-data");
  if (timelineDataEl) {
    let data;
    try {
      data = JSON.parse(timelineDataEl.textContent);
    } catch (e) {
      data = null;
    }

    if (data && data.eras && data.events) {
      const bar = document.querySelector("[data-tl-bar]");
      const eraButtons = Array.from(document.querySelectorAll(".tl-era"));
      const barSegments = Array.from(document.querySelectorAll(".tl-bar__seg"));
      const panels = Array.from(document.querySelectorAll("[data-tl-list]"));
      const detail = document.querySelector("[data-tl-detail]");
      const detailEra = detail ? detail.querySelector(".tl-detail__era") : null;
      const detailYear = detail ? detail.querySelector("[data-tl-year]") : null;
      const detailTitle = detail ? detail.querySelector("[data-tl-title]") : null;
      const detailText = detail ? detail.querySelector("[data-tl-text]") : null;
      const detailLink = detail ? detail.querySelector("[data-tl-link]") : null;
      const prevBtn = detail ? detail.querySelector("[data-tl-prev]") : null;
      const nextBtn = detail ? detail.querySelector("[data-tl-next]") : null;
      const modeButtons = Array.from(document.querySelectorAll("[data-tl-mode]"));

      let mode = "equal";
      let eraId = "prehistory";
      let eventId = null;

      const eraById = {};
      data.eras.forEach((e) => {
        eraById[e.id] = e;
      });

      function chapterLabel(id) {
        if (!id) return "この章を読む";
        if (id === "prologue") return "序章を読む";
        const n = id.split("-")[1];
        return "第" + parseInt(n, 10) + "章を読む";
      }

      function setMode(next) {
        mode = next;
        modeButtons.forEach((b) => {
          b.setAttribute("aria-pressed", String(b.getAttribute("data-tl-mode") === mode));
        });
        barSegments.forEach((seg) => {
          const era = eraById[seg.getAttribute("data-era")];
          if (!era) return;
          const weight = mode === "log" ? Math.log10(era.span + 1) : 1;
          seg.style.setProperty("--w", weight.toFixed(4));
        });
      }

      function setEra(next) {
        eraId = next;
        eraButtons.forEach((b) => {
          b.setAttribute("aria-pressed", String(b.getAttribute("data-era") === eraId));
        });
        barSegments.forEach((b) => {
          b.setAttribute("aria-pressed", String(b.getAttribute("data-era") === eraId));
        });
        panels.forEach((p) => {
          p.hidden = p.getAttribute("data-tl-list") !== eraId;
        });
        const eraEvents = data.events.filter((ev) => ev.era === eraId);
        if (eraEvents.length) setEvent(eraEvents[0].id);
      }

      function setEvent(id) {
        eventId = id;
        const ev = data.events.find((e) => e.id === id);
        if (!ev) return;
        document.querySelectorAll(".tl-ev").forEach((btn) => {
          btn.setAttribute("aria-pressed", String(btn.getAttribute("data-ev") === id));
        });
        const era = eraById[ev.era];
        if (detailEra) detailEra.innerHTML = `<span>${era.no} / ${era.name}</span><span>${era.years}</span>`;
        if (detailYear) detailYear.textContent = ev.year;
        if (detailTitle) detailTitle.textContent = ev.title;
        if (detailText) detailText.textContent = ev.meaning + "。";
        if (detailLink) {
          detailLink.href = "read.html#" + era.chapter;
          detailLink.textContent = chapterLabel(era.chapter) + " ↗";
        }
        const eraEvents = data.events.filter((e) => e.era === ev.era);
        const idx = eraEvents.findIndex((e) => e.id === id);
        if (prevBtn) prevBtn.disabled = idx <= 0;
        if (nextBtn) nextBtn.disabled = idx >= eraEvents.length - 1;
      }

      function step(delta) {
        const ev = data.events.find((e) => e.id === eventId);
        if (!ev) return;
        const eraEvents = data.events.filter((e) => e.era === ev.era);
        const idx = eraEvents.findIndex((e) => e.id === eventId);
        const next = eraEvents[idx + delta];
        if (next) setEvent(next.id);
      }

      const onEraClick = (event) => {
        const btn = event.target.closest("[data-era]");
        if (btn) setEra(btn.getAttribute("data-era"));
      };
      if (bar) bar.addEventListener("click", onEraClick);
      eraButtons.forEach((b) => b.addEventListener("click", onEraClick));

      modeButtons.forEach((b) => {
        b.addEventListener("click", () => setMode(b.getAttribute("data-tl-mode")));
      });

      document.querySelectorAll(".tl-ev").forEach((btn) => {
        btn.addEventListener("click", () => setEvent(btn.getAttribute("data-ev")));
      });

      if (prevBtn) prevBtn.addEventListener("click", () => step(-1));
      if (nextBtn) nextBtn.addEventListener("click", () => step(1));

      const search = document.querySelector("[data-tl-search]");
      const count = document.querySelector("[data-tl-count]");
      const rows = Array.from(document.querySelectorAll("[data-tl-row]"));
      if (search && rows.length) {
        const filter = () => {
          const q = search.value.trim().toLowerCase();
          let visible = 0;
          rows.forEach((row) => {
            const show = !q || row.textContent.toLowerCase().includes(q);
            row.hidden = !show;
            if (show) visible += 1;
          });
          if (count) count.textContent = visible + " / " + rows.length;
        };
        search.addEventListener("input", filter);
      }

      setMode("equal");
      setEra("prehistory");
    }
  }

  /* ---------- Reading tools ---------- */
  const readRoot = document.querySelector("[data-read]");
  if (readRoot) {
    const progress = document.querySelector("[data-progress]");
    const sizes = ["small", "normal", "large"];
    const scale = { small: "0.92", normal: "1", large: "1.12" };
    let size = "normal";
    try {
      const stored = localStorage.getItem("dh-read-size");
      if (stored && sizes.includes(stored)) size = stored;
    } catch (e) {
      /* noop */
    }

    function applySize() {
      root.style.setProperty("--read-scale", scale[size]);
      document.querySelectorAll("[data-font-size]").forEach((btn) => {
        btn.setAttribute("aria-pressed", String(btn.getAttribute("data-font-size") === size));
      });
      const status = document.querySelector("[data-font-status]");
      if (status) status.textContent = size === "small" ? "小" : size === "large" ? "大" : "標準";
      try {
        localStorage.setItem("dh-read-size", size);
      } catch (e) {
        /* noop */
      }
    }

    document.querySelectorAll("[data-font-size]").forEach((btn) => {
      btn.addEventListener("click", () => {
        size = btn.getAttribute("data-font-size");
        applySize();
      });
    });
    applySize();

    if (progress) {
      const update = () => {
        const h = document.documentElement;
        const max = h.scrollHeight - h.clientHeight;
        const p = max > 0 ? Math.min(1, h.scrollTop / max) : 0;
        progress.style.transform = `scaleX(${p})`;
      };
      update();
      window.addEventListener("scroll", update, { passive: true });
      window.addEventListener("resize", update);
    }

    /* Highlight the current section in the table of contents */
    const tocLinks = Array.from(document.querySelectorAll("[data-toc-link]"));
    const targets = tocLinks
      .map((link) => {
        const id = link.getAttribute("href");
        return id && id.startsWith("#") ? document.querySelector(id) : null;
      })
      .filter(Boolean);

    if ("IntersectionObserver" in window && targets.length) {
      const tocObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            const id = "#" + entry.target.id;
            tocLinks.forEach((link) => {
              const active = link.getAttribute("href") === id;
              link.classList.toggle("is-current", active);
              if (active) link.setAttribute("aria-current", "true");
              else link.removeAttribute("aria-current");
            });
          });
        },
        { rootMargin: "-12% 0px -76% 0px", threshold: 0 }
      );
      targets.forEach((t) => tocObserver.observe(t));
    }
  }

  /* ---------- Atlas filter ---------- */
  const filterBar = document.querySelector("[data-filters]");
  const plateCards = Array.from(document.querySelectorAll("[data-plate-card]"));

  if (filterBar && plateCards.length) {
    filterBar.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-filter]");
      if (!btn) return;
      const filter = btn.getAttribute("data-filter");
      filterBar.querySelectorAll("[data-filter]").forEach((b) => {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      plateCards.forEach((card) => {
        const tags = card.getAttribute("data-tags") || "";
        const show = filter === "all" || tags.split(" ").includes(filter);
        card.hidden = !show;
      });
      const count = document.querySelector("[data-filter-count]");
      if (count) {
        const visible = plateCards.filter((c) => !c.hidden).length;
        count.textContent = String(visible);
      }
    });
  }

  /* ---------- Plate dialog ---------- */
  const dialog = document.getElementById("plate-dialog");
  if (dialog && typeof dialog.showModal === "function") {
    const dialogTitle = dialog.querySelector("[data-dialog-title]");
    const dialogNo = dialog.querySelector("[data-dialog-no]");
    const dialogText = dialog.querySelector("[data-dialog-text]");
    const dialogArt = dialog.querySelector("[data-dialog-art]");

    document.querySelectorAll("[data-open-plate]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const card = btn.closest("[data-plate-card]");
        if (!card) return;
        const svg = card.querySelector("svg");
        const title = card.querySelector(".plate-card__title");
        const no = card.querySelector(".plate-card__no");
        const desc = card.querySelector(".plate-card__desc");
        if (dialogTitle) dialogTitle.textContent = title ? title.textContent : "";
        if (dialogNo) dialogNo.textContent = no ? no.textContent : "";
        if (dialogText) dialogText.innerHTML = desc ? desc.innerHTML : "";
        if (dialogArt && svg) {
          dialogArt.innerHTML = "";
          const clone = svg.cloneNode(true);
          clone.removeAttribute("style");
          clone.removeAttribute("aria-labelledby");
          clone.removeAttribute("role");
          clone.setAttribute("aria-hidden", "true");
          const t = clone.querySelector("title");
          const d = clone.querySelector("desc");
          if (t) t.remove();
          if (d) d.remove();
          dialogArt.appendChild(clone);
        }
        dialog.showModal();
      });
    });

    const closeBtn = dialog.querySelector("[data-close-plate]");
    if (closeBtn) closeBtn.addEventListener("click", () => dialog.close());

    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) dialog.close();
    });
  }

  /* ---------- Fact-check filter ---------- */
  const fcSearch = document.querySelector("[data-fc-search]");
  const fcVerdict = document.querySelector("[data-fc-verdict]");
  const fcRows = Array.from(document.querySelectorAll("[data-fc-row]"));
  const fcCount = document.querySelector("[data-fc-count]");

  if (fcRows.length) {
    function filterRows() {
      const q = (fcSearch ? fcSearch.value : "").trim().toLowerCase();
      const v = fcVerdict ? fcVerdict.value : "all";
      let visible = 0;
      fcRows.forEach((row) => {
        const text = row.textContent.toLowerCase();
        const verdict = row.getAttribute("data-verdict") || "";
        const matchesText = !q || text.includes(q);
        const matchesVerdict =
          v === "all" ||
          (v === "概ね確認済み"
            ? verdict.includes("概ね")
            : verdict.startsWith("確認済み") && !verdict.includes("概ね"));
        const show = matchesText && matchesVerdict;
        row.hidden = !show;
        if (show) visible += 1;
      });
      if (fcCount) fcCount.textContent = String(visible);
    }

    if (fcSearch) fcSearch.addEventListener("input", filterRows);
    if (fcVerdict) fcVerdict.addEventListener("change", filterRows);
    filterRows();
  }
})();
