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


def main():
    l = input("Give url for QR-code: ")
    c = input("Give foreground color for QR-code: ")
    b = input("Give background color for QR-code: ")
    q = QRCode(l, c, b)
    q.qrcode()

if __name__ == "__main__":
    main()
