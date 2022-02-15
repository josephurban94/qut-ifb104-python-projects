# coding=utf-8
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****n8882959*****
#    Student name: *****Joseph Urban*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#


##### DEVELOP YOUR SOLUTION HERE #####
from sqlite3 import *


def top_book_list():
#allows the page_list function to be read by the save button on the splash page
    global page_list
#creates the book list window
    book_window = Toplevel(bg = 'cadetblue3')
    book_window.title('Top 10 Bestselling Books in the USA')

#fetches the html, then pulls the necessary items from the html with a regexp
    page_url = "http://www.usatoday.com/life/books/best-selling/"
    page_html = urlopen(page_url).read()
    page_list = findall("""[A-Za-z0-9'\-:,! ’â€™]+(?=<\/h3>)""", page_html)

#truncates the list to be only 10 items long if applicable, and replaces problem characters
    page_list = page_list[0:10]
    page_list = [item.replace('’', """'""") for item in page_list]

#adds the banner image to the window
    book_image = urlopen('https://s3.amazonaws.com/kajabi-storefronts-production/site/1157/images/7njAztRcQAmJiTmLMHA2_Best-Seller-Logo.png').read()
    book_image_use = image_to_PhotoImage(book_image, 500, 400)
    book_image_label = Label(book_window, image = book_image_use)
    book_image_label.image = book_image_use #keep a reference
    book_image_label.grid(row = 0, columnspan=3)

#enables the save button on the splash page now that a list has been pulled
    save_button.config(state = NORMAL)

#inserts the top 10 list into the window, adding the number of each item
    list_counter = 0
    book_list = Text(book_window, height = 10, width = 40, font = 'Arial 16 italic bold', fg = 'gold4', bg = 'cadetblue3', bd = 0)
    for entry in page_list:
        book_list.insert(INSERT, str(list_counter+1))
        book_list.insert(INSERT, ': ')
        book_list.insert(INSERT, str(page_list[list_counter]))
        book_list.insert(END, '\n')
        
        list_counter = list_counter + 1
    book_list.grid()

#source url with beautiful styling
    source_book_label = Label(book_window, text = page_url, bg = 'dark gray', fg = 'green', bd = 5, font = 'Arial 15 bold', relief = GROOVE)
    source_book_label.grid(row = 3, padx = 5, pady = 5)

    
def top_nrl_ladder():
#allows the page_list function to be read by the save button on the splash page
    global page_list
#creates the nrl list window
    nrl_window = Toplevel(bg = 'black')
    nrl_window.title('Top 10 NRL Teams')

#fetches the html, then pulls the necessary items from the html with a regexp
    page_url = "https://www.nrl.com/draw/telstrapremiership/ladder/tabid/10251/default.aspx"
    page_html = urlopen(page_url).read()
    page_list = findall('(?<=div>)([A-Z][a-z]+ ?[A-Z]*[a-z]*)', page_html)

#truncates the list to be only 10 items long
    page_list = page_list[0:10]

#adds the banner image to the window
    nrl_image = urlopen('https://www.melbournestorm.com.au/content/storm/club/news/2015/12/15/nrl_blueprint_for_th/_jcr_content/par/image.img.jpg/1450138917019.jpg').read()
    nrl_image_use = image_to_PhotoImage(nrl_image, 450, 200)
    nrl_image_label = Label(nrl_window, image = nrl_image_use, bd = 0)
    nrl_image_label.image = nrl_image_use #keep a reference
    nrl_image_label.grid(row = 1)

#enables the save button on the splash page now that a list has been pulled
    save_button.config(state = NORMAL)

#inserts the top 10 list into the window, adding the number of each item
    list_counter = 0
    nrl_list = Text(nrl_window, height = 10, width = 15, relief = FLAT, bg = 'black', fg = 'red', bd = 5, font = 'Arial 15 bold')
    for entry in page_list:
        nrl_list.insert(INSERT, str(list_counter+1))
        nrl_list.insert(INSERT, ': ')
        nrl_list.insert(INSERT, str(page_list[list_counter]))
        nrl_list.insert(END, '\n')
        
        list_counter = list_counter + 1
    nrl_list.grid(row = 2)

#source url with beautiful styling
    source_nrl_label = Label(nrl_window, text = page_url, bg = 'black', fg = 'green')
    source_nrl_label.grid(row = 3, padx = 10, pady = 10)

    
def top_song_list():
#allows the page_list function to be read by the save button on the splash page
    global page_list

#creates the song list window
    song_window = Toplevel(bg = 'rosybrown2')
    song_window.title('ARIA Top 10 Australian Charting Songs')

