import qrcode

# images = qrcode.make("https://www.facebook.com/sagorhosenrased/")

# images.save("sagor.jpg")

with open ("english_news_websites_500.csv", "r") as file:
    for i in file:
        data = i.strip("\n")
        updated_data = data.split(",")
        images = qrcode.make(f"{updated_data[1]}")
        images.save(f"{updated_data[0]}.jpg")