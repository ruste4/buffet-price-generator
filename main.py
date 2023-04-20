from fpdf import FPDF

pageW = 918
pageH = 691
color = (232, 99, 82)
pdf = FPDF(format=(pageW, pageH), unit="mm")
pdf.add_font("BebasNeue", "", "./BebasNeueBold.ttf", uni=True)


def draw_background(book: FPDF, bg_color: tuple):
    book.set_line_width(1)
    book.set_fill_color(bg_color[0], bg_color[1], bg_color[2])
    book.rect(0, 0, pageW, pageH, 'F')


def draw_title(book: FPDF, txt: str):
    book.set_font("BebasNeue", size=290)
    book.set_text_color(255, 255, 255)
    book.set_xy(67, 50)
    book.multi_cell(pageW - 200, 115, txt, 0, "L")


def draw_circle(book: FPDF):
    book.set_fill_color(255, 255, 255)
    book.ellipse(540, 299, 413, 413, 'F')


def draw_logo(book: FPDF):
    book.image("./bg/buffet_logo.png", h=50, w=201, x=70, y=560)


def draw_price(book: FPDF, price: str):
    book.set_font("BebasNeue", size=451)
    book.set_text_color(0, 0, 0)
    book.set_xy(129, 427)
    book.multi_cell(pageW - 200, 115, price, 0, "R")


def create_page(bg_color: tuple, title: str, price: str):
    pdf.add_page()
    draw_background(pdf, bg_color)
    draw_title(pdf, title)
    draw_circle(pdf)
    draw_price(pdf, price)
    draw_logo(pdf)


pdf.output("simple_demo.pdf")
