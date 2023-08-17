import json
import os
import http.server
import socketserver


GLYPHS = json.load(open("/app/glyphs.json"))
FLAG = os.getenv("GZCTF_FLAG") or "NepCTF{testflag}"


def build():
    program = "10 END\n"
    for x in range(20, (len(FLAG) + 1) * 10, 10):
        program += f"{x} PRINT {GLYPHS[FLAG[x // 10 - 1]]}\n"
    open("/app/attachment.bas", "w").write(program)
    os.popen(
        "/app/trs80-tool convert /app/attachment.bas /app/attachment/attachment.wav")


if __name__ == "__main__":
    build()
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", 8081), Handler)
    os.chdir("/app/attachment/")
    print("[*] UP", 8081)
    httpd.serve_forever()
