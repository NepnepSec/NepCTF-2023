import base64
import json
import wave
import os
import numpy as np
import http.server
import socketserver


SILENCE = np.array([0]*12348)
START = np.array(([-30000]*28+[30000]*29)*8192)
TAPE_IN = np.array([-30000]*9+[30000]*11)
ZERO = np.array([-30000]*11+[30000]*11)
ONE = np.array([-30000]*22+[30000]*22)
GLYPHS = json.load(open("/app/glyphs.json", "r"))


def bit2wav(data):
    wav = np.array([])
    for b in data:
        for bit in range(0, 8):
            if (b & 1):
                wav = np.append(wav, ONE * 1)
            else:
                wav = np.append(wav, ZERO * 1)
            b = b >> 1
    return wav


def sum2bin(data):
    sum = 0
    for b in data:
        sum = sum ^ b
    return (~sum & 0b11111111).to_bytes(1, "big")


def build():
    FLAG = os.getenv("GZCTF_FLAG") or "NepCTF{testflag-test-test-test-test}"
    flag_data = b""

    for c in FLAG:
        flag_data += base64.b64decode(GLYPHS[c])
    flag_data += b"\xff\xff"

    extent = open("/app/bin1.bin", "rb").read()
    sum = sum2bin(flag_data + extent)
    flag_wav = bit2wav(flag_data)

    f = wave.open("/app/attachment/attachment", 'wb')
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    f.setcomptype('NONE', 'not compressed')

    wav = np.repeat(SILENCE, 10)
    wav = np.append(wav, START)
    wav = np.append(wav, TAPE_IN)

    wav = np.append(wav, flag_wav)
    wav = np.append(wav, np.load("/app/bin1.npy"))
    wav = np.append(wav, bit2wav(sum))

    wav = np.append(wav, SILENCE)
    wav = np.append(wav, START * -1)
    wav = np.append(wav, TAPE_IN * -1)
    wav = np.append(wav, np.load("/app/bin2.npy"))
    wav = np.append(wav, SILENCE)
    wave_data = wav.astype(np.int16).tobytes()

    f.writeframes(wave_data)
    f.close()


if __name__ == "__main__":
    build()
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", 8081), Handler)
    os.chdir("/app/attachment")
    print("[*] UP", 8081)
    httpd.serve_forever()
