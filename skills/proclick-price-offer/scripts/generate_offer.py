from __future__ import annotations

import argparse
from pathlib import Path
import unicodedata

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ASSETS = SKILL_DIR / "assets"
LOGO = ASSETS / "proclick_logo.png"
LOGO_WHITE = ASSETS / "proclick_logo_white.png"
TEAM_COVER = ASSETS / "proclick_team_cover.png"

FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

RED = colors.HexColor("#EF493E")
DARK = colors.HexColor("#24211F")
CREAM = colors.HexColor("#F4EFE7")
MUTED = colors.HexColor("#77706A")
BORDER = colors.HexColor("#D7CEC3")
GREEN = colors.HexColor("#D9EDE1")


def clean(value: str) -> str:
    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean(text), style)


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("PC", FONT_REGULAR))
    pdfmetrics.registerFont(TTFont("PC-Bold", FONT_BOLD))


def make_styles():
    st = getSampleStyleSheet()
    st.add(ParagraphStyle("Hero", fontName="PC-Bold", fontSize=28, leading=32, textColor=colors.white, spaceAfter=8))
    st.add(ParagraphStyle("HeroSub", fontName="PC", fontSize=11.5, leading=15, textColor=colors.HexColor("#F4F0EA")))
    st.add(ParagraphStyle("Eyebrow", fontName="PC-Bold", fontSize=8.2, leading=10, textColor=RED, spaceAfter=5))
    st.add(ParagraphStyle("H1", fontName="PC-Bold", fontSize=22, leading=26, textColor=DARK, spaceAfter=8))
    st.add(ParagraphStyle("H1Dark", fontName="PC-Bold", fontSize=22, leading=26, textColor=colors.white, spaceAfter=8))
    st.add(ParagraphStyle("Body", fontName="PC", fontSize=9.3, leading=12.8, textColor=DARK, spaceAfter=4))
    st.add(ParagraphStyle("BodyMuted", fontName="PC", fontSize=9, leading=12, textColor=MUTED, spaceAfter=4))
    st.add(ParagraphStyle("BodyDark", fontName="PC", fontSize=9.5, leading=13, textColor=colors.HexColor("#E8E1DA"), spaceAfter=4))
    st.add(ParagraphStyle("CardTitle", fontName="PC-Bold", fontSize=11.5, leading=14, textColor=DARK, spaceAfter=4))
    st.add(ParagraphStyle("CardTitleDark", fontName="PC-Bold", fontSize=11.5, leading=14, textColor=colors.white, spaceAfter=4))
    st.add(ParagraphStyle("Metric", fontName="PC-Bold", fontSize=22, leading=24, textColor=RED, alignment=TA_CENTER))
    st.add(ParagraphStyle("MetricDark", fontName="PC-Bold", fontSize=22, leading=24, textColor=colors.white, alignment=TA_CENTER))
    st.add(ParagraphStyle("MetricSmall", fontName="PC-Bold", fontSize=14.2, leading=16.2, textColor=RED, alignment=TA_CENTER))
    st.add(ParagraphStyle("MetricSmallDark", fontName="PC-Bold", fontSize=14.2, leading=16.2, textColor=colors.white, alignment=TA_CENTER))
    st.add(ParagraphStyle("MetricLabel", fontName="PC", fontSize=8, leading=10, textColor=MUTED, alignment=TA_CENTER))
    st.add(ParagraphStyle("MetricLabelDark", fontName="PC", fontSize=8, leading=10, textColor=colors.HexColor("#E8E1DA"), alignment=TA_CENTER))
    st.add(ParagraphStyle("TableHead", fontName="PC-Bold", fontSize=8.3, leading=10, textColor=colors.white))
    return st


