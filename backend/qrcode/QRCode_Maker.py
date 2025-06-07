import streamlit as st
import qrcode


class QRCode:
    def __init__(self, link, color, backcolor):
        self.link = link
        self.color = color
        self.backcolor = backcolor

    def qrcode(self):
        qr = qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=40,
                            border=2)

        qr.add_data(self.link)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.color, back_color=self.backcolor)
        img.save("advanced.png")



st.title("QR Code Maker")

st.write("Generate a custom QR code by entering your link and choosing colors.")

link = st.text_input("URL for QR-code", "https://example.com")
color = st.color_picker("Foreground color", "#000000")
backcolor = st.color_picker("Background color", "#ffffff")

if st.button("Generate QR Code"):
    qr = QRCode(link, color, backcolor)
    qr.qrcode()
    st.image("advanced.png", caption="Your QR Code", width=400)