#fetches the html, then pulls the necessary items from the html with a regexp
    page_url = "http://www.vmusic.com.au/charts/australian-singles-chart.aspx"
    page_html = urlopen(page_url).read()
    page_list = findall("""(?<=Album_[0-9]">)[A-Za-z0-9 '!\.\-&,]+|[A-Za-z0-9 '!\.\-&,]+</a> -[A-Za-z0-9 '!\.\-&,]+""", page_html)

#truncates the list to be only 10 items long, and replaces problem characters
    page_list = page_list[0:10]
    page_list = [item.replace('</a>', '') for item in page_list]

#adds the banner image to the window
    song_image = urlopen('https://yt3.ggpht.com/-LwrJpguaNKQ/AAAAAAAAAAI/AAAAAAAAAAA/ukvUHiFzpls/s900-c-k-no-rj-c0xffffff/photo.jpg').read()
    song_image_use = image_to_PhotoImage(song_image, 500, 500)
    song_image_label = Label(song_window, image = song_image_use)
    song_image_label.image = song_image_use #keep a reference
    song_image_label.grid(row = 1, rowspan = 2)

#enables the save button on the splash page now that a list has been pulled    
    save_button.config(state = NORMAL)

#inserts the top 10 list into the window, adding the number of each item
    list_counter = 0
    song_list = Text(song_window, height = 10, width = 50, bd = 0, font = ('ms serif', 17, 'bold'), bg = 'rosybrown2')
    for entry in page_list:
        song_list.insert(INSERT, str(list_counter+1))
        song_list.insert(INSERT, ': ')
        song_list.insert(INSERT, str(page_list[list_counter]))
        song_list.insert(END, '\n')
        
        list_counter = list_counter + 1
    song_list.grid(row = 1, column = 2)

#source url with beautiful styling
    source_song_label = Label(song_window, text = page_url, bg = 'rosybrown2', font = 'Helvetica 15 underline')
    source_song_label.grid(row = 2, column = 2)
    

def save_button():
    global page_list

#connect to db file
    connection = connect(database = 'top_ten.db')
    ten_db = connection.cursor()

#delete all previous items, if any, from table in db
    delete_table = 'DELETE from Top_Ten'
    ten_db.execute(delete_table)

#replace apostrophe with a different one because I didn't want to have to deal with the error it caused properly
    page_list = [item.replace("'", '’') for item in page_list]
    
    insert_info = "INSERT INTO top_ten VALUES ('Rank', 'Description')"
    counter = range(10)
    counter_2 = 1
#for some reason I couldn't get the counter to work properly without spitting out an 'list index out of range' index error.
#I couldn't fix it, so I ended up using this slightly messier solution. It works though, so there's that
    for index in counter:
        insert_statement = insert_info.replace('Rank', str(counter_2)).replace('Description', str(page_list[index]))
        ten_db.execute(insert_statement)
        counter_2 = counter_2 + 1
#save changes to dp and end connection
    connection.commit()
    ten_db.close()
    connection.close()
        
#opens main splash window  
main = Tk()
main.title("Best Three Top Ten Lists!")
main.configure(bg = 'lavender')

#gives splash window an image banner
splash_image = urlopen('http://static.wixstatic.com/media/c85139_ead93f0b779a411fa6a69437ab196584.jpg_srz_1158_1435_85_22_0.50_1.20_0.00_jpg_srz').read()
splash_image_use = image_to_PhotoImage(splash_image, 600, 700)
splash_image_label = Label(main, image = splash_image_use, bd = 0)
splash_image_label.image = splash_image_use #keep a reference
splash_image_label.grid(row = 0, columnspan=3)

#some context for the user
splash_text = Label(main, text = 'Click a button below to view the current top 10 in each catagory!', font = 'Verdana 11 bold underline', fg = 'dark blue', bg = 'lavender') 
splash_text.grid(row = 2, columnspan = 3)

#buttons 1 - 3 to open each top 10 list
button_1 = Button(main, text = 'Top 10 Book Bestsellers (USA)', command = top_book_list)
button_1.grid(row = 3, column = 0, padx = 10, pady = 10)

button_2 = Button(main, text = 'Top 10 NRL Teams', command = top_nrl_ladder)
button_2.grid(row = 3, column = 1, padx = 10, pady = 10)

button_2 = Button(main, text = 'Top 10 ARIA Songs (Aus)', command = top_song_list)
button_2.grid(row = 3, column = 2, padx = 10, pady = 10)

# save button added for part B
save_button = Button(main, text = 'Save most recently accessed list!', command = save_button, state = DISABLED)
save_button.grid(row = 4, columnspan = 3, sticky = W+E, padx = 10, pady = 10)


main.mainloop()
