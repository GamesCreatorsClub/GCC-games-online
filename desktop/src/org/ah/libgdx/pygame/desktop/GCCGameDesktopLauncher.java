package org.ah.libgdx.pygame.desktop;

import java.io.IOException;
import java.io.InputStreamReader;

import org.ah.libgdx.pygame.PyGameLibGDX;
import org.ah.libgdx.pygame.python.CreateApplicationUtil;
import org.ah.libgdx.pygame.utils.GDXUtil;
import org.ah.python.interpreter.ModuleLoader;
import org.ah.python.modules.SysModule;

import com.badlogic.gdx.backends.lwjgl3.Lwjgl3Application;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;

public class GCCGameDesktopLauncher {

    public static void main(String[] arg) throws IOException {
        SysModule.systemBridge = new SysModule.SystemBridge() {
            @Override public void exit(int status) { System.exit(status); }
        };

        // PyGameLibGDX application = createApplication("shootingGame/ShootingGame.py");
        // PyGameLibGDX application = createApplication("gcc/MazeWithFunctions.py");
        // PyGameLibGDX application = createApplication("CaveQuest/maze.py");
        // PyGameLibGDX application = createApplication("game-of-circles/maze.py");
        // PyGameLibGDX application = createApplication("jonathan-phillips/Maze.py");
        // PyGameLibGDX application = createApplication("flappy-bird/Flappy-Bird.py");
        // PyGameLibGDX application = createApplication("transmission-to-mars/Transmission-to-mars.py");
        // PyGameLibGDX application = createApplication("guns-kills-people!!/JetPack.py");
        // PyGameLibGDX application = createApplication("game.py");

        String pythonFilename = "david-cave-quest/game.py";
//        String pythonFilename = "rpg-2023/game.py";

        if (arg.length > 0) {
            pythonFilename = arg[0];
        }

        final String gameDir;
        int i = pythonFilename.lastIndexOf("/");
        if (i > 0) {
            gameDir = pythonFilename.substring(0, i + 1);
            pythonFilename = pythonFilename.substring(i + 1);
        } else {
            gameDir = "";
        }

        if (pythonFilename.endsWith(".py")) {
            pythonFilename = pythonFilename.substring(0, pythonFilename.length() - 3);
        }

        ModuleLoader moduleLoader = new ModuleLoader() {
            @Override public String loadModule(String moduleName) throws IOException {
                String pythonFilename = gameDir + moduleName.replace(".", "/") + ".py";
                return GDXUtil.loadString(new InputStreamReader(Thread.currentThread().getContextClassLoader().getResource(pythonFilename).openStream()));
            }

            @Override public String getPathPrefix() {
                return gameDir;
            }
        };

        PyGameLibGDX application = CreateApplicationUtil.createApplication(pythonFilename, moduleLoader);

        Lwjgl3ApplicationConfiguration cfg = new Lwjgl3ApplicationConfiguration();
        cfg.setTitle( "pygame-libgdx");
        cfg.setWindowedMode(application.getWidth(), application.getHeight());

        new Lwjgl3Application(application, cfg);
    }
}
