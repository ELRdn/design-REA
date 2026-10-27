# デザイン全史 / Web Edition

先史時代から2026年までを、15章・13の図版・128件の年表でたどる、図解化された教材サイトです。

**公開URL:** [https://elrdn.github.io/design-REA/](https://elrdn.github.io/design-REA/)  
**リポジトリ:** [https://github.com/ELRdn/design-REA](https://github.com/ELRdn/design-REA)

## 開く

`index.html` をブラウザで開いてください。ローカルファイルのまま動きます（書体の取得にGoogle Fontsへの接続を使います）。

| ページ | 内容 |
|---|---|
| `index.html` | 入口。展覧会の案内、デザインの方程式、15の部屋、年表・神話・図版の抜粋 |
| `read.html` | 本文。約122,000字、15章＋序章＋付録。目次、読書進捗、文字サイズ、印刷用CSS |
| `timeline.html` | 年表。128件を、等幅（時代の厚み）と対数（実際の時間感覚）で切り替え |
| `atlas.html` | 図版室。13枚の注釈つきSVG図版。フィルタと拡大ダイアログ |
| `method.html` | 検証室。20の神話、14の修正、100件のファクトチェック検索 |
| `textbooks.html` | 教本室。デザインの教科書・参考書7冊＋実践ブログを、書誌・役割・注意点で整理 |
| `design-notes.html` | 設計ノート。第一原理、色・書体・版面、自己批判、アクセシビリティ |

データ: `factcheck.csv` / `factcheck.json` / `デザイン全史.pdf` / `DESIGN_HISTORY_BOOK.md`

## 設計

- **台紙** `#E7E8E0` / **インク** `#111412` / **ウルトラマリン** `#1B2FC7` / **レジストレーション** `#F04A22` / **工程イエロー** `#F2C300` / **工程シアン** `#007F8F`
- **書体**: Shippori Mincho B1（歴史）、Archivo / Zen Kaku Gothic New（現在）、IBM Plex Mono（データ）、Noto Serif JP（本文）
- **13の図版**: すべてインラインSVG。フレーム、トンボ、注釈、スケールを共通言語にしている
- **フレームワークなし**: 静的HTML/CSS/JS。ビルドはPythonスクリプトのみ
- **読むための機能**: ライト/ダーク、文字サイズ、読書進捗、章目次、印刷用CSS、no-JSフォールバック、`prefers-reduced-motion`
- **アクセシビリティ**: WCAG 2.2 AAを目標。axe-coreで主要6ページの自動チェック0件（ライト/ダーク）、320–1440pxで横スクロールなし

## 再生成

```powershell
python design-history-research/site/build_read.py
python design-history-research/site/build_timeline.py
python design-history-research/site/build_atlas.py
python design-history-research/site/build_method.py
python design-history-research/site/build_notes.py
```

`build_read.py` が共通の head / rail / footer を持ち、他のスクリプトがそれを import します。本文を更新したら `DESIGN_HISTORY_BOOK.md` を再結合し、`build_read.py` を再実行してください。PDF・CSVは `design-history-research/` から `site/` にコピーしています。

## 検証

- `qa_site.py`: 320 / 390 / 768 / 1024 / 1440px の横overflow、ページエラー、axe-core（WCAG 2.2 AA）を確認
- `linkcheck.py`: 内部リンクとアンカーの存在を確認
- `qa_dark.py`: ダークモードのaxeチェック
- 自動チェックは、手動のキーボード操作・スクリーンリーダー確認の代わりにはなりません。

## 既知の限界

- Google Fontsに接続できない環境では、Yu Mincho / Yu Gothic / Consolasなどのフォールバックになります。
- タイムラインの「対数」は時間感覚のための比喩で、科学的な縮尺ではありません。
- 本文ページに全文検索はまだありません。
- 図版は対象の写真ではなく、構造を読むための作図です。正確な形は各博物館のコレクションで確認してください。
- 非西洋の記述は、英語圏の資料に依存している部分があります。本書の「限界」を参照してください。

## ファイル構成

```
site/
├─ index.html / read.html / timeline.html / atlas.html / method.html / design-notes.html / textbooks.html
├─ assets/
│  ├─ style.css      # デザイントークン、全ページのスタイル、印刷用CSS
│  └─ app.js         # テーマ、メニュー、数式、年表、図版、読書ツール
├─ favicon.svg
├─ build_read.py / build_timeline.py / build_atlas.py / build_method.py / build_notes.py / build_textbooks.py
├─ qa_site.py / qa_dark.py / linkcheck.py
├─ factcheck.csv / factcheck.json / デザイン全史.pdf / DESIGN_HISTORY_BOOK.md
├─ textbooks-research.md   # 教本調査ノート（書誌・版・出典）
└─ README.md
```
