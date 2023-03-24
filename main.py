from tkinter import Label, Text, Button, Tk, END, PhotoImage
from PIL import Image
import textwrap
import time
import os


img_list = []
og_img_list = []
curr_count = 0
scan_img_list = []
temp_bool = 1


def save_pdf():
    global img_list

    pdf_lbl = Label(root, text='Pdf Saved', relief='solid',
                    font=("Comic Sans MS", 9))
    pdf_lbl.place(x=1050, y=740)
    pdf_lbl.after(5000, pdf_lbl.destroy)

    if img_list != []:

        image1 = img_list[0]
        img_list.remove(image1)

        image1.save(r'Images_to_PDF.pdf', save_all=True,
                    append_images=img_list)


def save_pdf_scan():
    global scan_img_list

    pdf_lbl_scan = Label(root, text='Scan Pdf Saved', relief='solid',
                         font=("Comic Sans MS", 9))
    pdf_lbl_scan.place(x=1135, y=740)
    pdf_lbl_scan.after(5000, pdf_lbl_scan.destroy)

    if scan_img_list != []:

        image1 = scan_img_list[0]
        scan_img_list.remove(image1)

        image1.save(r'Images_to_Scan_PDF.pdf', save_all=True,
                    append_images=scan_img_list)


def save_img():

    global img_list, og_img_list, curr_count

    saved_lbl = Label(root, text='Image Saved',
                      relief='solid', font=("Comic Sans MS", 9))
    saved_lbl.place(x=940, y=740)
    saved_lbl.after(5000, saved_lbl.destroy)

    ctime = time.strftime("%d-%m-%y_%H-%M-%S")

    try:
        os.rename(r'temp_text_to_handwriting.png',
                  r'text_to_handwriting_{}.png'.format(ctime))

        img_list.append(Image.open(
            r'text_to_handwriting_{}.png'.format(ctime)).convert('RGB'))
        og_img_list.append(
            r'text_to_handwriting_{}.png'.format(ctime))
        scan_img_list.append(Image.open(
            r'text_to_handwriting_{}.png'.format(ctime)).convert('L'))

    except:
        print("Error!")

    if curr_count != len(og_img_list)-1:
        next_icon = PhotoImage(file=r'images\next_40x50.png')
        next_btn = Button(root, image=next_icon, relief='flat',
                          bg='#6999fa', command=goto_next_page)
        next_btn.photo = next_icon
        next_btn.place(x=1320, y=355)

    if len(og_img_list) != 1:
        prev_icon = PhotoImage(file=r'images\prev_40x50.png')
        prev_btn = Button(root, image=prev_icon, relief='flat', bg='#6999fa',
                          command=lambda: goto_prev_page(len(og_img_list)-1))
        prev_btn.photo = prev_icon
        prev_btn.place(x=750, y=355)

    pdf_icon = PhotoImage(file=r'images\pdf_icon_50x50.png')

    pdf_btn = Button(root, image=pdf_icon, bg='#6999fa',
                     command=save_pdf, borderwidth=0, relief='flat')
    pdf_btn.photo = pdf_icon
    pdf_btn.place(x=1050, y=665)

    pdf_icon_scan = PhotoImage(file=r'images\pdf_icon_scan.png')

    pdf_btn_scan = Button(root, image=pdf_icon_scan, bg='#6999fa',
                          command=save_pdf_scan, borderwidth=0, relief='flat')
    pdf_btn_scan.photo = pdf_icon_scan
    pdf_btn_scan.place(x=1150, y=665)


def goto_next_page():
    global og_img_list, curr_count

    if curr_count != len(og_img_list) - 1:
        img = PhotoImage(file=og_img_list[curr_count+1])
        curr_count = curr_count + 1
    else:
        img = PhotoImage(file=og_img_list[curr_count])

    final_img = Label(root, image=img, borderwidth=3, relief="flat")
    final_img.photo = img
    final_img.place(x=800, y=20)


