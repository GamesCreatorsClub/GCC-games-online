package org.ah.libgdx.pygame;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.Rectangle;

import org.ah.libgdx.pygame.modules.pygame.PyGameModule;
import org.ah.libgdx.pygame.python.Modules;
import org.ah.libgdx.pygame.utils.GDXUtil;
import org.ah.python.grammar.PythonParser;
import org.ah.python.grammar.PythonScannerFixed;
import org.ah.python.interpreter.GlobalScope;
import org.ah.python.interpreter.Module;
import org.ah.python.interpreter.PythonObject;
import org.ah.python.interpreter.PythonString;
import org.ah.python.interpreter.Suite;
import org.ah.python.interpreter.While;

import java.io.StringReader;
import java.util.List;

import static org.ah.python.interpreter.PythonBoolean.FALSE;
import static org.ah.python.interpreter.PythonBoolean.TRUE;

public class PyGameLibGDX extends ApplicationAdapter implements InputProcessor {

    private Rectangle screenRect;
    private OrthographicCamera camera;
    private SpriteBatch batch;
    private ShapeRenderer shapeRenderer;
    private BitmapFont font;

    private Suite mainLoop;

    private Module module;
//    private String pythonFileName;
    private String path;

    protected boolean startGame;

//    private String pythonCode;
    private int width = 1024;
    private int height = 768;

    public PyGameLibGDX(String path, Module module) {
        this.path = path;
        this.module = module;

//        PythonObject source = module.__getitem__(PythonString.valueOf("__sourcecode__"));
//        if (source != null) {
//            pythonCode = source.asString();
//        }
    }

//    public PyGameLibGDX(String pythonFileName) {
//        int i = pythonFileName.indexOf('/');
//        if (i < 0) {
//            path = "";
//        } else {
//            this.path = pythonFileName.substring(0, i);
//        }
//        this.pythonFileName = pythonFileName;
//    }

    public void setModule(Module module) {
        this.module = module;
    }

    @Override
    public void create() {
        screenRect = new Rectangle(0, 0, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());

        camera = new OrthographicCamera(screenRect.width, screenRect.height);
        camera.setToOrtho(true);
        camera.update();

        batch = new SpriteBatch();
        shapeRenderer = new ShapeRenderer();

        font = new BitmapFont(Gdx.files.internal("data/arial-15.fnt"), Gdx.files.internal("data/arial-15.png"), true);
        font.getData().setScale(2f, 2f);

        Gdx.input.setInputProcessor(this);

        if (module == null) {
            Modules.init();
        }

        PyGameModule.PYGAME_MODULE.setSpriteBatch(batch);
        PyGameModule.PYGAME_MODULE.setShapeRenderer(shapeRenderer);
        PyGameModule.PYGAME_MODULE.setFont(font);
        PyGameModule.PYGAME_MODULE.setCamera(camera);
        PyGameModule.PYGAME_MODULE.setPath(path);

//        if (module == null) {
//            pythonCode = GDXUtil.loadString(Gdx.files.internal(pythonFileName));
//
//            PythonScannerFixed scanner = new PythonScannerFixed(new StringReader(pythonCode));
//            PythonParser parser = new PythonParser(scanner);
//
//            parser.next();
//            parser.file_input();
//
//            module = parser.getModule();
//        }

        List<PythonObject> body = module.getSuite().asList();

        While whle = (While)body.get(body.size() - 1);

        body.remove(body.size() - 1);

        mainLoop = whle.getBody();

        module.__call__();
        GlobalScope.pushScope(module);
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
//            shapeRenderer.begin(ShapeType.Line);
            batch.begin();
        }
        mainLoop.__call__();
        if (!PyGameModule.ENABLE_SHAPE_RENDERER) {
//            shapeRenderer.end();
            batch.end();
        }
        PyGameModule.getPyGameEvent().getEvents().clear();
    }

    @Override
    public void resize(int width, int height) {
    }

    @Override
    public void pause() {
    }

    @Override
    public void resume() {
    }

    @Override
    public boolean keyDown(int keycode) {
//        PyGameModule.KEYS.asList().set(keycode, TRUE);
        PyGameModule.KEYS[keycode] = TRUE;
        return false;
    }

    @Override
    public boolean keyUp(int keycode) {
//        PyGameModule.KEYS.asList().set(keycode, FALSE);
        PyGameModule.KEYS[keycode] = FALSE;
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
        // processKeys(screenX, screenY);
        return false;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        PyGameModule.getPyGameEvent().addMouseUp(screenX, screenY);
        //        PyGameModule.KEYS.asList().set(Keys.LEFT, FALSE);
        //        PyGameModule.KEYS.asList().set(Keys.RIGHT, FALSE);
        //        PyGameModule.KEYS.asList().set(Keys.UP, FALSE);
        //        PyGameModule.KEYS.asList().set(Keys.DOWN, FALSE);
        //        PyGameModule.KEYS.asList().set(Keys.ENTER, FALSE);
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
//
//    public void setPythonFileName(String pythonFileName) {
//        this.pythonFileName = pythonFileName;
//    }

    @Override
    public boolean scrolled(float amountX, float amountY) {
        // TODO Auto-generated method stub
        return false;
    }


    public int getWidth() { return this.width; }
    public void setWidth(int width) { this.width = width; }

    public int getHeight() { return this.height; }
    public void setHeight(int height) { this.height = height; }

}
