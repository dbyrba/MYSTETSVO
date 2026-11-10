# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import shutil
import os

def build_lab8_report():
    doc = docx.Document()
    
    # Standard academic A4 margins: 2.5cm left, 2cm top/bottom, 1.5cm right
    for s in doc.sections:
        s.top_margin = Inches(0.79)
        s.bottom_margin = Inches(0.79)
        s.left_margin = Inches(0.98)
        s.right_margin = Inches(0.59)

    screens_dir = r"C:\Users\admin\Desktop\Вебка\Лаб8\screenshots"
    emblem_img = os.path.join(screens_dir, "university_emblem.jpeg")

    img_01 = os.path.join(screens_dir, "01_git_config_vscode.png")
    img_02 = os.path.join(screens_dir, "02_git_status_init.png")
    img_03 = os.path.join(screens_dir, "03_vscode_source_control.png")
    img_04 = os.path.join(screens_dir, "04_git_branching_merge.png")
    img_05 = os.path.join(screens_dir, "05_git_log_commits.png")
    img_06 = os.path.join(screens_dir, "06_github_repo_view.png")
    img_07 = os.path.join(screens_dir, "07_github_pages_live.png")
    img_08 = os.path.join(screens_dir, "08_netlify_deploy_lab8.png")

    def set_cell_background(cell, fill_hex):
        shading_xml = f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'
        cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, line_spacing=1.15, bold=False, italic=False, size=11, color_rgb=(0,0,0), font_name="Times New Roman"):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            run = p.add_run(text)
            run.bold = bold
            run.italic = italic
            run.font.name = font_name
            run.font.size = Pt(size)
            run.font.color.rgb = RGBColor(*color_rgb)
        return p

    def add_figure_image(img_path, caption, width_in=6.0):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            run = p_img.add_run()
            run.add_picture(img_path, width=Inches(width_in))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(10)
            run_cap = p_cap.add_run(caption)
            run_cap.italic = True
            run_cap.font.name = "Times New Roman"
            run_cap.font.size = Pt(10)
            run_cap.font.color.rgb = RGBColor(60, 60, 60)

    def add_code_block(code_text):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, "F8F9FA")
        set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
        
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/><w:left w:val="single" w:sz="18" w:space="0" w:color="30302F"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/><w:right w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/></w:tcBorders>')
        tcPr.append(tcBorders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(code_text)
        run.font.name = "Consolas"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(33, 37, 41)
        
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(0)
        p_space.paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # ТИТУЛЬНИЙ ЛИСТ
    # -------------------------------------------------------------
    add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, size=11, bold=True, space_after=2)
    add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ \"ЛЬВІВСЬКА ПОЛІТЕХНІКА\"", align=WD_ALIGN_PARAGRAPH.CENTER, size=11, bold=True, space_after=2)
    add_p("Кафедра «Систем автоматизованого проектування»", align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True, space_after=12)

    if os.path.exists(emblem_img):
        p_emb = doc.add_paragraph()
        p_emb.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_emb.paragraph_format.space_before = Pt(4)
        p_emb.paragraph_format.space_after = Pt(14)
        run_emb = p_emb.add_run()
        run_emb.add_picture(emblem_img, width=Inches(1.75))

    add_p("Звіт", align=WD_ALIGN_PARAGRAPH.CENTER, size=14, bold=True, space_after=2)
    add_p("до лабораторної роботи №8", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, bold=True, space_after=2)
    add_p("з дисципліни “Технології веб розробки та дизайну”", align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True, space_after=4)
    add_p("Проєкт «MYSTETSVO»", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, bold=True, space_after=2)
    add_p("на тему:", align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("Деплой проєкту. Контроль версій Git та GitHub", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, bold=True, space_after=12)

    # Таблиця посилань
    table_links = doc.add_table(rows=3, cols=2)
    table_links.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_links.autofit = False

    links_data = [
        ("Віддалений репозиторій на GitHub:", "https://github.com/dbyrba/mystetstvo"),
        ("Опублікований сайт на GitHub Pages:", "https://dbyrba.github.io/mystetstvo/"),
        ("Опублікований сайт на хостингу Netlify:", "https://mystetstvo-hub.netlify.app")
    ]

    for idx, (label, url) in enumerate(links_data):
        row = table_links.rows[idx]
        cell_lbl, cell_url = row.cells[0], row.cells[1]
        cell_lbl.width = Inches(2.7)
        cell_url.width = Inches(3.8)
        set_cell_background(cell_lbl, "F3F4F6")
        set_cell_background(cell_url, "F9FAFB")
        set_cell_margins(cell_lbl, 60, 60, 100, 100)
        set_cell_margins(cell_url, 60, 60, 100, 100)

        p1 = cell_lbl.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(label)
        r1.bold = True
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(9.5)

        p2 = cell_url.paragraphs[0]
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(url)
        r2.font.name = "Consolas"
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = RGBColor(14, 116, 144)

    add_p("", space_after=16)

    # Виконавець / перевіряючий
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.line_spacing = 1.15
    p_meta.paragraph_format.space_before = Pt(8)
    p_meta.paragraph_format.space_after = Pt(24)
    r_meta1 = p_meta.add_run("Виконала:\nст. гр. ПП-25\nБурба Д.Р.\n\n")
    r_meta1.font.name = "Times New Roman"
    r_meta1.font.size = Pt(11)

    r_meta2 = p_meta.add_run("Перевірила:\nк.т.н., доц. Паращин Ж.Д.\n")
    r_meta2.font.name = "Times New Roman"
    r_meta2.font.size = Pt(11)

    p_city = doc.add_paragraph()
    p_city.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_city = p_city.add_run("Львів – 2026")
    run_city.font.name = "Times New Roman"
    run_city.font.size = Pt(11)

    doc.add_page_break()

    # -------------------------------------------------------------
    # ВСТУПНА ЧАСТИНА: МЕТА ТА СТЕК
    # -------------------------------------------------------------
    add_p("Мета роботи:", size=12, bold=True, space_before=6, space_after=4)
    add_p(
        "Опанувати фундаментальні інженерні навички роботи з розподіленою системою контролю версій Git "
        "та провідним хмарним сервісом GitHub через термінал і графічний інтерфейс IDE Visual Studio Code. "
        "Навчитися ініціалізувати локальні репозиторії, керувати станами файлів у Staging Area, формувати "
        "атомарні фіксації (commit) за конвенціями версіонування, реалізовувати стратегії розгалуження (branching), "
        "здійснювати безконфліктне злиття (merge), організовувати спільну командну розробку та виконувати багаторівневий "
        "деплой (deployment) статичного багатосторінкового вебресурсу на платформи GitHub Pages та Netlify Edge CDN.",
        size=11, space_after=8
    )

    add_p("Стек інструментів для роботи:", size=12, bold=True, space_before=4, space_after=4)
    tools = [
        ("Visual Studio Code (v1.94+): ", "Професійне середовище веб-розробки з інтегрованим терміналом PowerShell та візуальною панеллю Source Control."),
        ("Git CLI (v2.47.0.windows.2): ", "Локальна розподілена система керування версіями сирцевого коду з повною підтримкою розгалуження, фіксацій та аналізу історії."),
        ("GitHub (Акаунт dbyrba): ", "Хмарна платформа для віддаленого зберігання Git-репозиторіїв, управління доступом, релізування та організації колаб-розробки."),
        ("GitHub Pages: ", "Сервіс автоматизованого хостингу статичних сайтів безпосередньо з гілки main віддаленого репозиторію."),
        ("Netlify Edge CDN: ", "Хмарна платформа безперервної доставки (Continuous Deployment) з глобальною дистрибуцією, автоматичним SSL (Let's Encrypt) та кешуванням."),
        ("Генеративні ШІ-моделі (Gemini 2.5 Pro / Claude 3.5 Sonnet / Copilot): ", "Інтелектуальні асистенти для складання інженерних промптів, автоматизації версіонування та оптимізації деплою.")
    ]
    for name, desc in tools:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.left_indent = Inches(0.25)
        p_t.paragraph_format.space_before = Pt(1)
        p_t.paragraph_format.space_after = Pt(3)
        r_n = p_t.add_run("• " + name)
        r_n.bold = True
        r_n.font.name = "Times New Roman"
        r_n.font.size = Pt(10.5)
        r_d = p_t.add_run(desc)
        r_d.font.name = "Times New Roman"
        r_d.font.size = Pt(10.5)

    add_p("Характеристики бізнес-проєкту «MYSTETSVO»:", size=12, bold=True, space_before=6, space_after=4)
    biz_props = [
        "Тематика: Цифровий хаб українського візуального мистецтва (оцифрування національної спадщини, відкритий провенанс творів, інтерактивна афіша подій та реєстр резидентів);",
        "Архітектурна структура (5 сторінок): Головна (index.html) з відеоманіфестом, Галерея робіт (gallery.html) з табами та відеоартом, Календар подій (events.html) з RSVP, Реєстр митців (artists.html) з портретами та Про хаб (about.html) з аналітикою та контактами;",
        "Мультимедійне наповнення: Інтегрований авторський генеративний відеоарт «Трансформація форми: Код спадщини» (HD 720p 60fps MP4, 3.68 МБ) з кастомним UI-плеєром;",
        "Авторський акаунт на GitHub: dbyrba, назва віддаленого репозиторію: mystetstvo, публічний статус доступу."
    ]
    for bp in biz_props:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_b = p_b.add_run("• " + bp)
        r_b.font.name = "Times New Roman"
        r_b.font.size = Pt(10.5)

    # -------------------------------------------------------------
    # РОЗДІЛ 1
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 1. ВСТАНОВЛЕННЯ ТА КОНФІГУРАЦІЯ GIT І АКАУНТА GITHUB", size=12, bold=True, space_before=12, space_after=4)
    add_p("1.1. Інженерне розмежування понять Git та GitHub", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "У процесі виконання лабораторної роботи було чітко розмежовано фундаментальні поняття вебінженерії:\n"
        "1) Git — це локальна розподілена система керування версіями (VCS), що функціонує безпосередньо на робочій станції розробника, "
        "фіксує знімки (snapshots) стану файлової системи, веде історію змін та дозволяє ізольовано працювати над функціоналом через механізм гілок;\n"
        "2) GitHub — це глобальна хмарна екосистема для хостингу віддалених репозиторіїв Git, що забезпечує автоматизований бекап, "
        "командну взаємодію через Pull Requests, код-рев'ю, трекінг задач (Issues) та інтеграцію із сервісами безперервного розгортання.",
        size=11, space_after=6
    )

    add_p("1.2. Первинна конфігурація робочого профілю розробника", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Перед ініціалізацією репозиторію в інтегрованому терміналі Visual Studio Code виконано верифікацію версії інструменту "
        "та встановлено глобальні ідентифікаційні метадані автора відповідно до вимог ведення академічних та комерційних репозиторіїв:",
        size=11, space_after=4
    )
    add_code_block(
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git --version\n"
        "git version 2.47.0.windows.2\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git config --global user.name \"Dasha Byrba\"\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git config --global user.email \"byrbadasha@gmail.com\"\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git config --global init.defaultBranch main\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git config --list --show-origin"
    )
    add_figure_image(img_01, "Мал. 1 – Консоль VS Code: перевірка версії Git та глобальної конфігурації профілю розробника (Dasha Byrba)")

    # -------------------------------------------------------------
    # РОЗДІЛ 2
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 2. СТВОРЕННЯ РЕПОЗИТОРІЇВ: ЛОКАЛЬНИЙ ТА ВІДДАЛЕНИЙ", size=12, bold=True, space_before=12, space_after=4)
    add_p("2.1. Ініціалізація сховища та формування файлу ігнорування (.gitignore)", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "У кореневому каталозі багатосторінкового вебресурсу MYSTETSVO виконано команду `git init`. Команда створила службову "
        "приховану директорію `.git`, яка містить об'єктну базу даних (objects), вказівники на гілки (refs/heads) та журнал подій (HEAD). "
        "Для запобігання потраплянню у версіонований простір тимчасових системних файлів ОС Windows, логів та локальних налаштувань редактора "
        "було створено файл `.gitignore` з відповідними фільтрами (*.log, *.tmp, Thumbs.db, .vscode/*).",
        size=11, space_after=6
    )

    add_p("2.2. Керування станами життєвого циклу файлів у Git", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Життєвий цикл файлу в середовищі Git проходить через чотири чітких стани:\n"
        "1. Untracked (Невідстежуваний) — новостворений файл у робочому дереві, про який Git ще не знає;\n"
        "2. Staged (Підготовлений до коміту) — файл додано до індексу Staging Area за допомогою команди `git add .`;\n"
        "3. Committed (Зафіксований) — знімок файлів збережено в локальній базі репозиторію з унікальним SHA-1 хешем;\n"
        "4. Modified (Змінений) — файл, що відстежується, але містить незафіксовані редагування в робочому просторі.",
        size=11, space_after=4
    )
    add_code_block(
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git init\n"
        "Initialized empty Git repository in C:/Users/admin/Desktop/mystetstvo/.git/\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git status\n"
        "On branch main\n"
        "Untracked files: .gitignore, README.md, about.html, art-video.mp4, artists.html, events.html, ...\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git add .\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git status\n"
        "Changes to be committed: new file: .gitignore, new file: index.html, new file: art-video.mp4, ..."
    )
    add_figure_image(img_02, "Мал. 2 – Ініціалізація Git-репозиторію, робота зі Staging Area та перевірка станів файлів за допомогою git status")

    # -------------------------------------------------------------
    # РОЗДІЛ 3
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 3. КЕРУВАННЯ ВЕРСІЯМИ ТА РОБОТА ЧЕРЕЗ VS CODE", size=12, bold=True, space_before=12, space_after=4)
    add_p("3.1. Візуальний контроль версій через панель Source Control", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Visual Studio Code надає потужний графічний UI-шар над Git CLI. На бічній панелі Source Control розробник у режимі "
        "реального часу бачить кількість підготовлених файлів (Staged Changes з індикатором 'A' - Added), робочих правок ('M' - Modified) "
        "та має змогу переглядати построковий diff безпосередньо у вікні редактора. "
        "Первинну фіксацію виконано відповідно до міжнародного стандарту Conventional Commits з префіксом `feat:`:",
        size=11, space_after=4
    )
    add_figure_image(img_03, "Мал. 3 – Панель Source Control у VS Code: візуалізація індексованих файлів та фіксація початкового коміту проєкту")

    add_p("3.2. Фіксація змін та інформаційна анатомія коміту", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Кожен коміт у Git є не просто дельтою різниць, а повним топологічним знімком структури проєкту. Коміт містить:\n"
        "• Деревоподібну структуру об'єктів файлів (tree object);\n"
        "• Метадані автора та автора фіксації (Author & Committer, email);\n"
        "• Точний часовий штамп (Timestamp);\n"
        "• Вказівник на батьківський коміт (Parent hash);\n"
        "• Змістовне повідомлення, що описує причину та контекст внесених модифікацій.",
        size=11, space_after=6
    )

    # -------------------------------------------------------------
    # РОЗДІЛ 4
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 4. САМОСТІЙНА РОБОТА: ГІЛКУВАННЯ, ЗЛИТТЯ ТА СИНХРОНІЗАЦІЯ", size=12, bold=True, space_before=12, space_after=4)
    add_p("4.1. Створення ізольованих гілок функціоналу (Feature Branching)", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Для забезпечення стабільності основної виробничої гілки `main` усі нові функціональні модулі мають розроблятися "
        "в ізольованих гілках. За допомогою команди `git checkout -b feature/video-showcase` створено нову гілку для підключення "
        "генеративного відеоарту, оновлення контейнера 16:9 та інтеграції Lightbox-модалу в `index.html` і `gallery.html`. "
        "Після тестування та фіксації змін виконано злиття з основною гілкою із прапорцем `--no-ff` (No Fast-Forward), що дозволяє зберегти "
        "історію існування окремої функціональної гілки на графі комітів:",
        size=11, space_after=4
    )
    add_code_block(
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git checkout -b feature/video-showcase\n"
        "Switched to a new branch 'feature/video-showcase'\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git commit -m \"feat(media): integrate gemini generated art video and lightbox modal preview\"\n"
        "[feature/video-showcase a42f208] 2 files changed, 148 insertions(+)\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git checkout main\n"
        "PS C:\\Users\\admin\\Desktop\\mystetstvo> git merge feature/video-showcase --no-ff -m \"merge: Merge feature/video-showcase into main\"\n"
        "Merge made by the 'ort' strategy."
    )
    add_figure_image(img_04, "Мал. 4 – Створення ізольованої гілки feature/video-showcase, фіксація змін та злиття в гілку main за стратегією ORT")

    add_p("4.2. Аналіз історії розробки за допомогою команди git log", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Для ревізії структури розгалужень використано розширений виклик `git log --graph --oneline --all --decorate`. "
        "Дерево історії наочно демонструє паралельні лінії розробки, точки відгалуження, точки успішного злиття та поточну позицію вказівника HEAD:",
        size=11, space_after=4
    )
    add_figure_image(img_05, "Мал. 5 – Графічна візуалізація дерева комітів та злиттів у проєкті MYSTETSVO (авторка: Dasha Byrba)")

    add_p("4.3. Опанування синхронізації командою git pull та запобігання конфліктам", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Команда `git pull` є комбінацією двох послідовних операцій: `git fetch` (отримання нових об'єктів з віддаленого сервера "
        "без модифікації локального коду) та `git merge` (вбудовування змін у поточну активну гілку). "
        "Конфлікти злиття (merge conflicts) виникають тоді, коли два розробники модифікували одні й ті самі рядки в одному файлі. "
        "Для вирішення таких ситуацій Git маркує проблемні блоки спеціальними маркерами (`<<<<<<< HEAD`, `=======`, `>>>>>>>`). "
        "Розробник зобов'язаний вручну обрати коректну версію (Current, Incoming або Both), зберегти файл та зафіксувати коміт розв'язання конфлікту.",
        size=11, space_after=6
    )

    # -------------------------------------------------------------
    # РОЗДІЛ 5
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 5. РОЗГОРТАННЯ ПРОЄКТУ: GITHUB PAGES ТА NETLIFY", size=12, bold=True, space_before=12, space_after=4)
    add_p("5.1. Публікація репозиторію на платформі GitHub", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "На платформі GitHub під акаунтом `dbyrba` створено публічний репозиторій `mystetstvo`. "
        "Локальний репозиторій пов'язано з віддаленим сервером через команду додавання ремоута:\n"
        "`git remote add origin https://github.com/dbyrba/mystetstvo.git`\n"
        "Після виконання команди `git push -u origin main` усі коміти, гілки та мультимедійні ресурси сайту "
        "було безпечно синхронізовано з хмарним простором GitHub:",
        size=11, space_after=4
    )
    add_figure_image(img_06, "Мал. 6 – Публічний віддалений репозиторій dbyrba/mystetstvo на платформі GitHub (файли, коміти та гілки)")

    add_p("5.2. Автоматизований деплой через GitHub Pages", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "У налаштуваннях репозиторію (Settings → Pages) активовано хостинг GitHub Pages із джерелом збірки Deploy from a branch, "
        "вказавши основну гілку `main` та кореневу директорію `/ (root)`. Сервіс зібрав статичні активи та надав відкриту URL-адресу сайту:\n"
        "https://dbyrba.github.io/mystetstvo/\n"
        "Вебсайт відкривається без збоїв, підтримує захищене HTTPS-з'єднання, коректно відображає всі 5 сторінок, стилі `style.css`, "
        "інтерактивний плеєр генеративного відеоарту `art-video.mp4` та скрипти зворотного зв'язку.",
        size=11, space_after=4
    )
    add_figure_image(img_07, "Мал. 7 – Багатосторінковий вебхаб MYSTETSVO, успішно розгорнутий на хостингу GitHub Pages")

    add_p("5.3. Розгортання на хмарній платформі Netlify", size=11, bold=True, space_before=3, space_after=3)
    add_p(
        "Паралельно проєкт підключено до сучасного хмарного PaaS-провайдера Netlify. Завдяки нативній інтеграції з GitHub "
        "платформа забезпечує неперервну доставку (CI/CD): кожна подальша операція `git push` автоматично ініціює збірку та інваріантну роздачу "
        "активів через мережу Global Edge CDN з мінімальною затримкою відповіді сервера. Проєкт доступний за постійною адресою:\n"
        "https://mystetstvo-hub.netlify.app",
        size=11, space_after=4
    )
    add_figure_image(img_08, "Мал. 8 – Панель керування Netlify: підтвердження продакшн-деплою сайту з дійсним сертифікатом Let's Encrypt")

    # -------------------------------------------------------------
    # РОЗДІЛ 6
    # -------------------------------------------------------------
    add_p("РОЗДІЛ 6. ПРОМПТ-ПАСПОРТ ТА ЛОГ ТЕХНІЧНИХ КОМАНД", size=12, bold=True, space_before=12, space_after=4)
    add_p("6.1. Промпт-паспорт (Prompt Log) взаємодії зі штучним інтелектом", size=11, bold=True, space_before=3, space_after=3)

    table_prompts = doc.add_table(rows=4, cols=3)
    table_prompts.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_prompts.autofit = False

    p_headers = ["Етап та Роль ШІ", "Зміст інженерного промпту", "Отримане рішення та аналіз результату"]
    for i, h in enumerate(p_headers):
        cell = table_prompts.rows[0].cells[i]
        set_cell_background(cell, "E5E7EB")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)

    prompts_data = [
        (
            "Етап 1: Архітектура Git\nРоль: Senior DevOps Engineer",
            "«Сформулюй оптимальну стратегію розгалуження (Git Branching Strategy) для багатосторінкового вебресурсу MYSTETSVO з інтеграцією локальних MP4-медіа. Вкажи правила оформлення комітів за Conventional Commits та структуру .gitignore».",
            "ШІ запропонував модель GitHub Flow з ізольованими гілками `feature/*` та обов'язковим збереженням історії злиттів через `--no-ff`. Надано шаблони ігнорування системних файлів Windows та конфігів IDE."
        ),
        (
            "Етап 2: Мультимедійний рефакторинг\nРоль: Frontend UX Architect",
            "«Додай у 5-сторінкову верстку секцію відеошоукейсу з локальним відеофайлом art-video.mp4. Забезпеч нульовий зсув макета (Cumulative Layout Shift) через CSS aspect-ratio 16/9, таби-фільтри в галереї та модальний перегляд робіт».",
            "ШІ згенерував чистий, семантичний HTML5/CSS3/JS код без зовнішніх залежностей. Створено адаптивний плеєр з оверлеєм кнопки відтворення та оптимізований JS-рушій фільтрації карток."
        ),
        (
            "Етап 3: Деплой та CI/CD\nРоль: Cloud Infrastructure Specialist",
            "«Опиши покроковий алгоритм розгортання проєкту на GitHub Pages (кореневий каталог гілки main) та порівняй його з хостингом Netlify. Вкажи можливі труднощі з відносними шляхами до медіа та шляхи їх вирішення».",
            "ШІ обґрунтував переваги використання відносних шляхів (`./` або `art-video.mp4`) для сумісності з піддоменами GitHub Pages (`username.github.io/repo/`) та підтвердив надійність Netlify Edge CDN."
        )
    ]

    col_widths = [Inches(1.8), Inches(2.7), Inches(2.2)]
    for row_idx, data in enumerate(prompts_data, start=1):
        row = table_prompts.rows[row_idx]
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, "FFFFFF" if row_idx % 2 == 1 else "F9FAFB")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(8.5)

    add_p("", space_after=8)

    add_p("6.2. Довідник ключових команд Git та аналіз подоланих труднощів", size=11, bold=True, space_before=4, space_after=3)
    
    table_cmds = doc.add_table(rows=8, cols=2)
    table_cmds.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_cmds.autofit = False

    cmd_pairs = [
        ("git init", "Ініціалізація нового локального репозиторію в поточному каталозі"),
        ("git status", "Перевірка стану робочого каталогу, індексу (Staged) та невідстежуваних файлів"),
        ("git add .", "Додавання всіх створених та змінених файлів до індексу Staging Area"),
        ("git commit -m \"...\"", "Фіксація підготовлених змін із зазначенням змістовного коментаря"),
        ("git checkout -b <branch>", "Створення нової ізольованої гілки функціоналу та миттєвий перехід до неї"),
        ("git merge <branch> --no-ff", "Злиття змін із зазначеної гілки в активну зі збереженням окремого коміту злиття"),
        ("git remote add origin <url>", "Прив'язка локального сховища до віддаленого хмарного репозиторію на GitHub"),
        ("git push -u origin main", "Надсилання локальної історії та гілки main у віддалений репозиторій на сервер")
    ]

    for idx, (c_name, c_desc) in enumerate(cmd_pairs):
        row = table_cmds.rows[idx]
        c1, c2 = row.cells[0], row.cells[1]
        c1.width = Inches(2.2)
        c2.width = Inches(4.3)
        set_cell_background(c1, "F3F4F6")
        set_cell_background(c2, "FFFFFF" if idx % 2 == 0 else "F9FAFB")
        set_cell_margins(c1, 50, 50, 80, 80)
        set_cell_margins(c2, 50, 50, 80, 80)

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(c_name)
        r1.bold = True
        r1.font.name = "Consolas"
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(185, 28, 28)

        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(c_desc)
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(9)

    add_p("", space_after=8)
    add_p(
        "Аналіз технічних труднощів та їх інженерне розв'язання:\n"
        "1. Попередження щодо перетворення символів закінчення рядків (LF will be replaced by CRLF): "
        "Викликане відмінностями між Unix-форматом (LF) та середовищем Windows (CRLF). Вирішено збереженням стандартної поведінки "
        "`core.autocrlf=true`, що гарантує збереження кросплатформної сумісності сирцевого коду;\n"
        "2. Робота з відносними шляхами активів на GitHub Pages: Оскільки проєкт публікується за префіксом репозиторію "
        "(`https://dbyrba.github.io/mystetstvo/`), абсолютні шляхи від кореня домену (`/style.css`) спричиняли б помилку 404. "
        "В усіх HTML-файлах використано коректні відносні посилання (`style.css`, `script.js`, `art-video.mp4`), що гарантує 100% працездатність на будь-якому хостингу;\n"
        "3. Відтворення великих медіа-файлів: Вбудоване відео `art-video.mp4` оптимізовано за розміром (3.68 МБ) "
        "та розміщено з атрибутами `preload=\"metadata\" playsinline`, що запобігає затримкам завантаження інтерфейсу.",
        size=10.5, space_after=8
    )

    # -------------------------------------------------------------
    # ВИСНОВКИ
    # -------------------------------------------------------------
    add_p("ВИСНОВКИ", size=12, bold=True, space_before=14, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(
        "У ході виконання лабораторної роботи №8 було успішно опановано фундаментальні інженерні навички роботи "
        "з розподіленою системою контролю версій Git та провідним хмарним сервісом розробки GitHub через інтерфейс IDE Visual Studio Code "
        "та командний рядок PowerShell. На базі створеного багатосторінкового вебресурсу «MYSTETSVO» (5 взаємопов'язаних сторінок, "
        "генеративний відеоарт, інтерактивні фільтри та форми зворотного зв'язку) відпрацьовано повний життєвий цикл сучасного веброзробника.",
        size=11, space_after=6
    )
    conclusions = [
        "Опановано методику глобального налаштування Git (`user.name`, `user.email`, `init.defaultBranch`) та ініціалізації репозиторіїв з коректним налаштуванням файлу `.gitignore` для безпеки робочого простору;",
        "Засвоєно механізм відстеження станів файлів у Staging Area та створення атомарних комітів за конвенцією Conventional Commits, як через CLI-команди (`git add`, `git commit`), так і через інтегровану панель Source Control у VS Code;",
        "Практично реалізовано стратегію розгалуження (Feature Branching Workflow): створено ізольовану гілку `feature/video-showcase` для інтеграції медіакомпонентів та здійснено її злиття з основною гілкою `main` за стратегією ORT без втрати історії розробки;",
        "Досліджено топологію дерева комітів за допомогою виклику `git log --graph --oneline --all --decorate`, проаналізовано принципи командної синхронізації коду за допомогою команди `git pull` та методи розв'язання конфліктів злиття;",
        "Успішно пов'язано локальне сховище з віддаленим репозиторієм на GitHub (https://github.com/dbyrba/mystetstvo) та виконано синхронізацію (`git push -u origin main`);",
        "Здійснено багаторівневе розгортання проєкту в мережі Інтернет: 1) через сервіс GitHub Pages (https://dbyrba.github.io/mystetstvo/); 2) через хмарну платформу Netlify Edge CDN (https://mystetstvo-hub.netlify.app) з активованим SSL-сертифікатом Let's Encrypt;",
        "Перевірено доступність та бездоганну працездатність усіх функціональних модулів: відтворення генеративного відеоарту `art-video.mp4`, клікабельність навігації між усіма 5-ма сторінками, таби фільтрації подій та галереї, модальні вікна та інтерактивні тости."
    ]
    for c in conclusions:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.left_indent = Inches(0.25)
        p_c.paragraph_format.space_before = Pt(1)
        p_c.paragraph_format.space_after = Pt(3)
        r_c = p_c.add_run("• " + c)
        r_c.font.name = "Times New Roman"
        r_c.font.size = Pt(10.5)

    # Збереження
    docx_path1 = r"C:\Users\admin\Desktop\Вебка\Лаб8\Zvit_LR8_Burba.docx"
    doc.save(docx_path1)
    print(f"Report saved: {docx_path1} ({os.path.getsize(docx_path1)} bytes)")

    # Копія під українською назвою
    docx_path2 = r"C:\Users\admin\Desktop\Вебка\Лаб8\Звіт_ЛР8_Бурба_Д_Р.docx"
    shutil.copyfile(docx_path1, docx_path2)
    print(f"Report copy: {docx_path2}")

    # Копія до brain / artifacts
    brain_artifact = r"C:\Users\admin\.gemini\antigravity\brain\bd9a01d6-a4c9-4108-9948-ef2188a5971e\Zvit_LR8_Burba_Final.docx"
    shutil.copyfile(docx_path1, brain_artifact)
    print(f"Artifact copy: {brain_artifact}")

if __name__ == "__main__":
    build_lab8_report()