def goto_prev_page(count):
    global og_img_list, curr_count, temp_bool

    if temp_bool == 1:
        img = PhotoImage(file=og_img_list[count-1])
        curr_count = count - 1
        temp_bool = 0
    else:
        if curr_count != 0:
            img = PhotoImage(file=og_img_list[curr_count-1])
            curr_count = curr_count - 1
        else:
            img = PhotoImage(file=og_img_list[curr_count])

    final_img = Label(root, image=img, borderwidth=3, relief="flat")
    final_img.photo = img
    final_img.place(x=800, y=20)


def convert_press():
    global temp_bool

    temp_bool = 1

    text = text_area.get('1.0', END)
    #text = text.replace('\n', '~')

    main_img = Image.open("images\lined_paper.png")

    text = '\n'.join(textwrap.wrap(
        text, 33, break_long_words=False)).replace('\n', '~')
    text = ' ' + text

    x = 60
    y = 92

    line_no = 1

    for i in range(len(text)):

        if text[i] == ' ':
            img2 = Image.open('images\my_fonts\\space.png')
        elif text[i] == '*':
            img2 = Image.open('images\my_fonts\\star.png')
        elif text[i] == '|':
            img2 = Image.open('images\my_fonts\\vbar.png')
        elif text[i] in "\ ":
            img2 = Image.open('images\my_fonts\\bslash.png')
        elif text[i] in "/":
            img2 = Image.open('images\my_fonts\\slash.png')
        elif text[i] == '<':
            img2 = Image.open('images\my_fonts\\abrace1.png')
        elif text[i] == '?':
            img2 = Image.open('images\my_fonts\\qmark.png')
        elif text[i] == '>':
            img2 = Image.open('images\my_fonts\\abrace2.png')
        elif text[i] == '"':
            img2 = Image.open('images\my_fonts\\quotation.png')
        elif text[i] == ':':
            img2 = Image.open('images\my_fonts\\colon.png')
        elif text[i] == ".":
            img2 = Image.open('images\my_fonts\\dot.png')
        elif text[i] == "~":
            y = y + 20
            x = 60
            line_no = line_no + 1

            if line_no == 4:
                y = y + 3
            if line_no == 7:
                y = y + 2
            if line_no == 11:
                y = y + 2
            if line_no == 15:
                y = y + 2
            if line_no == 19:
                y = y + 2
            if line_no == 22:
                y = y + 2
        elif text[i].isupper():
            img2 = Image.open('images\my_fonts\\'+text[i]+' .png')
        else:
            img2 = Image.open('images\my_fonts\\'+text[i]+'.png')

        x = x + 13

        if text[i] != '~':

            img2.thumbnail((33, 33))
            main_img.paste(img2, (x, y), mask=img2)

        if text[i] == 'l' or text[i] == 'i' or text[i] == ',' or text[i] == "'":
            x = x - 6

    main_img.save(f'temp_text_to_handwriting.png')

    img = PhotoImage(file=r'temp_text_to_handwriting.png')

    final_img = Label(root, image=img, borderwidth=3, relief="flat")
    final_img.photo = img
    final_img.place(x=800, y=20)

    correct_img = PhotoImage(file=r'images\correct_img_50x50.png')

    save_btn = Button(root, image=correct_img, bg='#6999fa',
                      command=save_img, borderwidth=0, relief='flat')
    save_btn.photo = correct_img
    save_btn.place(x=950, y=665)


if __name__ == "__main__":

    root = Tk()
    root.configure(background='#6999fa')
    root.state("zoomed")
    root.title("Text To Handwriting")

    text_area = Text(height=26, width=31, font=("Arial", 16),
                     relief='solid', borderwidth=3, insertbackground="red")
    text_area.place(x=70, y=20)
    

    text_area.insert('1.0', 'Start Writing from here...')

    convert_btn = Button(root, text='CONVERT', font=(
        "Comic Sans MS", 14, 'bold'), command=convert_press, borderwidth=3,relief="solid")
    convert_btn.place(x=575, y=350)

    img = PhotoImage(file=r'images\lined_paper.png')

    blank_img = Label(root, image=img, borderwidth=3, relief="flat")
    blank_img.photo = img
    blank_img.place(x=800, y=20)

    root.mainloop()
