"""로컬 미리보기용 정적 서버.

기본 `python3 -m http.server` 는 요청을 하나씩만 처리해서, 관리자 화면이
미리보기 iframe 과 content/*.json 20여 개를 한꺼번에 가져올 때 연결이 끊긴다.
스레드형으로 띄우고 캐시를 끄면 그 문제가 사라진다.
"""
import http.server
import socketserver

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 고친 내용이 곧바로 보이도록 캐시를 끈다
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):  # 요청 로그는 조용히
        pass


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Server(("127.0.0.1", PORT), Handler) as httpd:
        print(f"http://localhost:{PORT} 에서 실행 중")
        httpd.serve_forever()
