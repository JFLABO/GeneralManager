# OpenGLとGLFWをインポートします
from OpenGL.GL import *
import glfw
def main():
	# GLFW初期化
	if not glfw.init():
		return

	# ウィンドウを作成
	#window = glfw.create_window(640, 480, 'Hello World', None, None)
	#if not window:
	#    glfw.terminate()
	#    print('Failed to create window')
	#    return

	# コンテキストを作成
	#glfw.make_context_current(openGLWidget)

	# OpenGLのバージョン等を表示します
	print('Vendor :', glGetString(GL_VENDOR))
	print('GPU :', glGetString(GL_RENDERER))
	print('OpenGL version :', glGetString(GL_VERSION))

	# バージョンを指定
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
	#while not glfw.window_should_close(openGLWidget):
	# バッファを指定色で初期化
	glClearColor(0.5, 5, 0.5, 1)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# バッファを入れ替えて画面を更新
	#glfw.swap_buffers(openGLWidget)
	# イベントを受け付けます
	glfw.poll_events()

	# ウィンドウを破棄してGLFWを終了
	#glfw.destroy_window(window)
	#glfw.terminate()


