package org.ah.libgdx.pygame;

import org.ah.libgdx.pygame.modules.pygame.PyGameDisplay;
import org.ah.libgdx.pygame.modules.pygame.PyGameDisplay.WindowSizeCallback;
import org.ah.libgdx.pygame.modules.pygame.PyGameModule;
import org.ah.libgdx.pygame.python.Modules;
import org.ah.python.interpreter.Module;
import org.ah.python.interpreter.ThreadContext;
import org.ah.python.interpreter.ThreadContext.Executable;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.HdpiUtils;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class PyGameLibGDX extends ApplicationAdapter implements InputProcessor, WindowSizeCallback {

    private OrthographicCamera camera;
    private SpriteBatch batch;
    private ShapeRenderer shapeRenderer;
    private BitmapFont font;

    private ThreadContext context;

    private Module module;

    @SuppressWarnings("unused")
    private String path;

    protected boolean startGame;

    private int width = 1024;
    private int height = 256;

    public PyGameLibGDX(String path, Module module) {
        this.path = path;
        this.module = module;

        PyGameModule.PYGAME_MODULE.setPath(path);

        context = new ThreadContext(module);
        context.setCurrentScope(module);
        context.continuation(module.getBlock());
    }

    public void setModule(Module module) {
        this.module = module;
    }

    @Override
    public void create() {
        int width = Gdx.graphics.getWidth();
        int height = Gdx.graphics.getHeight();

        camera = new OrthographicCamera(width, height);
        camera.setToOrtho(true);
        camera.position.set(width / 2, height / 2, 0);
        camera.update();

        batch = new SpriteBatch();
        shapeRenderer = new ShapeRenderer();

        font = new BitmapFont(Gdx.files.internal("data/arial-15.fnt"), Gdx.files.internal("data/arial-15.png"), true);
        font.getData().setScale(2f, 2f);

        Gdx.input.setInputProcessor(this);

        if (module == null) {
            Modules.init();
        }

        PyGameDisplay.windowSizeCallback = this;
        PyGameModule.PYGAME_MODULE.setSpriteBatch(batch);
        PyGameModule.PYGAME_MODULE.setShapeRenderer(shapeRenderer);
        PyGameModule.PYGAME_MODULE.setFont(font);
        PyGameModule.PYGAME_MODULE.setCamera(camera);
        PyGameModule.PRE_RUN = false;
    }

    @Override
    public void dispose() {
        batch.dispose();
    }

    @Override
    public void render() {
        shapeRenderer.setProjectionMatrix(camera.combined);
        batch.setProjectionMatrix(camera.combined);

        if (!PyGameModule.ENABLE_SHAPE_RENDERER) {
            // shapeRenderer.begin(ShapeType.Line);
            batch.begin();
        }

        try {
            PyGameModule.flip = false;
            boolean eof = false;
            while (!eof && !PyGameModule.flip) {
                if (context.pcStack.isEmpty()) {
                    eof = true;
                }

                Executable pc = context.pcStack.pop();
                pc.evaluate(context);
            }
        } catch (Exception e) {
            throw new RuntimeException(context.position() + e.getMessage(), e);
        }

        if (!PyGameModule.ENABLE_SHAPE_RENDERER) {
            // shapeRenderer.end();
            batch.end();
        }
        PyGameModule.getPyGameEvent().getEvents().clear();
        PyGameModule.flip = false;
    }

    @Override
    public void resize(int width, int height) {
        HdpiUtils.glViewport(0, 0, width, height);

        camera.setToOrtho(true, width, height);
    }

    @Override
    public void pause() {
    }

    @Override
    public void resume() {
    }

    @Override
    public boolean keyDown(int keycode) {
        PyGameModule.keyDown(keycode);
        return false;
    }

    @Override
    public boolean keyUp(int keycode) {
        PyGameModule.keyUp(keycode);
        return false;
    }

    @Override
    public boolean keyTyped(char character) {
        return false;
    }

//    protected void processKeys(int screenX, int screenY) {
//        float ratio = screenRect.height / screenRect.width;
//        int w = (int)screenRect.width;
//        int h = (int)screenRect.height;
//
//        if ((screenX > w / 3 && screenX < w - w / 3)
//                && (screenY > h / 3 && screenX < h - h / 3)) {
//
//            PyGameModule.KEYS.asList().set(Keys.ENTER, TRUE);
//            PyGameModule.KEYS.asList().set(Keys.LEFT, FALSE);
//            PyGameModule.KEYS.asList().set(Keys.RIGHT, FALSE);
//            PyGameModule.KEYS.asList().set(Keys.UP, FALSE);
//            PyGameModule.KEYS.asList().set(Keys.DOWN, FALSE);
//
//        } else {
//            PyGameModule.KEYS.asList().set(Keys.ENTER, FALSE);
//            if (screenY < screenX * ratio) {
//                if (screenY < (screenRect.width - screenX) * ratio) {
//                    PyGameModule.KEYS.asList().set(Keys.LEFT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.RIGHT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.UP, TRUE);
//                    PyGameModule.KEYS.asList().set(Keys.DOWN, FALSE);
//                } else {
//                    PyGameModule.KEYS.asList().set(Keys.LEFT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.RIGHT, TRUE);
//                    PyGameModule.KEYS.asList().set(Keys.UP, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.DOWN, FALSE);
//                }
//            } else {
//                if (screenY < (screenRect.width - screenX) * ratio) {
//                    PyGameModule.KEYS.asList().set(Keys.LEFT, TRUE);
//                    PyGameModule.KEYS.asList().set(Keys.RIGHT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.UP, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.DOWN, FALSE);
//                } else {
//                    PyGameModule.KEYS.asList().set(Keys.LEFT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.RIGHT, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.UP, FALSE);
//                    PyGameModule.KEYS.asList().set(Keys.DOWN, TRUE);
//                }
//            }
//        }
//    }

    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        PyGameModule.getPyGameEvent().addMouseDown(screenX, screenY);
        return false;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        PyGameModule.getPyGameEvent().addMouseUp(screenX, screenY);
        return false;
    }

    @Override
    public boolean touchDragged(int screenX, int screenY, int pointer) {
        return false;
    }

    @Override
    public boolean mouseMoved(int screenX, int screenY) {
        PyGameModule.getPyGameEvent().addMouseMotion(screenX, screenY);
        return false;
    }

    @Override
    public boolean scrolled(float amountX, float amountY) {
        return false;
    }


    public int getWidth() { return this.width; }
    public void setWidth(int width) { this.width = width; }

    public int getHeight() { return this.height; }
    public void setHeight(int height) { this.height = height; }

    @Override
    public void setSize(int width, int height) {
        Gdx.graphics.setWindowedMode(width, height);
    }
}
