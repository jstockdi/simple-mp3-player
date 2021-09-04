import os

def make_pages():

    mp3_list = {
      "Allegro Maestoso": "https://archive.org/download/01mozartpianoconcerto19inf/01%20Mozart_%20Piano%20Concerto%20%2319%20In%20F.mp3",
      "Allegretto": "https://archive.org/download/01mozartpianoconcerto19inf/02%20Mozart_%20Piano%20Concerto%20%2319%20In%20F.mp3"
    }
    
    html = ""

    for mp3 in mp3_list.keys():
        html += "<div><a href=" + mp3_list[mp3] + ">" + mp3 + "</a></div>"

    
    try:
      os.mkdir("dist")
    except FileExistsError:
      print("dist already exists")
      
    with open("dist/mp3-player.html", "w") as writer:
        writer.write(html)
 

if __name__ == "__main__":
    make_pages()

