import os

def encrypt(text, shift=3):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


texts = [
    """In the midst of the pandemic, it became evident that digital security is paramount. With the increasing number of cyber threats, protecting personal and sensitive information has never been more crucial. Organizations must adopt robust security measures to safeguard their data and ensure continuity of operations.""",
    """The importance of cybersecurity cannot be overstated. As more aspects of our lives move online, the potential for data breaches and cyberattacks increases. It is essential to stay informed about the latest security trends and adopt best practices to protect our digital assets.""",
    """Investing in cybersecurity infrastructure is a necessity for modern organizations. Cybercriminals are constantly evolving their tactics, making it imperative to stay ahead of potential threats. Comprehensive security protocols and regular system updates can significantly reduce the risk of cyber incidents.""",
    """As technology advances, the need for effective cybersecurity measures becomes more critical. Companies must prioritize the protection of their digital infrastructure to prevent unauthorized access and data breaches. This involves implementing advanced encryption techniques and educating employees on security best practices."""
]


bat_filename = "script.bat"


with open(bat_filename, "w") as file:
    for i, text in enumerate(texts):
        encrypted_text = encrypt(text)
        file.write(f":: Texto {i+1} encriptografado\n")
        file.write(f"echo {encrypted_text}\n")
        file.write("echo.\n")


os.system(f"start cmd /k {bat_filename}")

