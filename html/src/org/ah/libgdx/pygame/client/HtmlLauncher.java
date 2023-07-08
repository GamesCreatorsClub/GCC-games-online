package org.ah.libgdx.pygame.client;

import java.io.IOException;
import java.io.InputStreamReader;

import org.ah.libgdx.pygame.PyGameLibGDX;
import org.ah.libgdx.pygame.python.CreateApplicationUtil;
import org.ah.libgdx.pygame.utils.GDXUtil;
import org.ah.python.interpreter.ModuleLoader;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.backends.gwt.GwtApplication;
import com.badlogic.gdx.backends.gwt.GwtApplicationConfiguration;
import com.badlogic.gdx.files.FileHandle;
import com.google.gwt.core.client.GWT;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Panel;

public class HtmlLauncher extends GwtApplication {

    @Override
    public GwtApplicationConfiguration getConfig() {

        GwtApplicationConfiguration cfg = new GwtApplicationConfiguration(1024, 768);
        return cfg;
    }

    public String getPathPrefix() {
        String p = Window.Location.getHash();
        consoleLog("Window.Location.getHash()=" + p);
        if (p.startsWith("#")) {
            p = p.substring(1);
            if (!p.endsWith("/")) { p = p + "/"; }
        } else {
            p = "";
        }
        return p;
    }

    @Override
    public ApplicationListener createApplicationListener () {
        ApplicationListener applicationListener = new ApplicationListener() {
            PyGameLibGDX game;

            @Override
            public void create() {
                String pythonFileName = "game.py";
                if (pythonFileName.endsWith(".py")) {
                    pythonFileName = pythonFileName.substring(0, pythonFileName.length() - 3);
                }

                consoleLog("Loading "+ "assets/" + pythonFileName);
                final String gameDir = "";

                ModuleLoader moduleLoader = new ModuleLoader(gameDir) {
                    @Override
                    protected String loadModuleSourceCodeFromName(String moduleName) throws IOException {
                      String pythonFilename = gameDir + moduleName.replace(".", "/") + ".py";
                      consoleLog("pythonFilename=" + pythonFilename);
                      FileHandle handle = Gdx.files.internal(pythonFilename);
                      return GDXUtil.loadString(new InputStreamReader(handle.read()));
                    }
                };

                try {
                    this.game = CreateApplicationUtil.createApplication(pythonFileName, moduleLoader);
                    int width = game.getWidth();
                    int height = game.getHeight();
                    consoleLog("Got dimensions as [" +  width + "," + height + "]");
                    Gdx.graphics.setWindowedMode(width, height);
                    consoleLog("Setting size..");
                    Panel rootPanel = getRootPanel();
                    consoleLog("Setting size....");
                    rootPanel.setWidth("" + width + "px");
                    rootPanel.setHeight("" + height + "px");
                    consoleLog("Set size.");
                } catch (IOException e) {
                    consoleLog("Got exception " + e);
                    throw new RuntimeException(e);
                }

                game.create();
            }

            @Override
            public void resize(int width, int height) {
                game.resize(width, height);
            }

            @Override
            public void render() {
                game.render();
            }

            @Override
            public void pause() {
                game.render();
            }

            @Override
            public void resume() {
                game.resume();
            }

            @Override
            public void dispose() {
                game.dispose();
            }

        };
        return applicationListener;
    }

    @Override
    public String getPreloaderBaseURL() {
        return GWT.getHostPageBaseURL() + getPathPrefix() + "assets/";
    }
}