def draw_cover(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.drawImage(str(TEAM_COVER), 0, 0, width=w, height=h, mask="auto")
    canvas.setFillColor(colors.Color(0.08, 0.08, 0.09, alpha=0.58))
    canvas.rect(0, 0, w, h, stroke=0, fill=1)
    canvas.drawImage(str(LOGO_WHITE), doc.leftMargin, h - 34 * mm, width=45 * mm, height=9 * mm, mask="auto")
    canvas.setFillColor(RED)
    canvas.rect(doc.leftMargin, h - 48 * mm, 15 * mm, 1.2 * mm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("PC-Bold", 8.5)
    canvas.drawString(doc.leftMargin + 18 * mm, h - 49 * mm, clean("OFERTA DE LANSARE"))
    canvas.setFont("PC", 8)
    canvas.drawRightString(w - doc.rightMargin, 13 * mm, clean("INTELLIGENT DIGITAL MARKETING SRL | 20 iulie 2026"))
    canvas.restoreState()


def draw_cream(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, w, h, stroke=0, fill=1)
    canvas.drawImage(str(LOGO), w - doc.rightMargin - 37 * mm, h - 18 * mm, width=37 * mm, height=7.4 * mm, mask="auto")
    canvas.setFillColor(RED)
    canvas.rect(doc.leftMargin, h - 18 * mm, 13 * mm, 1 * mm, stroke=0, fill=1)
    canvas.setFillColor(MUTED)
    canvas.setFont("PC", 7.5)
    canvas.drawRightString(w - doc.rightMargin, 10 * mm, f"{canvas.getPageNumber():02d}")
    canvas.restoreState()


def draw_dark(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, w, h, stroke=0, fill=1)
    canvas.drawImage(str(LOGO_WHITE), w - doc.rightMargin - 37 * mm, h - 18 * mm, width=37 * mm, height=7.4 * mm, mask="auto")
    canvas.setFillColor(RED)
    canvas.rect(doc.leftMargin, h - 18 * mm, 13 * mm, 1 * mm, stroke=0, fill=1)
    canvas.setFillColor(colors.HexColor("#8B827A"))
    canvas.setFont("PC", 7.5)
    canvas.drawRightString(w - doc.rightMargin, 10 * mm, f"{canvas.getPageNumber():02d}")
    canvas.restoreState()


def doc_template(output_path: Path):
    w, h = A4
    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=27 * mm,
        bottomMargin=18 * mm,
        title=clean("Oferta ProClick pentru ZEILA"),
        author="proClick",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, w - doc.leftMargin - doc.rightMargin, h - doc.topMargin - doc.bottomMargin, id="main")
    doc.addPageTemplates(
        [
            PageTemplate("cover", [frame], onPage=draw_cover),
            PageTemplate("cream", [frame], onPage=draw_cream),
            PageTemplate("dark", [frame], onPage=draw_dark),
        ]
    )
    return doc


def metric_cards(st):
    data = [
        [
            p("10.710 lei TVA inclus<br/><font color='#77706A' size='10'>9.000 lei + TVA</font>", st["MetricSmall"]),
            p("24.290 lei TVA inclus<br/><font color='#E8E1DA' size='10'>20.411,76 lei + TVA</font>", st["MetricSmallDark"]),
            p("35.000 lei TVA inclus<br/><font color='#77706A' size='10'>29.411,76 lei + TVA</font>", st["MetricSmall"]),
        ],
        [p("servicii ProClick", st["MetricLabel"]), p("buget media", st["MetricLabelDark"]), p("investitie totala", st["MetricLabel"])],
    ]
    table = Table(data, colWidths=[50 * mm, 50 * mm, 50 * mm], rowHeights=[24 * mm, 10 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), colors.white),
                ("BACKGROUND", (1, 0), (1, -1), DARK),
                ("BACKGROUND", (2, 0), (2, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return table


def white_card(title, text, st, number=None):
    header = p(f"{number or ''}", st["Eyebrow"]) if number else p("&nbsp;", st["Eyebrow"])
    t = Table([[header], [p(title, st["CardTitle"])], [p(text, st["BodyMuted"])]], colWidths=[50 * mm], rowHeights=[9 * mm, 16 * mm, 34 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("LINEABOVE", (0, 0), (-1, 0), 3, RED),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def service_grid(st):
    cards = [
        white_card("Strategie de lansare", "Pozitionare, funnel, segmentare, calendar 90 zile, directii de mesaj si prioritizare produse.", st, "01"),
        white_card("Audit tracking", "GA4, GTM, Meta Pixel, Shopify events, conversii Google Ads, UTM si calitatea datelor.", st, "02"),
        white_card("Administrare PPC", "Google Search/Shopping/PMax, Meta prospecting si remarketing, catalog ads, creatii statice/video si optimizare spre vanzari.", st, "03"),
        white_card("Optimizare conversii", "Audit UX pentru homepage, colectii, produs, cos si checkout; prioritati CRO cu impact comercial.", st, "04"),
        white_card("Optimizare feed + CSS", "Titluri, categorii, atribute si feed pentru Shopping. Include avantaj CSS Partner: pana la 20% discount aplicabil in Google Shopping.", st, "05"),
        white_card("Raportare consolidata", "Dashboard si raport lunar cu spend, venit, ROAS, POAS, CAC, AOV si produse castigatoare.", st, "06"),
    ]
    return Table([[cards[0], cards[1], cards[2]], [cards[3], cards[4], cards[5]]], colWidths=[52 * mm, 52 * mm, 52 * mm], rowHeights=[64 * mm, 64 * mm], hAlign="LEFT")


def media_table(st):
    rows = [
        [p("Canal", st["TableHead"]), p("Buget", st["TableHead"]), p("Rol", st["TableHead"])],
        [p("Google Ads", st["CardTitle"]), p("40%<br/><b>9.716 lei TVA inclus</b><br/><font color='#77706A' size='8'>8.164,71 lei + TVA</font>", st["Body"]), p("Search brand/non-brand, Shopping/PMax, CSS Partner cu discount de pana la 20% si intentie clara de cumparare.", st["Body"])],
        [p("Meta Ads", st["CardTitle"]), p("60%<br/><b>14.574 lei TVA inclus</b><br/><font color='#77706A' size='8'>12.247,06 lei + TVA</font>", st["Body"]), p("Canal principal pentru social: prospectare vizuala, catalog ads, remarketing, add-to-cart, checkout si validare creativa.", st["Body"])],
    ]
    t = Table(rows, colWidths=[35 * mm, 35 * mm, 84 * mm], repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("LINEBELOW", (0, 0), (-1, 0), 2, RED),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return t


def dark_process(st):
    data = [
        [p("01", st["Eyebrow"]), p("02", st["Eyebrow"]), p("03", st["Eyebrow"])],
        [p("Pregatire", st["CardTitleDark"]), p("Lansare", st["CardTitleDark"]), p("Optimizare", st["CardTitleDark"])],
        [
            p("Audit tracking, Shopify, feed, KPI, produse prioritare si primele directii creative.", st["BodyDark"]),
            p("Google pentru intentie si Meta pentru cerere noua, social proof, catalog ads si remarketing.", st["BodyDark"]),
            p("Buget mutat catre canalele, audientele si produsele vandabile pentru promovare si vanzare.", st["BodyDark"]),
        ],
    ]
    t = Table(data, colWidths=[50 * mm, 50 * mm, 50 * mm], rowHeights=[10 * mm, 16 * mm, 42 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#302B27")),
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#655D55")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#655D55")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def kpi_table(st):
    rows = [
        [p("KPI PPC", st["TableHead"]), p("Ce urmarim in campanii", st["TableHead"])],
        [p("Vizibilitate", st["CardTitle"]), p("Spend, reach, impressions, CPM si frecventa pe audientele principale.", st["Body"])],
        [p("Trafic", st["CardTitle"]), p("CTR, CPC, click-uri, landing page views si calitatea traficului trimis catre Shopify.", st["Body"])],
        [p("Conversii", st["CardTitle"]), p("Add-to-cart, checkout initiated, purchase, cost per purchase si rata de conversie din campanii.", st["Body"])],
        [p("Eficienta", st["CardTitle"]), p("ROAS, valoare conversii, cost per achizitie si buget redistribuit catre campaniile castigatoare.", st["Body"])],
    ]
    t = Table(rows, colWidths=[38 * mm, 116 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("LINEBELOW", (0, 0), (-1, 0), 2, RED),
                ("BACKGROUND", (0, 1), (0, -1), colors.white),
                ("BACKGROUND", (1, 1), (1, -1), colors.HexColor("#FBFAF7")),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def story(st):
    s = []
    s.append(Spacer(1, 75 * mm))
    s.append(p("Oferta de colaborare marketing pentru ZEILA", st["Hero"]))
    s.append(p("Lansare si dezvoltare eCommerce pe Shopify pentru un brand premium de lumanari parfumate, odorizante pentru dulap si decor.", st["HeroSub"]))
    s.append(Spacer(1, 18 * mm))
    s.append(metric_cards(st))
    s.append(Spacer(1, 14 * mm))
    s.append(p("Obiectiv", st["Eyebrow"]))
    s.append(p("Un sistem de crestere masurabil: tracking corect, campanii PPC orientate spre vanzari, optimizare de funnel si raportare clara pentru decizii comerciale.", st["HeroSub"]))
    s.append(NextPageTemplate("cream"))
    s.append(PageBreak())

    s.append(p("Serviciile incluse sunt gandite ca sistem complet de lansare.", st["H1"]))
    s.append(p("Nu operam doar campanii. Aliniem media, tracking, feed, creative si conversie pentru ca bugetul sa lucreze coerent.", st["BodyMuted"]))
    s.append(Spacer(1, 8 * mm))
    s.append(service_grid(st))
    s.append(Spacer(1, 8 * mm))
    s.append(Table([[p("Principiu: acelasi buget devine mai valoros cand deciziile vad aceeasi realitate comerciala.", st["CardTitleDark"])]], colWidths=[154 * mm], rowHeights=[16 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), DARK), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")])) )
    s.append(NextPageTemplate("dark"))
    s.append(PageBreak())

    s.append(p("Strategia de lansare are trei etape.", st["H1Dark"]))
    s.append(p("Pentru ZEILA, prima luna trebuie sa valideze trackingul, mesajele si produsele vandabile pentru promovare si vanzare. Abia dupa aceea crestem presiunea media.", st["BodyDark"]))
    s.append(Spacer(1, 12 * mm))
    s.append(dark_process(st))
    s.append(Spacer(1, 16 * mm))
    s.append(Table([[p("Avantaj pentru client: nu plecam de la setari de campanie, ci de la economie, oferta, continut, feed, conversie, ROAS si POAS.", st["CardTitleDark"])]], colWidths=[154 * mm], rowHeights=[22 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#191716")), ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#655D55")), ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")])) )
    s.append(NextPageTemplate("cream"))
    s.append(PageBreak())

    s.append(p("Alocarea bugetului media.", st["H1"]))
    s.append(p("Bugetul total ramane 35.000 lei TVA inclus: servicii ProClick 9.000 lei + TVA (10.710 lei TVA inclus) si buget media 20.411,76 lei + TVA (24.290 lei TVA inclus).", st["BodyMuted"]))
    s.append(Spacer(1, 8 * mm))
    s.append(media_table(st))
    s.append(Spacer(1, 10 * mm))
    green = Table([[p("Directie de optimizare: dupa primele date, bugetul se muta spre canalele si produsele vandabile, nu doar spre trafic.", st["CardTitle"])]], colWidths=[154 * mm], rowHeights=[18 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), GREEN), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    s.append(green)
    s.append(PageBreak())

    s.append(p("KPI, raportare si mod de lucru.", st["H1"]))
    s.append(kpi_table(st))
    s.append(Spacer(1, 8 * mm))
    s.append(p("Raportare si optimizare", st["Eyebrow"]))
    s.append(p("Raport scurt saptamanal cu evolutia bugetului, concluzii si actiuni efectuate. Raport lunar extins cu rezultate, recomandari de continut, recomandari Shopify/CRO si plan pentru urmatoarea luna.", st["Body"]))
    s.append(p("Intalnire bilunara de aliniere pentru decizii comerciale, prioritizarea canalelor si validarea testelor creative.", st["Body"]))
    s.append(Spacer(1, 5 * mm))
    s.append(p("Shopify si eCommerce", st["Eyebrow"]))
    s.append(p("Colaborarea include verificarea evenimentelor Shopify, feed de produse, structura paginilor de produs, coerenta ofertelor si identificarea blocajelor din cos/checkout. Continutul foto-video realizat intern va fi transformat in variante de reclame si directii de testare.", st["Body"]))
    s.append(Spacer(1, 8 * mm))
    s.append(p("Date companie", st["Eyebrow"]))
    s.append(
        Table(
            [
                [p("Denumire", st["CardTitle"]), p("INTELLIGENT DIGITAL MARKETING SRL", st["Body"])],
                [p("CUI", st["CardTitle"]), p("RO16554762", st["Body"])],
                [p("Adresa", st["CardTitle"]), p("Piata Victoriei nr. 5, Targu-Mures, Romania", st["Body"])],
                [p("Contact", st["CardTitle"]), p("contact@proclick.ro | +40 744 692 880 | proclick.ro", st["Body"])],
            ],
            colWidths=[38 * mm, 116 * mm],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (0, -1), colors.white),
                    ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#FBFAF7")),
                    ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                    ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            ),
        )
    )
    s.append(Spacer(1, 8 * mm))
    s.append(Image(str(LOGO), width=34 * mm, height=6.8 * mm))
    return s


def main():
    parser = argparse.ArgumentParser(description="Generate a ProClick-style commercial offer PDF.")
    parser.add_argument(
        "--output",
        default=str(Path.cwd() / "outputs" / "proclick_price_offer.pdf"),
        help="Output PDF path. Defaults to ./outputs/proclick_price_offer.pdf in the current workspace.",
    )
    args = parser.parse_args()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    register_fonts()
    doc_template(output_path).build(story(make_styles()))
    print(output_path)


if __name__ == "__main__":
    main()
