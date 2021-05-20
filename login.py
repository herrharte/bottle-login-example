from bottle import route, run

# watch https://www.youtube.com/watch?v=g_9nsFJS_pk&list=PLXmMXHVSvS-AyIwEYkGNa4WE1AR1_45mv&index=1 first
@route('/')
def hallo():
    return "Hallo Herr Harte!"

if __name__ == '__main__':
    run(debug=True, reloader=True)
